import pytest
import json
from flask import url_for
from augur.api.view.routes import app, db_session
from augur.application.db.models import User, ClientApplication
import secrets

class TestAPIKeyRoutes:
    
    def test_api_keys_list(self, client, app_context):
        """Test the API keys list route."""
        # Create a test user
        test_user = User(
            login_name="test_user",
            login_hashword="test_password",
            email="test@example.com"
        )
        db_session.add(test_user)
        db_session.commit()
        
        # Create a test API key
        test_app = ClientApplication(
            id=secrets.token_hex(16),
            api_key=secrets.token_hex(16),
            name="Test API Key",
            redirect_url="2023-01-01 00:00:00",
            user_id=test_user.user_id
        )
        db_session.add(test_app)
        db_session.commit()
        
        # Log in the test user
        with client.session_transaction() as session:
            session['user_id'] = test_user.user_id
        
        # Test the API keys list route
        response = client.get('/account/api-keys')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert len(data['keys']) == 1
        assert data['keys'][0]['api_key'] == test_app.api_key
        
        # Clean up
        db_session.delete(test_app)
        db_session.delete(test_user)
        db_session.commit()
    
    def test_generate_api_key(self, client, app_context):
        """Test the generate API key route."""
        # Create a test user
        test_user = User(
            login_name="test_user",
            login_hashword="test_password",
            email="test@example.com"
        )
        db_session.add(test_user)
        db_session.commit()
        
        # Log in the test user
        with client.session_transaction() as session:
            session['user_id'] = test_user.user_id
        
        # Test the generate API key route
        response = client.post('/account/generate-api-key')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert 'api_key' in data
        
        # Verify the API key was created
        api_key = data['api_key']
        app = db_session.query(ClientApplication).filter(
            ClientApplication.api_key == api_key
        ).first()
        assert app is not None
        assert app.user_id == test_user.user_id
        
        # Clean up
        db_session.delete(app)
        db_session.delete(test_user)
        db_session.commit()
    
    def test_delete_api_key(self, client, app_context):
        """Test the delete API key route."""
        # Create a test user
        test_user = User(
            login_name="test_user",
            login_hashword="test_password",
            email="test@example.com"
        )
        db_session.add(test_user)
        db_session.commit()
        
        # Create a test API key
        test_app = ClientApplication(
            id=secrets.token_hex(16),
            api_key=secrets.token_hex(16),
            name="Test API Key",
            redirect_url="2023-01-01 00:00:00",
            user_id=test_user.user_id
        )
        db_session.add(test_app)
        db_session.commit()
        
        # Log in the test user
        with client.session_transaction() as session:
            session['user_id'] = test_user.user_id
        
        # Test the delete API key route
        response = client.post('/account/delete-api-key', data={'key_id': test_app.id})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        
        # Verify the API key was deleted
        app = db_session.query(ClientApplication).filter(
            ClientApplication.id == test_app.id
        ).first()
        assert app is None
        
        # Clean up
        db_session.delete(test_user)
        db_session.commit() 