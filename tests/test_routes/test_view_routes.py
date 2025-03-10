# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, session
from datetime import datetime

from augur.api.view.routes import (
    repo_table_view, repo_card_view, user_groups_view, dashboard_view,
    api_keys_list, generate_api_key, delete_api_key
)
from augur.api.view.api import (
    list_worker_oauth_keys, add_worker_oauth_key, delete_worker_oauth_key
)

class TestViewRoutes(unittest.TestCase):
    """
    Tests for the view routes in the Augur application.
    These tests focus on the routes that were modified in the PR.
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
    def test_placeholder_functions(self):
        """Test that placeholder functions return expected values"""
        self.assertEqual(get_all_repos(), [])
        self.assertEqual(get_all_repos_count(), 0)
        
        # Test with parameters
        self.assertEqual(get_all_repos(None, "group1"), [])
        self.assertEqual(get_all_repos_count(None, "group1"), 0)
    
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.get_all_repos')
    @patch('augur.api.view.routes.get_all_repos_count')
    @patch('augur.api.view.routes.render_module')
    def test_repo_table_view_unauthenticated(self, mock_render, mock_count, mock_repos, mock_user):
        """Test repo_table_view for unauthenticated users"""
        # Setup mocks
        mock_user.is_authenticated = False
        mock_repos.return_value = ([{"repo_id": 1}], None)
        mock_count.return_value = (10, None)
        mock_render.return_value = "rendered table"
        
        # Call the function
        with self.app.test_request_context('/?q=test&p=1&s=name&r=True'):
            result = repo_table_view()
            
        # Verify the correct functions were called
        mock_repos.assert_called_once()
        mock_count.assert_called_once()
        mock_render.assert_called_once()
        
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.render_module')
    def test_repo_table_view_authenticated(self, mock_render, mock_user):
        """Test repo_table_view for authenticated users"""
        # Setup mocks
        mock_user.is_authenticated = True
        mock_user.get_repos.return_value = ([{"repo_id": 1}], None)
        mock_user.get_repo_count.return_value = (10, None)
        mock_render.return_value = "rendered table"
        
        # Call the function
        with self.app.test_request_context('/?q=test&p=1&s=name&r=True'):
            result = repo_table_view()
            
        # Verify the correct functions were called
        mock_user.get_repos.assert_called_once()
        mock_user.get_repo_count.assert_called_once()
        mock_render.assert_called_once()
    
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.get_all_repos')
    @patch('augur.api.view.routes.get_all_repos_count')
    @patch('augur.api.view.routes.renderRepos')
    def test_repo_card_view_unauthenticated(self, mock_render, mock_count, mock_repos, mock_user):
        """Test repo_card_view for unauthenticated users"""
        # Setup mocks
        mock_user.is_authenticated = False
        mock_repos.return_value = ([{"repo_id": 1}], None)
        mock_count.return_value = (10, None)
        mock_render.return_value = "rendered cards"
        
        # Call the function
        with self.app.test_request_context('/?q=test'):
            result = repo_card_view()
            
        # Verify the correct functions were called
        mock_repos.assert_called_once()
        mock_count.assert_called_once()
        mock_render.assert_called_once()
        
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.renderRepos')
    def test_repo_card_view_authenticated(self, mock_render, mock_user):
        """Test repo_card_view for authenticated users"""
        # Setup mocks
        mock_user.is_authenticated = True
        mock_user.get_repos.return_value = ([{"repo_id": 1}], None)
        mock_user.get_repo_count.return_value = (10, None)
        mock_render.return_value = "rendered cards"
        
        # Call the function
        with self.app.test_request_context('/?q=test'):
            result = repo_card_view()
            
        # Verify the correct functions were called
        mock_user.get_repos.assert_called_once()
        mock_user.get_repo_count.assert_called_once()
        mock_render.assert_called_once()
        
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.render_module')
    def test_user_groups_view(self, mock_render, mock_user):
        """Test user_groups_view handles groups correctly"""
        # Setup mocks
        mock_user.get_groups_info.return_value = (
            [{"name": "group1", "repos": [1, 2]}, {"name": "group2", "repos": [3, 4]}],
            "success"
        )
        mock_render.return_value = "rendered groups"
        
        # Call the function
        with self.app.test_request_context('/user/groups/?q=test&s=name&r=True&p=0'):
            result = user_groups_view()
            
        # Verify the correct functions were called
        mock_user.get_groups_info.assert_called_once()
        mock_render.assert_called_once()
        
    @patch('augur.api.view.routes.db_session')
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.jsonify')
    def test_api_keys_list(self, mock_jsonify, mock_user, mock_db):
        """Test api_keys_list returns the correct data"""
        # Setup mocks
        mock_app1 = MagicMock()
        mock_app1.id = "id1"
        mock_app1.api_key = "key1"
        mock_app1.name = "name1"
        mock_app1.redirect_url = "2023-01-01"
        
        mock_db.query.return_value.filter.return_value.all.return_value = [mock_app1]
        mock_user.user_id = 1
        mock_jsonify.return_value = {"success": True, "keys": [{"id": "id1"}]}
        
        # Call the function
        result = api_keys_list()
        
        # Verify the correct functions were called
        mock_db.query.assert_called_once()
        mock_jsonify.assert_called_once()
        
    @patch('augur.api.view.routes.secrets')
    @patch('augur.api.view.routes.datetime')
    @patch('augur.api.view.routes.db_session')
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.jsonify')
    @patch('augur.api.view.routes.ClientApplication')
    def test_generate_api_key(self, mock_app, mock_jsonify, mock_user, mock_db, mock_dt, mock_secrets):
        """Test generate_api_key creates a new API key"""
        # Setup mocks
        mock_secrets.token_hex.return_value = "random_token"
        mock_dt.now.return_value = datetime(2023, 1, 1)
        mock_user.user_id = 1
        mock_jsonify.return_value = {"success": True, "api_key": "random_token"}
        
        # Call the function
        with self.app.test_request_context('/account/generate-api-key', method='POST'):
            result = generate_api_key()
        
        # Verify the correct functions were called
        mock_secrets.token_hex.assert_called()
        mock_app.assert_called_once()
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_jsonify.assert_called_once()
        
    @patch('augur.api.view.routes.request')
    @patch('augur.api.view.routes.db_session')
    @patch('augur.api.view.routes.current_user')
    @patch('augur.api.view.routes.jsonify')
    def test_delete_api_key(self, mock_jsonify, mock_user, mock_db, mock_request):
        """Test delete_api_key removes an API key"""
        # Setup mocks
        mock_app = MagicMock()
        mock_db.query.return_value.filter.return_value.first.return_value = mock_app
        mock_user.user_id = 1
        mock_request.form.get.return_value = "key_id_123"
        mock_jsonify.return_value = {"success": True}
        
        # Call the function
        with self.app.test_request_context('/account/delete-api-key', method='POST'):
            result = delete_api_key()
        
        # Verify the correct functions were called
        mock_request.form.get.assert_called_once_with('key_id')
        mock_db.query.assert_called_once()
        mock_db.delete.assert_called_once_with(mock_app)
        mock_db.commit.assert_called_once()
        mock_jsonify.assert_called_once()
        
    @patch('augur.api.view.routes.requestJson')
    @patch('augur.api.view.routes.render_template')
    def test_dashboard_view(self, mock_render, mock_request_json):
        """Test dashboard_view returns the correct template with data"""
        # Setup mocks
        mock_request_json.return_value = {"config": "data"}
        mock_render.return_value = "rendered dashboard"
        
        # Call the function
        result = dashboard_view()
        
        # Verify the correct functions were called
        mock_request_json.assert_called_once_with("config/get", False)
        mock_render.assert_called_once()
        args, kwargs = mock_render.call_args
        self.assertEqual(args[0], 'admin-dashboard.j2')
        self.assertIn('sections', kwargs)
        self.assertIn('config', kwargs)

    @patch('augur.api.view.api.DatabaseSession')
    @patch('augur.api.view.api.jsonify')
    def test_list_worker_oauth_keys(self, mock_jsonify, mock_db_session):
        """Test list_worker_oauth_keys returns the correct data."""
        # Setup mocks
        mock_key = MagicMock()
        mock_key.oauth_id = 1
        mock_key.name = "Test GitHub Key"
        mock_key.platform = "github"
        mock_key.access_token = "test_token"
        
        mock_session = MagicMock()
        mock_db_session.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.all.return_value = [mock_key]
        mock_jsonify.return_value = {"success": True, "keys": [{"id": 1}]}
        
        # Call the function
        result = list_worker_oauth_keys()
        
        # Verify the correct functions were called
        mock_session.query.assert_called_once()
        mock_jsonify.assert_called_once()
        
    @patch('augur.api.view.api.request')
    @patch('augur.api.view.api.DatabaseSession')
    @patch('augur.api.view.api.jsonify')
    @patch('augur.api.view.api.WorkerOauth')
    def test_add_worker_oauth_key(self, mock_worker_oauth, mock_jsonify, 
                                  mock_db_session, mock_request):
        """Test add_worker_oauth_key creates a new worker OAuth key."""
        # Setup mocks
        mock_key = MagicMock()
        mock_key.oauth_id = 1
        mock_worker_oauth.return_value = mock_key
        mock_request.form.get.side_effect = lambda key, default=None: {
            'platform': 'github',
            'name': 'Test Key',
            'access_token': 'test_token'
        }.get(key, default)
        mock_jsonify.return_value = {"success": True, "key_id": 1}
        
        mock_session = MagicMock()
        mock_db_session.return_value.__enter__.return_value = mock_session
        
        # Call the function
        with self.app.test_request_context('/admin/worker-oauth-keys', method='POST'):
            result = add_worker_oauth_key()
        
        # Verify the correct functions were called
        mock_worker_oauth.assert_called_once()
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_jsonify.assert_called_once()
        
    @patch('augur.api.view.api.DatabaseSession')
    @patch('augur.api.view.api.jsonify')
    def test_delete_worker_oauth_key(self, mock_jsonify, mock_db_session):
        """Test delete_worker_oauth_key removes a worker OAuth key."""
        # Setup mocks
        mock_key = MagicMock()
        mock_session = MagicMock()
        mock_db_session.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.filter.return_value.first.return_value = mock_key
        mock_jsonify.return_value = {"success": True}
        
        # Call the function
        result = delete_worker_oauth_key(1)
        
        # Verify the correct functions were called
        mock_session.query.assert_called_once()
        mock_session.delete.assert_called_once_with(mock_key)
        mock_session.commit.assert_called_once()
        mock_jsonify.assert_called_once()

if __name__ == '__main__':
    unittest.main()
