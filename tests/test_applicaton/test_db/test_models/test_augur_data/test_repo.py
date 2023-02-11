
import logging
import pytest
import sqlalchemy as s

from augur.application.db.session import DatabaseSession
from augur.tasks.github.util.github_task_session import GithubTaskSession
from tests.test_applicaton.test_repo_load_controller.helper import *
from augur.application.db.models import Repo
logger = logging.getLogger(__name__)


def test_parse_github_repo_url():

    with DatabaseSession(logger) as session:

        assert Repo.parse_github_repo_url("hello world") == (None, None)
        assert Repo.parse_github_repo_url("https://github.com/chaoss/hello") == ("chaoss", "hello")
        assert Repo.parse_github_repo_url("https://github.com/hello124/augur") == ("hello124", "augur")
        assert Repo.parse_github_repo_url("https://github.com//augur") == (None, None)
        assert Repo.parse_github_repo_url("https://github.com/chaoss/") == (None, None)
        assert Repo.parse_github_repo_url("https://github.com//") == (None, None)
        assert Repo.parse_github_repo_url("https://github.com/chaoss/augur") == ("chaoss", "augur")
        assert Repo.parse_github_repo_url("https://github.com/chaoss/augur/") == ("chaoss", "augur")
        assert Repo.parse_github_repo_url("https://github.com/chaoss/augur.git") == ("chaoss", "augur")
        assert Repo.parse_github_repo_url("https://github.com/chaoss/.github") == ("chaoss", ".github")

def test_parse_github_org_url():

    with DatabaseSession(logger) as session:

        assert Repo.parse_github_org_url("hello world") == None, None
        assert Repo.parse_github_org_url("https://github.com/chaoss/") == "chaoss"
        assert Repo.parse_github_org_url("https://github.com/chaoss") == "chaoss"
        assert Repo.parse_github_org_url("https://github.com/hello124/augur") == None
        assert Repo.parse_github_org_url("https://github.com//augur") == None, None
        assert Repo.parse_github_org_url("https://github.com//") == None
        assert Repo.parse_github_org_url("https://github.com/chaoss/augur") == None


def test_is_valid_github_repo():

    with GithubTaskSession(logger) as session:

        assert Repo.is_valid_github_repo(session, "hello world")[0] is False
        assert Repo.is_valid_github_repo(session, "https://github.com/chaoss/hello")[0] is False
        assert Repo.is_valid_github_repo(session, "https://github.com/hello124/augur")[0] is False
        assert Repo.is_valid_github_repo(session, "https://github.com//augur")[0] is False
        assert Repo.is_valid_github_repo(session, "https://github.com/chaoss/")[0] is False
        assert Repo.is_valid_github_repo(session, "https://github.com//")[0] is False
        assert Repo.is_valid_github_repo(session, "https://github.com/chaoss/augur")[0] is True
        assert Repo.is_valid_github_repo(session, "https://github.com/chaoss/augur/")[0] is True
        assert Repo.is_valid_github_repo(session, "https://github.com/chaoss/augur.git")[0] is True
        assert Repo.is_valid_github_repo(session, "https://github.com/chaoss/augur/")[0] is True



def test_insert_repo(test_db_engine):

    clear_tables = ["repo", "repo_groups"]
    clear_tables_statement = get_repo_related_delete_statements(clear_tables)

    try:
        data = {"rg_id": 1, 
                "tool_source": "Frontend",
                "repo_urls": ["https://github.com/chaoss/augur", "https://github.com/chaoss/grimoirelab-sortinghat"]
                }

        with test_db_engine.connect() as connection:

            query_statements = []
            query_statements.append(clear_tables_statement)
            query_statements.append(get_repo_group_insert_statement(data["rg_id"]))
            query = s.text("".join(query_statements))

            connection.execute(query)

        with DatabaseSession(logger, test_db_engine) as session:
            
            assert Repo.insert(session, data["repo_urls"][0], data["rg_id"], data["tool_source"]) is not None
            assert Repo.insert(session, data["repo_urls"][1], data["rg_id"], data["tool_source"]) is not None

            # invalid rg_id
            assert Repo.insert(session, data["repo_urls"][0], 12, data["tool_source"]) is None

            # invalid type for repo url
            assert Repo.insert(session, 1, data["rg_id"], data["tool_source"]) is None

            # invalid type for rg_id
            assert Repo.insert(session, data["repo_urls"][1], "1", data["tool_source"]) is None

            # invalid type for tool_source
            assert Repo.insert(session, data["repo_urls"][1], data["rg_id"], 52) is None

        with test_db_engine.connect() as connection:

            result = get_repos(connection)
            assert result is not None
            assert len(result) == len(data["repo_urls"])

    finally:
        with test_db_engine.connect() as connection:
            connection.execute(clear_tables_statement)


def test_add_repo_row_with_updates(test_db_engine):

    clear_tables = ["user_repos", "user_groups", "repo", "repo_groups", "users"]
    clear_tables_statement = get_repo_related_delete_statements(clear_tables)

    try:
        data = {"old_rg_id": 1, "new_rg_id": 2, "repo_id": 1, "repo_id_2": 2, "tool_source": "Test",
                "repo_url": "https://github.com/chaoss/augur", "repo_url_2": "https://github.com/chaoss/grimoirelab-perceval-opnfv",  "repo_status": "Complete"}

        with test_db_engine.connect() as connection:

            query_statements = []
            query_statements.append(clear_tables_statement)
            query_statements.append(get_repo_group_insert_statement(data["old_rg_id"]))
            query_statements.append(get_repo_group_insert_statement(data["new_rg_id"]))
            query_statements.append(get_repo_insert_statement(data["repo_id"], data["old_rg_id"], repo_url=data["repo_url"], repo_status=data["repo_status"]))
            query = s.text("".join(query_statements))

            connection.execute(query)

        with DatabaseSession(logger, test_db_engine) as session:

            result =  Repo.insert(session, data["repo_url"], data["new_rg_id"], data["tool_source"]) is not None
            assert result == data["repo_id"]

        with test_db_engine.connect() as connection:

            result = get_repos(connection, where_string=f"WHERE repo_git='{data['repo_url']}'")
            assert result is not None
            assert len(result) == 1

            value = dict(result[0])
            assert value["repo_status"] == data["repo_status"]
            assert value["repo_group_id"] == data["new_rg_id"]

    finally:
        with test_db_engine.connect() as connection:
            connection.execute(clear_tables_statement)
