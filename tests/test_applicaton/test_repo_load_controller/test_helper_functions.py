import logging
import pytest
import sqlalchemy as s


from augur.util.repo_load_controller import RepoLoadController, DEFAULT_REPO_GROUP_IDS, CLI_USER_ID

from augur.application.db.session import DatabaseSession
from augur.tasks.github.util.github_task_session import GithubTaskSession
from tests.test_applicaton.test_repo_load_controller.helper import *

logger = logging.getLogger(__name__)



def test_is_valid_repo():

    with GithubTaskSession(logger) as session:

        controller = RepoLoadController(session)

        assert controller.is_valid_repo("hello world") is False
        assert controller.is_valid_repo("https://github.com/chaoss/hello") is False
        assert controller.is_valid_repo("https://github.com/hello124/augur") is False
        assert controller.is_valid_repo("https://github.com//augur") is False
        assert controller.is_valid_repo("https://github.com/chaoss/") is False
        assert controller.is_valid_repo("https://github.com//") is False
        assert controller.is_valid_repo("https://github.com/chaoss/augur") is True
        assert controller.is_valid_repo("https://github.com/chaoss/augur/") is True
        assert controller.is_valid_repo("https://github.com/chaoss/augur.git") is True


def test_add_repo_row(test_db_engine):

    clear_tables = ["repo", "repo_groups"]
    clear_tables_statement = get_repo_related_delete_statements(clear_tables)

    try:
        data = {"rg_id": 1, "repo_id": 1, "tool_source": "Frontend",
                "repo_url": "https://github.com/chaoss/augur"}

        with test_db_engine.connect() as connection:

            query_statements = []
            query_statements.append(clear_tables_statement)
            query_statements.append(get_repo_group_insert_statement(data["rg_id"]))
            query = s.text("".join(query_statements))

            connection.execute(query)

        with DatabaseSession(logger, test_db_engine) as session:

            assert RepoLoadController(session).add_repo_row(data["repo_url"], data["rg_id"], data["tool_source"]) is not None

        with test_db_engine.connect() as connection:

            result = get_repos(connection, where_string=f"WHERE repo_git='{data['repo_url']}'")
            assert result is not None
            assert len(result) > 0

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

            result =  RepoLoadController(session).add_repo_row(data["repo_url"], data["new_rg_id"], data["tool_source"]) is not None
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


def test_add_repo_to_user_group(test_db_engine):

    clear_tables = ["user_repos", "user_groups", "repo", "repo_groups", "users"]
    clear_tables_statement = get_repo_related_delete_statements(clear_tables)

    try:
        with test_db_engine.connect() as connection:

            data = {"repo_id": 1, "user_id": 2, "user_repo_group_id": 1, "user_group_id": 1, "user_group_name": "test_group"}

            query_statements = []
            query_statements.append(clear_tables_statement)
            query_statements.append(get_repo_group_insert_statement(data["user_repo_group_id"]))
            query_statements.append(get_repo_insert_statement(data["repo_id"], data["user_repo_group_id"]))
            query_statements.append(get_user_insert_statement(data["user_id"]))
            query_statements.append(get_user_group_insert_statement(data["user_id"], data["user_group_name"], data["user_group_id"]))
            query = s.text("".join(query_statements))

            connection.execute(query)

        with DatabaseSession(logger, test_db_engine) as session:

            RepoLoadController(session).add_repo_to_user_group(data["repo_id"], data["user_group_id"])

        with test_db_engine.connect() as connection:

            query = s.text("""SELECT * FROM "augur_operations"."user_repos" WHERE "group_id"=:user_group_id AND "repo_id"=:repo_id""")

            result = connection.execute(query, **data).fetchall()
            assert result is not None
            assert len(result) > 0

    finally:
        with test_db_engine.connect() as connection:
            connection.execute(clear_tables_statement)



def test_convert_group_name_to_id(test_db_engine):

    clear_tables = ["user_repos", "user_groups", "repo", "repo_groups", "users"]
    clear_tables_statement = get_repo_related_delete_statements(clear_tables)

    try:
        with test_db_engine.connect() as connection:

            data = {"user_id": 1, "group_name": "test_group_name", "group_id": 1}

            query_statements = []
            query_statements.append(clear_tables_statement)
            query_statements.append(get_user_insert_statement(data["user_id"]))
            query_statements.append(get_user_group_insert_statement(data["user_id"], data["group_name"], data["group_id"]))

            connection.execute("".join(query_statements))

        with GithubTaskSession(logger, test_db_engine) as session:

            controller = RepoLoadController(session)
            group_id = controller.convert_group_name_to_id(data["user_id"], data["group_name"])

            assert group_id is not None
            assert group_id == data["group_id"]

    finally:
        with test_db_engine.connect() as connection:
            connection.execute(clear_tables_statement)






