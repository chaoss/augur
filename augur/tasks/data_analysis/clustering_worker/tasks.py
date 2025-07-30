import logging
import os
import time
import traceback
import re
import pickle
import uuid
import datetime
import json

import sqlalchemy as s
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# LDA import removed as we're using NMF model
# from sklearn.decomposition import LatentDirichletAllocation  as LDA
from collections import OrderedDict
from textblob import TextBlob
from collections import Counter
from sklearn.decomposition import NMF

from augur.tasks.init.celery_app import celery_app as celery
from augur.application.db.lib import get_value, get_session, get_repo_by_repo_git
from augur.application.db.models import RepoClusterMessage, RepoTopic, TopicWord, TopicModelMeta
from augur.tasks.init.celery_app import AugurMlRepoCollectionTask

# HDP model import removed as we're using NMF+Count model
# from gensim.models import HdpModel
# import gensim.corpora as corpora


MODEL_FILE_NAME = "kmeans_repo_messages"
stemmer = nltk.stem.snowball.SnowballStemmer("english")

# --- Configuration Loading ---
# This section loads configuration from config.json file if available,
# otherwise falls back to database configuration.
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

def replace_env_vars(value):
    """Replace environment variables in string values"""
    if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
        # Extract variable name and default value
        var_content = value[2:-1]  # Remove ${ and }
        if ':-' in var_content:
            var_name, default_value = var_content.split(':-', 1)
        else:
            var_name = var_content
            default_value = ''
        
        # Get environment variable or use default
        env_value = os.getenv(var_name, default_value)
        
        # Try to convert to appropriate type
        try:
            if default_value.isdigit():
                return int(env_value)
            if default_value.replace('.', '').isdigit():
                return float(env_value)
            return env_value
        except (ValueError, AttributeError):
            return env_value
    
    return value

def load_config_with_env_vars(config_dict):
    """Recursively replace environment variables in config dictionary"""
    if isinstance(config_dict, dict):
        for key, value in config_dict.items():
            config_dict[key] = load_config_with_env_vars(value)
    elif isinstance(config_dict, list):
        for i, item in enumerate(config_dict):
            config_dict[i] = load_config_with_env_vars(item)
    elif isinstance(config_dict, str):
        return replace_env_vars(config_dict)
    
    return config_dict


@celery.task(base=AugurMlRepoCollectionTask, bind=True, queue='ml')
def clustering_task(self, repo_git):

    logger = logging.getLogger(clustering_model.__name__)
    engine = self.app.engine

    clustering_model(repo_git, logger, engine)

def clustering_model(repo_git: str,logger,engine) -> None:
    """
    Main entry for clustering and topic modeling on repository messages.
    Loads parameters from config.json if available, otherwise from database config table.
    Config parameters:
      - db: Database connection info (used for standalone runs)
      - topic_modeling.num_topics: Number of topics for NMF model (int)
      - topic_modeling.min_df: Min document frequency for vectorizer (int)
      - topic_modeling.max_df: Max document frequency for vectorizer (float)
      - topic_modeling.random_state: Random seed (int)
      - topic_modeling.coherence_metric: Coherence metric (str)
      - topic_modeling.retrain_days: Retrain if last model older than this (int, days)
      - topic_modeling.retrain_msg_growth: Retrain if message count grows by this fraction (float)
      - topic_modeling.output_dir: Where to save models/visualizations (str)
    """
    logger.info(f"Starting clustering analysis for {repo_git}")

    # Load topic modeling parameters from config.json or database
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            # Replace environment variables in config
            config = load_config_with_env_vars(config)
            topic_cfg = config.get('Clustering_Task', {})
            num_topics = int(topic_cfg.get('num_topics', 8))
            min_df = int(topic_cfg.get('min_df', 2))
            max_df = float(topic_cfg.get('max_df', 0.8))
            max_features = int(topic_cfg.get('max_features', 1000))
            num_words_per_topic = int(topic_cfg.get('num_words_per_topic', 12))
            num_clusters = int(topic_cfg.get('num_clusters', 5))
            random_state = int(topic_cfg.get('random_state', 42))
            coherence_metric = topic_cfg.get('coherence_metric', 'c_v')
            retrain_days = int(topic_cfg.get('retrain_days', 90))
            retrain_msg_growth = float(topic_cfg.get('retrain_msg_growth', 0.2))
            output_dir = topic_cfg.get('output_dir', 'artifacts/topic_models')
            ngram_range = (1, 4)  # Default ngram range
            clustering_by_content = True
            clustering_by_mechanism = False
            logger.info("Configuration loaded from config.json file")
    else:
        # Fallback to database configuration
        num_topics = get_value("Clustering_Task", 'num_topics') or 8
        min_df = get_value("Clustering_Task", 'min_df') or 2
        max_df = get_value("Clustering_Task", 'max_df') or 0.8
        max_features = get_value("Clustering_Task", 'max_features') or 1000
        num_words_per_topic = get_value("Clustering_Task", 'num_words_per_topic') or 12
        num_clusters = get_value("Clustering_Task", 'num_clusters') or 5
        random_state = get_value("Clustering_Task", 'random_state') or 42
        coherence_metric = get_value("Clustering_Task", 'coherence_metric') or 'c_v'
        retrain_days = get_value("Clustering_Task", 'retrain_days') or 90
        retrain_msg_growth = get_value("Clustering_Task", 'retrain_msg_growth') or 0.2
        output_dir = get_value("Clustering_Task", 'output_dir') or 'artifacts/topic_models'
        ngram_range = (1, 4)
        clustering_by_content = True
        clustering_by_mechanism = False
        logger.info("Configuration loaded from database")

    tool_source = 'Clustering Worker'
    tool_version = '0.3.0'
    data_source = 'Augur Collected Messages'

    repo_id = get_repo_by_repo_git(repo_git).repo_id

    logger.info(f"Min df: {min_df}. Max df: {max_df}")

    logger.info("If you did not install NLTK libraries when you installed Augur, this will fail. ")
    #nltk.download('all')

    logger.info(f"Getting repo messages for repo_id: {repo_id}")
    get_messages_for_repo_sql = s.sql.text(
        """
            SELECT
                r.repo_group_id,
                r.repo_id,
                r.repo_git,
                r.repo_name,
                i.issue_id thread_id,
                M.msg_text,
                i.issue_title thread_title,
                M.msg_id 
            FROM
                augur_data.repo r,
                augur_data.issues i,
                augur_data.message M,
                augur_data.issue_message_ref imr 
            WHERE
                r.repo_id = i.repo_id 
                AND imr.issue_id = i.issue_id 
                AND imr.msg_id = M.msg_id 
                AND r.repo_id = :repo_id 
            UNION
            SELECT
                r.repo_group_id,
                r.repo_id,
                        r.repo_git,
                r.repo_name,
                pr.pull_request_id thread_id,
                M.msg_text,
                pr.pr_src_title thread_title,
                M.msg_id 
            FROM
                augur_data.repo r,
                augur_data.pull_requests pr,
                augur_data.message M,
                augur_data.pull_request_message_ref prmr 
            WHERE
                r.repo_id = pr.repo_id 
                AND prmr.pull_request_id = pr.pull_request_id 
                AND prmr.msg_id = M.msg_id 
                AND r.repo_id = :repo_id
            """
    )
    # result = db.execute(delete_points_SQL, repo_id=repo_id, min_date=min_date)

    with engine.connect() as conn:
        msg_df_cur_repo = pd.read_sql(get_messages_for_repo_sql, conn, params={"repo_id": repo_id})
    logger.info(msg_df_cur_repo.head())
    logger.debug(f"Repo message df size: {len(msg_df_cur_repo.index)}")

    # check if dumped pickle file exists, if exists no need to train the model
    if not os.path.exists(MODEL_FILE_NAME):
        logger.info("clustering model not trained. Training the model.........")
        train_model(logger, engine, max_df, min_df, max_features, ngram_range, num_clusters, num_topics, num_words_per_topic, tool_source, tool_version, data_source)
    else:
        model_stats = os.stat(MODEL_FILE_NAME)
        model_age = (time.time() - model_stats.st_mtime)
        # if the model is more than month old, retrain it.
        logger.debug(f'model age is: {model_age}')
        if model_age > 2000000:
            logger.info("clustering model to old. Retraining the model.........")
            train_model(logger, engine, max_df, min_df, max_features, ngram_range, num_clusters, num_topics, num_words_per_topic, tool_source, tool_version, data_source)
        else:
            logger.info("using pre-trained clustering model....")

    with open("kmeans_repo_messages", 'rb') as model_file:
        kmeans_model = pickle.load(model_file)

    msg_df = msg_df_cur_repo.groupby('repo_id')['msg_text'].apply(','.join).reset_index()

    logger.debug(f'messages being clustered: {msg_df}')

    if msg_df.empty:
        logger.info("not enough data for prediction")
        # self.register_task_completion(task, repo_id, 'clustering')
        return

    vocabulary = pickle.load(open("vocabulary", "rb"))

    tfidf_vectorizer = TfidfVectorizer(max_df=max_df, max_features=max_features,
                                       min_df=min_df, stop_words='english',
                                       use_idf=True, tokenizer=preprocess_and_tokenize,
                                       ngram_range=ngram_range, vocabulary=vocabulary)
    tfidf_transformer = tfidf_vectorizer.fit(
        msg_df['msg_text'])  # might be fitting twice, might have been used in training

    # save new vocabulary ??
    feature_matrix_cur_repo = tfidf_transformer.transform(msg_df['msg_text'])

    prediction = kmeans_model.predict(feature_matrix_cur_repo)
    logger.info("prediction: " + str(prediction[0]))

    with get_session() as session:

        # inserting data
        record = {
            'repo_id': int(repo_id),
            'cluster_content': int(prediction[0]),
            'cluster_mechanism': -1,
            'tool_source': tool_source,
            'tool_version': tool_version,
            'data_source': data_source
        }
        repo_cluster_messages_obj = RepoClusterMessage(**record)
        session.add(repo_cluster_messages_obj)
        session.commit()

    # result = db.execute(repo_cluster_messages_table.insert().values(record))
    logging.info(
        "Primary key inserted into the repo_cluster_messages table: {}".format(repo_cluster_messages_obj.msg_cluster_id))
    try:
        logger.debug('loading NMF model')
        nmf_model = pickle.load(open("nmf_model", "rb"))
        logger.debug('loading count vocabulary')
        vocabulary = pickle.load(open("vocabulary_count", "rb"))
        logger.debug('count vectorizing vocab')
        count_vectorizer = CountVectorizer(max_df=max_df, max_features=max_features, min_df=min_df,
                                           stop_words="english", tokenizer=preprocess_and_tokenize,
                                           vocabulary=vocabulary)
        logger.debug('count transforming vocab')
        count_transformer = count_vectorizer.fit(
            msg_df['msg_text'])  # might be fitting twice, might have been used in training

        # save new vocabulary ??
        logger.debug('count matrix cur repo vocab')
        count_matrix_cur_repo = count_transformer.transform(msg_df['msg_text'])
        logger.debug('NMF prediction vocab')
        prediction = nmf_model.transform(count_matrix_cur_repo)

        with get_session() as session:

            logger.debug('for loop for vocab')
            for i, prob_vector in enumerate(prediction):
                # repo_id = msg_df.loc[i]['repo_id']
                for i, prob in enumerate(prob_vector):
                    record = {
                        'repo_id': int(repo_id),
                        'topic_id': i + 1,
                        'topic_prob': prob,
                        'tool_source': tool_source,
                        'tool_version': tool_version,
                        'data_source': data_source
                    }

                    repo_topic_object = RepoTopic(**record)
                    session.add(repo_topic_object)
                    session.commit()

                    # result = db.execute(repo_topic_table.insert().values(record))
    except Exception as e:
        logger.debug(f'error is: {e}.')
        stacker = traceback.format_exc()
        logger.debug(f"\n\n{stacker}\n\n")
        pass

    # self.register_task_completion(task, repo_id, 'clustering')


def get_tf_idf_matrix(text_list, max_df, max_features, min_df, ngram_range, logger):
    # Validate input parameters
    if not text_list:
        raise ValueError("Text list cannot be empty")
    
    if max_df <= 0 or max_df > 1.0:
        raise ValueError("max_df must be between 0 and 1")
    
    if min_df < 0:
        raise ValueError("min_df must be non-negative")
    
    # For small datasets, allow min_df to be larger than max_df if min_df is an integer
    if isinstance(min_df, float) and max_df < min_df:
        raise ValueError("max_df must be >= min_df")
    
    logger.debug("Getting the tf idf matrix from function")
    tfidf_vectorizer = TfidfVectorizer(max_df=max_df, max_features=max_features,
                                       min_df=min_df, stop_words='english',
                                       use_idf=True, tokenizer=preprocess_and_tokenize,
                                       ngram_range=ngram_range)
    tfidf_transformer = tfidf_vectorizer.fit(text_list)
    tfidf_matrix = tfidf_transformer.transform(text_list)
    pickle.dump(tfidf_transformer.vocabulary_, open("vocabulary", 'wb'))
    return tfidf_matrix, tfidf_vectorizer.get_feature_names_out()

def cluster_and_label(feature_matrix, num_clusters):
    # Validate input parameters
    if feature_matrix is None:
        raise ValueError("Feature matrix cannot be None")
    
    if num_clusters <= 0:
        raise ValueError("Number of clusters must be positive")
    
    if feature_matrix.shape[0] < num_clusters:
        raise ValueError(f"Number of samples ({feature_matrix.shape[0]}) must be >= number of clusters ({num_clusters})")
    
    kmeans_model = KMeans(n_clusters=num_clusters)
    kmeans_model.fit(feature_matrix)
    pickle.dump(kmeans_model, open("kmeans_repo_messages", 'wb'))
    return kmeans_model.labels_.tolist()

def count_func(msg):
    # Handle None or empty input
    if msg is None or not isinstance(msg, str):
        raise TypeError("Input must be a non-empty string")
    
    if not msg.strip():
        return {}
    
    blobed = TextBlob(msg)
    counts = Counter(tag for word, tag in blobed.tags if
                     tag not in ['NNPS', 'RBS', 'SYM', 'WP$', 'LS', 'POS', 'RP', 'RBR', 'JJS', 'UH', 'FW', 'PDT'])
    total = sum(counts.values())
    if total == 0:
        return {}
    normalized_count = {key: value / total for key, value in counts.items()}
    return normalized_count

def preprocess_and_tokenize(text):
    text = text.lower()
    text = re.sub(r'[@]\w+', '', text)
    text = re.sub(r'[^A-Za-z]+', ' ', text)

    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 1]
    stems = [stemmer.stem(t) for t in tokens]
    return stems



def train_model(logger, engine, max_df, min_df, max_features, ngram_range, num_clusters, num_topics, num_words_per_topic, tool_source, tool_version, data_source):
    def visualize_labels_PCA(features, labels, annotations, num_components, title):
        labels_color_map = {-1: "red"}
        for label in labels:
            labels_color_map[label] = [list([x / 255.0 for x in list(np.random.choice(range(256), size=3))])]
        low_dim_data = PCA(n_components=num_components).fit_transform(features)

        fig, ax = plt.subplots(figsize=(20, 10))

        for i, data in enumerate(low_dim_data):
            pca_comp_1, pca_comp_2 = data
            color = labels_color_map[labels[i]]
            ax.scatter(pca_comp_1, pca_comp_2, c=color, label=labels[i])
        # ax.annotate(annotations[i],(pca_comp_1, pca_comp_2))

        handles, labels = ax.get_legend_handles_labels()
        handles_label_dict = OrderedDict(zip(labels, handles))
        ax.legend(handles_label_dict.values(), handles_label_dict.keys())

        plt.title(title)
        plt.xlabel("PCA Component 1")
        plt.ylabel("PCA Component 2")
        # plt.show()
        filename = labels + "_PCA.png"
        plt.savefig(filename)

    get_messages_sql = s.sql.text(
        """
        SELECT r.repo_group_id, r.repo_id, r.repo_git, r.repo_name, i.issue_id thread_id,m.msg_text,i.issue_title thread_title,m.msg_id
        FROM augur_data.repo r, augur_data.issues i,
        augur_data.message m, augur_data.issue_message_ref imr
        WHERE r.repo_id=i.repo_id
        AND imr.issue_id=i.issue_id
        AND imr.msg_id=m.msg_id
        UNION
        SELECT r.repo_group_id, r.repo_id, r.repo_git, r.repo_name, pr.pull_request_id thread_id,m.msg_text,pr.pr_src_title thread_title,m.msg_id
        FROM augur_data.repo r, augur_data.pull_requests pr,
        augur_data.message m, augur_data.pull_request_message_ref prmr
        WHERE r.repo_id=pr.repo_id
        AND prmr.pull_request_id=pr.pull_request_id
        AND prmr.msg_id=m.msg_id
        """
    )

    with engine.connect() as conn:
        msg_df_all = pd.read_sql(get_messages_sql, conn, params={})

    # select only highly active repos
    logger.debug("Selecting highly active repos")
    msg_df_all = msg_df_all.groupby("repo_id").filter(lambda x: len(x) > 200)

    # combining all the messages in a repository to form a single doc
    logger.debug("Combining messages in repo to form single doc")
    msg_df = msg_df_all.groupby('repo_id')['msg_text'].apply(','.join)
    msg_df = msg_df.reset_index()

    # dataframe summarizing total message count in a repositoryde
    logger.debug("Summarizing total message count in a repo")
    message_desc_df = msg_df_all[["repo_id", "repo_git", "repo_name", "msg_id"]].groupby(
        ["repo_id", "repo_git", "repo_name"]).agg('count').reset_index()
    message_desc_df.columns = ["repo_id", "repo_git", "repo_name", "message_count"]
    logger.info(msg_df.head())

    tfidf_matrix, features = get_tf_idf_matrix(msg_df['msg_text'], max_df, max_features, min_df,
                                                    ngram_range, logger)
    msg_df['cluster'] = cluster_and_label(tfidf_matrix, num_clusters)

    # Count Vectorizer for NMF topic modeling
    logger.debug("Calling CountVectorizer for NMF topic modeling")
    count_vectorizer = CountVectorizer(max_df=max_df, max_features=min(max_features, 500), min_df=min_df,
                                       stop_words="english", tokenizer=preprocess_and_tokenize,
                                       ngram_range=(1, 2))
    count_transformer = count_vectorizer.fit(msg_df['msg_text'])
    count_matrix = count_transformer.transform(msg_df['msg_text'])
    pickle.dump(count_transformer.vocabulary_, open("vocabulary_count", 'wb'))
    feature_names = count_vectorizer.get_feature_names_out()

    logger.debug("Training NMF model for topic modeling")
    nmf_model = NMF(n_components=num_topics, random_state=42, max_iter=100, tol=0.01)
    nmf_model.fit(count_matrix)
    topic_list = nmf_model.components_

    logging.info(f"NMF Topic List Created: {topic_list}")
    pickle.dump(nmf_model, open("nmf_model", 'wb'))
    logging.info("pickle dump for NMF model")

    # Save topics to DB
    with get_session() as session:
        topic_id = 1
        for topic in topic_list:
            for i in topic.argsort()[:-num_words_per_topic - 1:-1]:
                record = {
                    'topic_id': int(topic_id),
                    'word': feature_names[i],
                    'tool_source': tool_source,
                    'tool_version': tool_version,
                    'data_source': data_source
                }
                topic_word_obj = TopicWord(**record)
                session.add(topic_word_obj)
                session.commit()
                logger.info(
                    "Primary key inserted into the topic_words table: {}".format(topic_word_obj.topic_words_id))
            topic_id += 1

    # Predict topic distribution for each repo
    logger.debug(f'entering prediction in model training, count_matrix is {count_matrix.shape}')
    prediction = nmf_model.transform(count_matrix)
    topic_model_dict_list = []
    logger.debug('entering for loop in model training. ')
    for i, prob_vector in enumerate(prediction):
        topic_model_dict = {}
        topic_model_dict['repo_id'] = msg_df.loc[i]['repo_id']
        for j, prob in enumerate(prob_vector):
            topic_model_dict["topic" + str(j + 1)] = prob
        topic_model_dict_list.append(topic_model_dict)
    logger.debug('creating topic model data frame.')
    topic_model_df = pd.DataFrame(topic_model_dict_list)

    result_content_df = topic_model_df.set_index('repo_id').join(message_desc_df.set_index('repo_id')).join(
        msg_df.set_index('repo_id'))
    result_content_df = result_content_df.reset_index()
    logger.info(result_content_df)

    # Save model artifacts
    model_id = str(uuid.uuid4())
    artifact_dir = os.path.join("artifacts", model_id)
    os.makedirs(artifact_dir, exist_ok=True)
    start_time = datetime.datetime.now()
    try:
        nmf_model_artifact_path = os.path.join(artifact_dir, f"nmf_model_{model_id}.pkl")
        with open(nmf_model_artifact_path, 'wb') as model_file:
            pickle.dump(nmf_model, model_file)
        vocab_artifact_path = os.path.join(artifact_dir, f"vocabulary_count_{model_id}.pkl")
        with open(vocab_artifact_path, 'wb') as vocab_file:
            pickle.dump(count_transformer.vocabulary_, vocab_file)
    except Exception as e:
        logger.warning(f"Artifact model/vocab save failed: {e}")

    # Save meta.json
    meta_json = {
        "model_id": model_id,
        "model_method": "NMF_COUNT",
        "num_topics": int(num_topics),
        "num_words_per_topic": int(num_words_per_topic),
        "training_parameters": {
            "max_df": max_df,
            "min_df": min_df,
            "max_features": max_features,
            "ngram_range": ngram_range,
            "num_clusters": num_clusters
        },
        "model_file_paths": {
            "nmf_model": nmf_model_artifact_path,
            "vocab": vocab_artifact_path
        },
        "training_start_time": str(start_time),
        "training_end_time": str(datetime.datetime.now()),
        "tool_source": tool_source,
        "tool_version": tool_version,
        "data_source": data_source
    }
    meta_path = os.path.join(artifact_dir, f"meta_{model_id}.json")
    try:
        with open(meta_path, 'w') as meta_file:
            json.dump(meta_json, meta_file, indent=2)
    except Exception as e:
        logger.warning(f"Meta JSON save failed: {e}")
    # Write topic_model_meta ORM record
    try:
        with get_session() as session:
            topic_model_meta = TopicModelMeta(
                model_id=model_id,
                model_method="NMF_COUNT",
                num_topics=int(num_topics),
                num_words_per_topic=int(num_words_per_topic),
                training_parameters=meta_json["training_parameters"],
                model_file_paths=meta_json["model_file_paths"],
                training_start_time=start_time,
                training_end_time=datetime.datetime.now(),
                tool_source=tool_source,
                tool_version=tool_version,
                data_source=data_source
            )
            session.add(topic_model_meta)
            session.commit()
    except Exception as e:
        logger.warning(f"topic_model_meta DB write failed: {e}")




