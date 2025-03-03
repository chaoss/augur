"""
Configuration synchronization module for Augur.

This module provides functionality to synchronize configuration between
the file system (db.config.json) and the database.
"""
import os
import json
import logging
from typing import Dict, Any

from augur.application.db.session import DatabaseSession
from augur.application.db.engine import DatabaseEngine
from augur.application.config import AugurConfig

logger = logging.getLogger(__name__)

def load_config_file() -> Dict[str, Any]:
    """
    Load configuration from the db.config.json file.
    
    Returns:
        Dict containing the configuration from the file
    """
    try:
        current_dir = os.getcwd()
    except FileNotFoundError:
        logger.error("Please run augur commands in the root directory")
        return {}

    db_json_file_location = current_dir + "/db.config.json"
    
    if not os.path.exists(db_json_file_location):
        logger.error("db.config.json file not found")
        return {}
        
    with open(db_json_file_location, 'r') as f:
        db_config = json.load(f)
        
    return db_config

def save_config_file(config: Dict[str, Any]) -> bool:
    """
    Save configuration to the db.config.json file.
    
    Args:
        config: Dictionary containing the configuration to save
        
    Returns:
        True if successful, False otherwise
    """
    try:
        current_dir = os.getcwd()
    except FileNotFoundError:
        logger.error("Please run augur commands in the root directory")
        return False
        
    db_json_file_location = current_dir + "/db.config.json"
    
    try:
        with open(db_json_file_location, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        logger.error(f"Error saving config file: {str(e)}")
        return False

def update_db_from_file() -> bool:
    """
    Update database configuration from the file configuration.
    This should be called on application startup.
    
    Returns:
        True if successful, False otherwise
    """
    file_config = load_config_file()
    if not file_config:
        logger.error("Failed to load configuration from file")
        return False
    
    try:
        # We need to use the file config to connect to the database first
        db_conn_string = f"postgresql+psycopg2://{file_config['user']}:{file_config['password']}@{file_config['host']}:{file_config['port']}/{file_config['database_name']}"
        
        with DatabaseEngine() as engine:
            with DatabaseSession(logger, engine) as session:
                # Create a config object
                config = AugurConfig(logger, session)
                
                # Update database settings
                settings = [
                    {
                        "section_name": "Database",
                        "setting_name": "user",
                        "value": file_config.get('user')
                    },
                    {
                        "section_name": "Database",
                        "setting_name": "password",
                        "value": file_config.get('password')
                    },
                    {
                        "section_name": "Database",
                        "setting_name": "host",
                        "value": file_config.get('host')
                    },
                    {
                        "section_name": "Database",
                        "setting_name": "port",
                        "value": file_config.get('port')
                    },
                    {
                        "section_name": "Database",
                        "setting_name": "database_name",
                        "value": file_config.get('database_name')
                    }
                ]
                
                config.add_or_update_settings(settings)
                
        return True
    except Exception as e:
        logger.error(f"Error updating database from file: {str(e)}")
        return False

def update_file_from_db() -> bool:
    """
    Update file configuration from the database configuration.
    This should be called on application shutdown.
    
    Returns:
        True if successful, False otherwise
    """
    try:
        with DatabaseEngine() as engine:
            with DatabaseSession(logger, engine) as session:
                # Create a config object
                config = AugurConfig(logger, session)
                
                # Get database settings
                db_section = config.get_section("Database")
                
                if not db_section:
                    logger.error("Database section not found in config")
                    return False
                
                # Create config dict to save to file
                file_config = {
                    "user": db_section.get("user"),
                    "password": db_section.get("password"),
                    "host": db_section.get("host"),
                    "port": db_section.get("port"),
                    "database_name": db_section.get("database_name")
                }
                
                # Save to file
                return save_config_file(file_config)
    except Exception as e:
        logger.error(f"Error updating file from database: {str(e)}")
        return False 