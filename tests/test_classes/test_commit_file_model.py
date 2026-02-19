# SPDX-License-Identifier: MIT
"""Tests for the Commit and CommitFile model structure after the table split."""

import pytest
from sqlalchemy import inspect

from augur.application.db.models.augur_data import Commit, CommitFile


class TestCommitModel:
    """Verify the refactored Commit model has only commit-level columns."""

    def test_tablename(self):
        assert Commit.__tablename__ == "commits"

    def test_schema(self):
        assert Commit.__table__.schema == "augur_data"

    def test_has_commit_level_columns(self):
        column_names = {c.name for c in Commit.__table__.columns}
        expected_columns = {
            'cmt_id', 'repo_id', 'cmt_commit_hash',
            'cmt_author_name', 'cmt_author_raw_email', 'cmt_author_email',
            'cmt_author_date', 'cmt_author_affiliation',
            'cmt_committer_name', 'cmt_committer_raw_email', 'cmt_committer_email',
            'cmt_committer_date', 'cmt_committer_affiliation',
            'cmt_date_attempted',
            'cmt_ght_author_id', 'cmt_ght_committer_id', 'cmt_ght_committed_at',
            'cmt_committer_timestamp', 'cmt_author_timestamp',
            'cmt_author_platform_username',
            'tool_source', 'tool_version', 'data_source', 'data_collection_date',
        }
        assert expected_columns.issubset(column_names), \
            f"Missing columns: {expected_columns - column_names}"

    def test_no_file_level_columns(self):
        """Commit should NOT have file-level columns after the split."""
        column_names = {c.name for c in Commit.__table__.columns}
        file_columns = {'cmt_filename', 'cmt_added', 'cmt_removed', 'cmt_whitespace'}
        assert file_columns.isdisjoint(column_names), \
            f"File-level columns should not be in Commit: {file_columns & column_names}"

    def test_has_files_relationship(self):
        """Commit should have a 'files' relationship to CommitFile."""
        mapper = inspect(Commit)
        relationship_names = {r.key for r in mapper.relationships}
        assert 'files' in relationship_names

    def test_has_unique_constraint_on_repo_id_hash(self):
        """Commit should have a unique constraint on (repo_id, cmt_commit_hash)."""
        unique_constraints = [
            c for c in Commit.__table__.constraints
            if hasattr(c, 'columns') and {col.name for col in c.columns} == {'repo_id', 'cmt_commit_hash'}
        ]
        assert len(unique_constraints) > 0, \
            "Expected UniqueConstraint on (repo_id, cmt_commit_hash)"


class TestCommitFileModel:
    """Verify the new CommitFile model has the expected structure."""

    def test_tablename(self):
        assert CommitFile.__tablename__ == "commit_files"

    def test_schema(self):
        assert CommitFile.__table__.schema == "augur_data"

    def test_has_file_level_columns(self):
        column_names = {c.name for c in CommitFile.__table__.columns}
        expected_columns = {
            'commit_file_id', 'commit_id', 'repo_id',
            'cmt_filename', 'cmt_added', 'cmt_removed', 'cmt_whitespace',
            'tool_source', 'tool_version', 'data_source', 'data_collection_date',
        }
        assert expected_columns.issubset(column_names), \
            f"Missing columns: {expected_columns - column_names}"

    def test_commit_id_is_not_nullable(self):
        """commit_id FK should be NOT NULL."""
        commit_id_col = CommitFile.__table__.c.commit_id
        assert commit_id_col.nullable is False

    def test_has_commit_relationship(self):
        """CommitFile should have a 'commit' relationship to Commit."""
        mapper = inspect(CommitFile)
        relationship_names = {r.key for r in mapper.relationships}
        assert 'commit' in relationship_names

    def test_has_fk_to_commits(self):
        """CommitFile.commit_id should reference augur_data.commits.cmt_id."""
        commit_id_col = CommitFile.__table__.c.commit_id
        fk_targets = [fk.target_fullname for fk in commit_id_col.foreign_keys]
        assert 'augur_data.commits.cmt_id' in fk_targets

    def test_has_unique_constraint_on_commit_id_filename(self):
        """CommitFile should have a unique constraint on (commit_id, cmt_filename)."""
        unique_constraints = [
            c for c in CommitFile.__table__.constraints
            if hasattr(c, 'columns') and {col.name for col in c.columns} == {'commit_id', 'cmt_filename'}
        ]
        assert len(unique_constraints) > 0, \
            "Expected UniqueConstraint on (commit_id, cmt_filename)"


class TestModelImports:
    """Verify that both models can be imported from the package."""

    def test_import_commit(self):
        from augur.application.db.models import Commit
        assert Commit is not None

    def test_import_commit_file(self):
        from augur.application.db.models import CommitFile
        assert CommitFile is not None


class TestLibSplitHelpers:
    """Test the record splitting helpers used in facade_bulk_insert_commits."""

    def test_split_commit_record(self):
        from augur.application.db.lib import _split_commit_record

        record = {
            'repo_id': 1,
            'cmt_commit_hash': 'abc123',
            'cmt_author_name': 'Alice',
            'cmt_author_raw_email': 'alice@example.com',
            'cmt_author_email': 'alice@example.com',
            'cmt_author_date': '2024-01-01',
            'cmt_committer_name': 'Bob',
            'cmt_committer_raw_email': 'bob@example.com',
            'cmt_committer_email': 'bob@example.com',
            'cmt_committer_date': '2024-01-01',
            'cmt_date_attempted': '2024-01-01',
            'cmt_author_timestamp': '2024-01-01 12:00:00 +0000',
            'cmt_committer_timestamp': '2024-01-01 12:00:00 +0000',
            'cmt_filename': 'src/main.py',
            'cmt_added': 10,
            'cmt_removed': 5,
            'cmt_whitespace': 2,
            'tool_source': 'Facade',
            'tool_version': '0.80',
            'data_source': 'git',
        }

        commit_data, file_data = _split_commit_record(record)

        # Commit data should have commit-level fields
        assert commit_data['cmt_commit_hash'] == 'abc123'
        assert commit_data['repo_id'] == 1
        assert 'cmt_filename' not in commit_data
        assert 'cmt_added' not in commit_data

        # File data should have file-level fields
        assert file_data['cmt_filename'] == 'src/main.py'
        assert file_data['cmt_added'] == 10
        assert file_data['cmt_removed'] == 5
        assert file_data['cmt_whitespace'] == 2
        assert file_data['repo_id'] == 1
        assert file_data['tool_source'] == 'Facade'
        assert 'cmt_commit_hash' not in file_data

    def test_fix_invalid_timezone_valid(self):
        from augur.application.db.lib import _fix_invalid_timezone

        record = {'cmt_author_timestamp': '2024-01-01 12:00:00 +0500'}
        result = _fix_invalid_timezone(record)
        assert result is False  # +0500 is valid

    def test_fix_invalid_timezone_invalid(self):
        from augur.application.db.lib import _fix_invalid_timezone

        record = {
            'cmt_author_timestamp': '2024-01-01 12:00:00 +9999',
            'cmt_committer_timestamp': '2024-01-01 12:00:00 +9999',
        }
        result = _fix_invalid_timezone(record)
        assert result is True
        assert '+0000' in record['cmt_author_timestamp']
