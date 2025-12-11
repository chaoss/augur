# SPDX-License-Identifier: MIT
import pytest
from unittest.mock import Mock, patch, MagicMock
from augur.tasks.init import get_redis_conn_values, get_rabbitmq_conn_string


class TestInitFunctions:
    """Test suite for functions in augur.tasks.init module to ensure proper database connection handling."""

    @patch('augur.tasks.init.DatabaseEngine')
    @patch('augur.tasks.init.DatabaseSession')
    @patch('augur.tasks.init.AugurConfig')
    def test_get_redis_conn_values_closes_connections(self, mock_config_class, mock_session_class, mock_engine_class):
        """Test that get_redis_conn_values properly closes database connections."""
        # Setup mocks
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_config = MagicMock()
        
        mock_engine_class.return_value.__enter__ = Mock(return_value=mock_engine)
        mock_engine_class.return_value.__exit__ = Mock(return_value=None)
        
        mock_session_class.return_value.__enter__ = Mock(return_value=mock_session)
        mock_session_class.return_value.__exit__ = Mock(return_value=None)
        
        mock_config_class.return_value = mock_config
        mock_config.get_value.side_effect = lambda section, key: {
            ("Redis", "cache_group"): 1,
            ("Redis", "connection_string"): "redis://localhost:6379/"
        }[(section, key)]
        
        # Call the function
        db_number, conn_string = get_redis_conn_values()
        
        # Verify the context managers were entered and exited properly
        mock_engine_class.return_value.__enter__.assert_called_once()
        mock_engine_class.return_value.__exit__.assert_called_once()
        mock_session_class.return_value.__enter__.assert_called_once()
        mock_session_class.return_value.__exit__.assert_called_once()
        
        # Verify the returned values are correct
        assert db_number == 3  # 1 * 3
        assert conn_string == "redis://localhost:6379/"

    @patch('augur.tasks.init.DatabaseEngine')
    @patch('augur.tasks.init.DatabaseSession')
    @patch('augur.tasks.init.AugurConfig')
    def test_get_redis_conn_values_adds_trailing_slash(self, mock_config_class, mock_session_class, mock_engine_class):
        """Test that get_redis_conn_values adds trailing slash to connection string if missing."""
        # Setup mocks
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_config = MagicMock()
        
        mock_engine_class.return_value.__enter__ = Mock(return_value=mock_engine)
        mock_engine_class.return_value.__exit__ = Mock(return_value=None)
        
        mock_session_class.return_value.__enter__ = Mock(return_value=mock_session)
        mock_session_class.return_value.__exit__ = Mock(return_value=None)
        
        mock_config_class.return_value = mock_config
        mock_config.get_value.side_effect = lambda section, key: {
            ("Redis", "cache_group"): 2,
            ("Redis", "connection_string"): "redis://localhost:6379"  # No trailing slash
        }[(section, key)]
        
        # Call the function
        db_number, conn_string = get_redis_conn_values()
        
        # Verify trailing slash is added
        assert conn_string == "redis://localhost:6379/"
        assert db_number == 6  # 2 * 3

    @patch('augur.tasks.init.DatabaseEngine')
    @patch('augur.tasks.init.DatabaseSession')
    @patch('augur.tasks.init.AugurConfig')
    def test_get_rabbitmq_conn_string_closes_connections(self, mock_config_class, mock_session_class, mock_engine_class):
        """Test that get_rabbitmq_conn_string properly closes database connections."""
        # Setup mocks
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_config = MagicMock()
        
        mock_engine_class.return_value.__enter__ = Mock(return_value=mock_engine)
        mock_engine_class.return_value.__exit__ = Mock(return_value=None)
        
        mock_session_class.return_value.__enter__ = Mock(return_value=mock_session)
        mock_session_class.return_value.__exit__ = Mock(return_value=None)
        
        mock_config_class.return_value = mock_config
        expected_conn_string = "amqp://user:pass@localhost:5672/"
        mock_config.get_value.return_value = expected_conn_string
        
        # Call the function
        conn_string = get_rabbitmq_conn_string()
        
        # Verify the context managers were entered and exited properly
        mock_engine_class.return_value.__enter__.assert_called_once()
        mock_engine_class.return_value.__exit__.assert_called_once()
        mock_session_class.return_value.__enter__.assert_called_once()
        mock_session_class.return_value.__exit__.assert_called_once()
        
        # Verify the config was accessed with correct parameters
        mock_config.get_value.assert_called_once_with("RabbitMQ", "connection_string")
        
        # Verify the returned value is correct
        assert conn_string == expected_conn_string

    @patch('augur.tasks.init.DatabaseEngine')
    @patch('augur.tasks.init.DatabaseSession')
    @patch('augur.tasks.init.AugurConfig')
    def test_get_redis_conn_values_config_accessed_before_exit(self, mock_config_class, mock_session_class, mock_engine_class):
        """Test that config values are accessed inside the context manager (before __exit__ is called)."""
        # Track the order of calls
        call_order = []
        
        mock_engine = MagicMock()
        mock_session = MagicMock()
        mock_config = MagicMock()
        
        # Track when __exit__ is called
        def track_engine_exit(*args):
            call_order.append('engine_exit')
            return None
        
        def track_session_exit(*args):
            call_order.append('session_exit')
            return None
        
        # Track when get_value is called
        def track_get_value(section, key):
            call_order.append(f'get_value_{section}_{key}')
            if section == "Redis" and key == "cache_group":
                return 1
            elif section == "Redis" and key == "connection_string":
                return "redis://localhost:6379/"
            return None
        
        mock_engine_class.return_value.__enter__ = Mock(return_value=mock_engine)
        mock_engine_class.return_value.__exit__ = Mock(side_effect=track_engine_exit)
        
        mock_session_class.return_value.__enter__ = Mock(return_value=mock_session)
        mock_session_class.return_value.__exit__ = Mock(side_effect=track_session_exit)
        
        mock_config_class.return_value = mock_config
        mock_config.get_value = Mock(side_effect=track_get_value)
        
        # Call the function
        get_redis_conn_values()
        
        # Verify that get_value calls happened before the exit calls
        # This ensures the config is accessed while the connections are still open
        cache_group_index = call_order.index('get_value_Redis_cache_group')
        connection_string_index = call_order.index('get_value_Redis_connection_string')
        session_exit_index = call_order.index('session_exit')
        engine_exit_index = call_order.index('engine_exit')
        
        assert cache_group_index < session_exit_index, "Config access should happen before session exit"
        assert connection_string_index < session_exit_index, "Config access should happen before session exit"
        assert cache_group_index < engine_exit_index, "Config access should happen before engine exit"
        assert connection_string_index < engine_exit_index, "Config access should happen before engine exit"
