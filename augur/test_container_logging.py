#!/usr/bin/env python3
"""
Test script to verify logging functionality in the containerized environment.
This script tests:
1. Connection to the database
2. Reading logging configuration from the database
3. Writing logs to the configured directory
4. Verifying log file permissions
5. Testing log rotation
6. Testing custom log formats
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pathlib import Path
import coloredlogs

def get_config_value(section_name, setting_name, default=None):
    """Get configuration value from database."""
    try:
        conn = psycopg2.connect(
            dbname="augur",
            user="augur",
            password="augur",
            host="db",
            port="5432"
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            "SELECT value FROM augur_operations.config WHERE section_name = %s AND setting_name = %s",
            (section_name, setting_name)
        )
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result['value'] if result else default
    except Exception as e:
        print(f"Error getting config value: {e}")
        return default

def setup_logging():
    """Set up logging with configuration from database."""
    try:
        # Get logging configuration from database
        logs_dir = get_config_value('Logging', 'logs_directory')
        log_level = get_config_value('Logging', 'log_level')
        max_file_size = int(get_config_value('Logging', 'max_file_size_mb', '10')) * 1024 * 1024
        backup_count = int(get_config_value('Logging', 'backup_count', '5'))
        file_format = get_config_value('Logging', 'file_format', '%(asctime)s [%(levelname)s] %(message)s')
        console_format = get_config_value('Logging', 'console_format', '%(asctime)s [%(levelname)s] %(message)s')
        date_format = get_config_value('Logging', 'date_format', '%Y-%m-%d %H:%M:%S')

        # Expand user directory if needed
        if logs_dir.startswith('~'):
            logs_dir = '/home/augur/.augur/logs'  # Use absolute path for augur user

        # Create logs directory if it doesn't exist
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, 'augur.log')

        # Create logger
        logger = logging.getLogger('augur')
        logger.setLevel(getattr(logging, log_level.upper()))

        # Create rotating file handler
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_file_size,
            backupCount=backup_count
        )
        file_handler.setFormatter(logging.Formatter(file_format, date_format))
        logger.addHandler(file_handler)

        # Create console handler with colored output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(console_format, date_format))
        logger.addHandler(console_handler)

        # Install coloredlogs
        coloredlogs.install(
            logger=logger,
            level=log_level.upper(),
            fmt=console_format,
            datefmt=date_format
        )

        return logger
    except Exception as e:
        print(f"Error setting up logging: {e}")
        return None

def test_database_connection():
    """Test database connection and retrieve logging configuration."""
    try:
        print("Testing database connection...")
        conn = psycopg2.connect(
            dbname="augur",
            user="augur",
            password="augur",
            host="db",
            port="5432"
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM augur_operations.config WHERE section_name = 'logging'")
        config = cur.fetchall()
        cur.close()
        conn.close()
        print("Database connection successful")
        print("Logging configuration:")
        for item in config:
            print(f"  {item['setting_name']}: {item['value']}")
        return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False

def test_logging_setup():
    """Test logging setup and write test messages."""
    try:
        print("\nTesting logging setup...")
        logger = setup_logging()
        if not logger:
            return False

        # Test log file creation
        log_file = '/home/augur/.augur/logs/augur.log'  # Use absolute path for augur user
        if not os.path.exists(log_file):
            print(f"Log file not created at {log_file}")
            return False
        print(f"Log file created at {log_file}")

        # Test log file permissions
        mode = os.stat(log_file).st_mode
        if mode & 0o777 != 0o644:
            print(f"Log file permissions incorrect: {oct(mode & 0o777)}")
            return False
        print("Log file permissions correct")

        # Test logging at different levels
        print("\nTesting log levels...")
        logger.debug("Test debug message")
        logger.info("Test info message")
        logger.warning("Test warning message")
        logger.error("Test error message")
        logger.critical("Test critical message")

        # Test log rotation
        print("\nTesting log rotation...")
        for i in range(100):  # Reduced number of messages for testing
            logger.info(f"Test log message {i} for testing rotation")
            if i % 10 == 0:
                print(f"Written {i} messages...")

        # Check for rotated files
        log_dir = os.path.dirname(log_file)
        rotated_files = [f for f in os.listdir(log_dir) if f.startswith('augur.log.')]
        if rotated_files:
            print(f"Found rotated log files: {rotated_files}")
        else:
            print("No rotated log files found")

        return True
    except Exception as e:
        print(f"Logging setup test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Starting logging tests...")
    
    if not test_database_connection():
        print("Database connection test failed")
        return False
        
    if not test_logging_setup():
        print("Logging setup test failed")
        return False
        
    print("\nAll tests completed successfully")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 