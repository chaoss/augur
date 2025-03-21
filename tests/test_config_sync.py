import os
import json
import unittest
import tempfile
import shutil
from unittest.mock import patch, MagicMock

from augur.application.config_sync import (
    load_config_file,
    save_config_file,
    update_db_from_file,
    update_file_from_db
)

class TestConfigSync(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        # Create a test config file
        self.test_config = {
            "user": "test_user",
            "password": "test_password",
            "host": "localhost",
            "port": "5432",
            "database_name": "test_db"
        }
        
        with open("db.config.json", 'w') as f:
            json.dump(self.test_config, f)
    
    def tearDown(self):
        # Clean up the temporary directory
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)
    
    def test_load_config_file(self):
        # Test loading the config file
        config = load_config_file()
        self.assertEqual(config, self.test_config)
    
    def test_save_config_file(self):
        # Test saving the config file
        new_config = {
            "user": "new_user",
            "password": "new_password",
            "host": "new_host",
            "port": "5433",
            "database_name": "new_db"
        }
        
        result = save_config_file(new_config)
        self.assertTrue(result)
        
        # Verify the file was saved correctly
        with open("db.config.json", 'r') as f:
            saved_config = json.load(f)
        
        self.assertEqual(saved_config, new_config)
    
    @patch('augur.application.config_sync.DatabaseEngine')
    @patch('augur.application.config_sync.DatabaseSession')
    @patch('augur.application.config_sync.AugurConfig')
    def test_update_db_from_file(self, mock_augur_config, mock_db_session, mock_db_engine):
        # Mock the database session and config
        mock_engine_instance = MagicMock()
        mock_db_engine.return_value.__enter__.return_value = mock_engine_instance
        
        mock_session_instance = MagicMock()
        mock_db_session.return_value.__enter__.return_value = mock_session_instance
        
        mock_config_instance = MagicMock()
        mock_augur_config.return_value = mock_config_instance
        
        # Call the function
        result = update_db_from_file()
        
        # Verify the result
        self.assertTrue(result)
        
        # Verify the config was updated
        mock_config_instance.add_or_update_settings.assert_called_once()
        
        # Get the settings that were passed to add_or_update_settings
        settings = mock_config_instance.add_or_update_settings.call_args[0][0]
        
        # Verify the settings
        self.assertEqual(len(settings), 5)
        self.assertEqual(settings[0]["section_name"], "Database")
        self.assertEqual(settings[0]["setting_name"], "user")
        self.assertEqual(settings[0]["value"], "test_user")
    
    @patch('augur.application.config_sync.DatabaseEngine')
    @patch('augur.application.config_sync.DatabaseSession')
    @patch('augur.application.config_sync.AugurConfig')
    def test_update_file_from_db(self, mock_augur_config, mock_db_session, mock_db_engine):
        # Mock the database session and config
        mock_engine_instance = MagicMock()
        mock_db_engine.return_value.__enter__.return_value = mock_engine_instance
        
        mock_session_instance = MagicMock()
        mock_db_session.return_value.__enter__.return_value = mock_session_instance
        
        mock_config_instance = MagicMock()
        mock_augur_config.return_value = mock_config_instance
        
        # Mock the get_section method to return a test section
        db_section = {
            "user": "db_user",
            "password": "db_password",
            "host": "db_host",
            "port": "db_port",
            "database_name": "db_name"
        }
        mock_config_instance.get_section.return_value = db_section
        
        # Call the function
        result = update_file_from_db()
        
        # Verify the result
        self.assertTrue(result)
        
        # Verify the config was retrieved
        mock_config_instance.get_section.assert_called_once_with("Database")
        
        # Verify the file was updated
        with open("db.config.json", 'r') as f:
            saved_config = json.load(f)
        
        self.assertEqual(saved_config, db_section)

if __name__ == '__main__':
    unittest.main() 