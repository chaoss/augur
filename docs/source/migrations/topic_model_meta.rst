.. _topic_model_meta_migration:

====================================
Topic Model Meta Migration
====================================

What is Topic Modeling and Why is it Useful in Augur?
-----------------------------------------------------

Topic modeling is a machine learning technique that automatically groups large amounts of text—like issue comments, pull requests, or commit messages—into topics based on the words people use.

**In plain English:**  
If you have thousands of GitHub comments, topic modeling helps you see what people are talking about by automatically sorting them into categories (topics) such as "bugs", "features", or "documentation", without having to read each comment yourself.

**Why is this helpful for Augur?**
- **Automatic grouping:** Augur can organize issues, PRs, and comments into topics, making it easier to analyze trends and community focus.
- **Project health insights:** Maintainers can quickly spot which topics are most discussed, helping them identify emerging problems or popular features.
- **Data-driven analysis:** Enables advanced analytics, such as tracking how topics change over time or comparing topic trends across projects.

**How does Augur use topic modeling?**
- Augur uses algorithms like LDA and HDP to discover topics in text data.
- The results are stored in a new `topic_model_meta` table, which records which model was used, its parameters, and its results.
- This makes it possible to reproduce results, compare different models, and trace which data came from which model run.

**Example:**  
Suppose a project has 10,000 issue comments. Topic modeling might automatically group them into topics like:
- "Build errors"
- "Feature requests"
- "Documentation"
- "Performance issues"

This helps maintainers and contributors see what the community cares about most, and track how these topics change over time.

This documentation is written for both technical and non-technical contributors, so you don't need to be a machine learning expert to understand how topic modeling benefits Augur.

**Benefits for Augur:**

- **Automatic categorization:** Issues, PRs, and comments can be grouped by topic, making it easier to analyze trends and community focus.
- **Insight into project health:** By tracking which topics are most discussed, maintainers can identify emerging problems or areas of interest.
- **Data-driven analysis:** Enables advanced analytics, such as tracking how topics change over time or comparing topic distributions across projects.

**How it works in Augur:**

- Augur uses algorithms like LDA (Latent Dirichlet Allocation) and HDP (Hierarchical Dirichlet Process) to discover topics in text data.
- The new migration adds a `topic_model_meta` table to store metadata about each topic model run, making results reproducible and comparable.
- Each set of topic assignments (for words or repos) is linked to the specific model that generated them, supporting versioning and traceability.


Overview
--------

The migration creates a new `topic_model_meta` table and adds foreign key relationships to existing `repo_topic` and `topic_words` tables to track which topic model was used to generate the data.

Changes Made
------------

1. New Table: `topic_model_meta`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Creates a comprehensive table to store topic model metadata:

- `model_id` (UUID, Primary Key): Unique identifier for each topic model
- `model_method` (Text, Required): The algorithm used (e.g., "LDA", "HDP", "NMF")
- `num_topics` (Integer, Required): Number of topics in the model
- `num_words_per_topic` (Integer, Required): Number of words per topic
- `training_parameters` (JSONB, Required): Model-specific training parameters
- `model_file_paths` (JSONB, Required): Paths to saved model artifacts
- `coherence_score` (Float, Optional): Topic coherence score
- `perplexity_score` (Float, Optional): Model perplexity score
- `training_start_time` (Timestamp, Required): When training started
- `training_end_time` (Timestamp, Required): When training completed
- `tool_source` (Text, Required): Source of the tool
- `tool_version` (Text, Required): Version of the tool
- `data_source` (Text, Required): Source of the training data
- `data_collection_date` (Timestamp, Auto): When the record was created

2. Foreign Key Columns
~~~~~~~~~~~~~~~~~~~~~~
Adds `model_id` (UUID, nullable) columns to:
- `repo_topic` table
- `topic_words` table

These columns allow linking topic data to the specific model that generated it.

3. Indexes
~~~~~~~~~~
Creates indexes on the new foreign key columns for better query performance:
- `idx_repo_topic_model_id`
- `idx_topic_words_model_id`

Backward Compatibility
----------------------
- All new columns are nullable to avoid issues with existing data
- Foreign key constraints use `ON DELETE SET NULL` to handle model deletion gracefully
- Existing data will have `model_id` set to NULL until explicitly linked

Usage
-----

Creating a Topic Model Record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    from augur.application.db.models import TopicModelMeta
    import uuid
    from datetime import datetime

    model = TopicModelMeta(
        model_id=uuid.uuid4(),
        model_method="LDA",
        num_topics=10,
        num_words_per_topic=20,
        training_parameters={"alpha": 0.1, "beta": 0.01},
        model_file_paths={"model": "/path/to/model.pkl", "vocab": "/path/to/vocab.pkl"},
        coherence_score=0.85,
        perplexity_score=120.5,
        training_start_time=datetime.now(),
        training_end_time=datetime.now(),
        tool_source="topic_modeling_worker",
        tool_version="1.0",
        data_source="github_issues"
    )
    session.add(model)
    session.commit()

Linking Topic Data to Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    # When creating topic words
    topic_word = TopicWord(
        topic_id=1,
        word="python",
        word_prob=0.8,
        model_id=model.model_id,  # Link to specific model
        tool_source="test",
        tool_version="1.0",
        data_source="test"
    )

    # When creating repo topics
    repo_topic = RepoTopic(
        repo_id=1,
        topic_id=1,
        topic_prob=0.7,
        model_id=model.model_id,  # Link to specific model
        tool_source="test",
        tool_version="1.0",
        data_source="test"
    )

Querying with Model Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    # Get all topic words for a specific model
    words = session.query(TopicWord).filter_by(model_id=model_id).all()

    # Get model information for topic words
    result = session.query(TopicWord, TopicModelMeta).join(
        TopicModelMeta, TopicWord.model_id == TopicModelMeta.model_id
    ).filter_by(model_id=model_id).all()

Migration Commands
------------------

Apply Migration
~~~~~~~~~~~~~~~
.. code-block:: bash

    cd augur
    alembic upgrade head

Rollback Migration
~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    cd augur
    alembic downgrade 31

Test Migration
~~~~~~~~~~~~~~
.. code-block:: bash

    python test_migration.py

Benefits
--------

1. **Model Versioning**: Track different versions of topic models
2. **Reproducibility**: Link results to specific model configurations
3. **Performance Tracking**: Compare coherence and perplexity scores across models
4. **Data Lineage**: Understand which model generated which topic data
5. **Flexibility**: Support multiple topic modeling algorithms and parameters

Notes
-----
- The migration is designed to be safe for production use
- Existing data will continue to work without modification
- New topic modeling workflows should include model metadata
- Consider running the test script before applying to production 