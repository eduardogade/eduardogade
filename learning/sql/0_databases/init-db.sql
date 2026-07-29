-- Drop if exists (for development reset)
DROP DATABASE IF EXISTS eggdb;
DROP USER IF EXISTS egguser;

-- Create fresh
CREATE USER egguser WITH PASSWORD 'eggpassword';
CREATE DATABASE eggdb OWNER egguser;

-- Connect to the new database
\c eggdb

-- Enable extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- You can even create initial tables here
CREATE TABLE IF NOT EXISTS schema_version (
    version VARCHAR(50) PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO schema_version (version) VALUES ('1.0.0');
