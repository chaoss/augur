import os
import sys
import logging
import coloredlogs
from pathlib import Path
import json

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Monkey patch SQLAlchemy to handle JSONB import
import sqlalchemy
if not hasattr(sqlalchemy, 'JSONB'):
    from sqlalchemy.dialects.postgresql import JSONB
    sqlalchemy.JSONB = JSONB

# Monkey patch models to include MetricsConfig
from augur.application.db.models.augur_operations import MetricsConfig
import augur.application.db.models
augur.application.db.models.MetricsConfig = MetricsConfig

def test_basic_logging():
    """Test basic logging functionality without database integration"""
    print("\n=== Testing Basic Logging ===")
    
    # Create a basic logger
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    
    # Set up logging directory
    log_dir = os.path.expanduser('~/.augur/test_logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Add file handler
    file_handler = logging.FileHandler(os.path.join(log_dir, 'test.log'))
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(process)d] %(name)s [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Add console handler with colored output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    coloredlogs.install(level='INFO', logger=logger)
    
    # Test logging
    logger.info('Basic logging test message')
    logger.error('Test error message')
    
    # Verify log file exists and contains content
    log_file = os.path.join(log_dir, 'test.log')
    if os.path.exists(log_file):
        print(f"\nLog file created successfully at: {log_file}")
        with open(log_file, 'r') as f:
            print("\nLog file contents:")
            print(f.read())
    else:
        print(f"\nError: Log file was not created at {log_file}")

def test_augur_logger():
    """Test AugurLogger with database integration"""
    print("\n=== Testing AugurLogger with Database Integration ===")
    
    try:
        from augur.application.logs import AugurLogger
        
        # Test with default configuration
        logger = AugurLogger('test_augur_logger')
        logger.lg.info('Test message with default config')
        
        # Test with custom log directory
        test_log_dir = os.path.expanduser('~/.augur/test_logs')
        os.environ['AUGUR_LOGS_DIR'] = test_log_dir
        logger2 = AugurLogger('test_augur_logger2')
        logger2.lg.info('Test message with custom log directory')
        
        # Test error handling for restricted directory
        try:
            os.environ['AUGUR_LOGS_DIR'] = '/root/logs'  # Should trigger fallback
            logger3 = AugurLogger('test_augur_logger3')
            logger3.lg.info('Test message with fallback directory')
        except Exception as e:
            print(f"\nExpected error handling test: {e}")
            
        print("\nAugurLogger tests completed successfully")
        
    except ModuleNotFoundError:
        print("\nError: Could not import AugurLogger. Make sure the augur package is installed.")
    except Exception as e:
        if "connection to server" in str(e):
            print("\nDatabase connection error: PostgreSQL server is not running or not accessible.")
            print("Please ensure PostgreSQL is installed and running, then try again.")
        else:
            print(f"\nError during AugurLogger testing: {e}")

def check_database_config():
    """Check if database configuration is available"""
    print("\n=== Checking Database Configuration ===")
    
    if os.getenv("AUGUR_DB"):
        print("Database configuration found in environment variable AUGUR_DB")
        return True
        
    if os.path.exists("db.config.json"):
        try:
            with open("db.config.json", 'r') as f:
                config = json.load(f)
            print("Database configuration found in db.config.json")
            return True
        except Exception as e:
            print(f"Error reading db.config.json: {e}")
            return False
    
    print("No database configuration found")
    return False

if __name__ == '__main__':
    # Always run basic logging test
    test_basic_logging()
    
    # Run AugurLogger test if database config is available
    if check_database_config():
        test_augur_logger()
    else:
        print("\nSkipping AugurLogger tests due to missing database configuration") 