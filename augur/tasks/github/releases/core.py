#SPDX-License-Identifier: MIT
import logging, os, sys, time, requests, json
from datetime import datetime
from multiprocessing import Process, Queue
from urllib.parse import urlparse
import pandas as pd
import sqlalchemy as s
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base
from augur.tasks.github.util.github_task_session import *
from augur.application.db.models import *
from augur.tasks.github.util.util import get_owner_repo
from augur.tasks.github.util.gh_graphql_entities import hit_api_graphql, request_graphql_dict
from augur.application.db.util import execute_session_query


def get_release_inf(repo_id, release, tag_only):
    if not tag_only:

        if release['author'] is None:
            author = 'No Author Available.'
            name = "N/A"
            company = "N/A"
        else:
            author = release["author"]

            name = author.get("name") or "nobody"
            company = author.get("company") or "nocompany"
            author = name + '_' + company


        release_inf = {
            'release_id': release['id'],
            'repo_id': repo_id,
            'release_name': release['name'],
            'release_description': release['description'],
            'release_author': author,
            'release_created_at': release['createdAt'],
            'release_published_at': release['publishedAt'],
            'release_updated_at': release['updatedAt'],
            'release_is_draft': release['isDraft'],
            'release_is_prerelease': release['isPrerelease'],
            'release_tag_name': release['tagName'],
            'release_url': release['url'],
            'tag_only': tag_only
        }
    else:
        if 'tagger' in release['target']:

            tagger = release["target"]["tagger"]

            date = tagger.get("date") or ""
            name = tagger.get("name") or "nobody"
            email = tagger.get("email") or "noemail"

            author = name + "_" + email
        else:
            author = "nobody"
            date = ""
        release_inf = {
            'release_id': release['id'],
            'repo_id': repo_id,
            'release_name': release['name'],
            'release_author': author,
            'release_tag_name': release['name'],
            'tag_only': tag_only
        }
        if date:
            release_inf['release_created_at'] = date

    return release_inf


def insert_release(augur_db, logger, repo_id, owner, release, tag_only = False):

    # Get current table values
    logger.info('Getting release table values\n')
    query = augur_db.session.query(Release.release_id).filter(Release.repo_id == repo_id)
    release_id_data = execute_session_query(query, 'all')#pd.read_sql(release_id_data_sql, self.db, params={'repo_id': repo_id})
    release_id_data = [str(r_id).strip() for r_id in release_id_data]#release_id_data.apply(lambda x: x.str.strip())

    # Put all data together in format of the table
    logger.info(f'Inserting release for repo with id:{repo_id}, owner:{owner}, release name:{release["name"]}\n')
    release_inf = get_release_inf(repo_id, release, tag_only)

    #Do an upsert
    augur_db.insert_data(release_inf,Release,['release_id'])

    logger.info(f"Inserted info for {owner}/{repo_id}/{release['name']}\n")

    return


def get_query(logger, owner, repo, tag_only):
    if not tag_only:
        query = """
            {
                repository(owner:"%s", name:"%s"){
                    id
                    releases(orderBy: {field: CREATED_AT, direction: ASC}, last: %d) {
                        edges {
                            node {
                                name
                                publishedAt
                                createdAt
                                description
                                id
                                isDraft
                                isPrerelease
                                tagName
                                url
                                updatedAt
                                author {
                                    name
                                    company
                                }
                            }
                        }
                    }
                }
            }
        """ % (owner, repo, 100)
    else:
        query = """
            {
                repository(owner:"%s", name:"%s"){
                    id
                    refs(refPrefix: "refs/tags/", last: %d){
                        edges {
                            node {
                                name
                                id
                                target {
                                    ... on Tag {
                                        tagger {
                                            name
                                            email
                                            date
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """ % (owner, repo, 100)

    logger.debug(f"query is: {query}")

    return query



def fetch_data(key_auth, logger, github_url, repo_id, tag_only = False):

    logger.info("Beginning filling the releases model for repo: " + github_url + "\n")

    owner, repo = get_owner_repo(github_url)

    url = 'https://api.github.com/graphql'

    query = get_query(logger, owner, repo, tag_only)

    # Hit the graphql endpoint
    logger.info("Hitting endpoint: {} ...\n".format(url))
    data = request_graphql_dict(key_auth,logger, url, query)

    if 'data' in data:
        data = data['data']['repository']

    data['owner'] = owner

    return data

def releases_model(augur_db, key_auth, logger, repo_git, repo_id):

    try:
        data = fetch_data(key_auth, logger, repo_git, repo_id)
    except Exception as e:
        logger.info(f"Ran into problem when fetching data for repo {repo_git}: {e}")
        return

    #logger.info("repository value is: {}\n".format(data))
    if 'releases' in data:
        if 'edges' in data['releases'] and data['releases']['edges']:
            for n in data['releases']['edges']:
                if 'node' in n:
                    release = n['node']
                    #self.insert_release(task, repo_id, data['owner'], release)
                    insert_release(augur_db, logger, repo_id, data['owner'], release)
                else:
                    logger.info("There's no release to insert. Current node is not available in releases: {}\n".format(n))
        elif 'edges' in data['releases'] and not data['releases']['edges']:
            logger.info("Searching for tags instead of releases...")
            data = fetch_data(key_auth, logger, repo_git, repo_id,True)
            logger.info("refs value is: {}\n".format(data))
            if 'refs' in data:
                if 'edges' in data['refs']:
                    for n in data['refs']['edges']:
                        if 'node' in n:
                            release = n['node']
                            #self.insert_release(task, repo_id, data['owner'], release, True)
                            insert_release(augur_db, repo_id, data['owner'], release, True)
                        else:
                            logger.info("There's no release to insert. Current node is not available in releases: {}\n".format(n))
                else:
                    logger.info("There are no releases to insert for current repository: {}\n".format(data))
            else:
                logger.info("There are no refs in data: {}\n".format(data))
        else:
            logger.info("There are no releases to insert for current repository: {}\n".format(data))
    else:
        logger.info("Graphql response does not contain repository: {}\n".format(data))