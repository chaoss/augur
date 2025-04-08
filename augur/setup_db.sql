-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS augur_operations;

-- Create config table
CREATE TABLE IF NOT EXISTS augur_operations.config (
    id SERIAL PRIMARY KEY,
    section_name VARCHAR NOT NULL,
    setting_name VARCHAR NOT NULL,
    value TEXT,
    type VARCHAR
);

-- Insert initial logging configuration
INSERT INTO augur_operations.config (section_name, setting_name, value, type)
VALUES 
    ('Logging', 'logs_directory', '~/.augur/logs', 'str'),
    ('Logging', 'log_level', 'INFO', 'str'); 