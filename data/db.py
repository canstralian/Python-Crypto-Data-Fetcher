import os
import psycopg2
from psycopg2 import sql, extras

# Fetch the DATABASE_URL from Replit secrets
DATABASE_URL = os.getenv('DATABASE_URL')

# Connect to the PostgreSQL database
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Define SQL commands to create the tables
commands = [
    """
    CREATE TABLE IF NOT EXISTS RawData (
        data_id SERIAL PRIMARY KEY,
        source VARCHAR(100) NOT NULL,
        timestamp TIMESTAMPTZ NOT NULL,
        raw_value TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS CleanedData (
        cleaned_id SERIAL PRIMARY KEY,
        data_id INTEGER NOT NULL,
        timestamp TIMESTAMPTZ NOT NULL,
        cleaned_value TEXT NOT NULL,
        FOREIGN KEY (data_id) REFERENCES RawData(data_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS FeatureExtraction (
        feature_id SERIAL PRIMARY KEY,
        cleaned_id INTEGER NOT NULL,
        feature_name VARCHAR(100) NOT NULL,
        feature_value TEXT NOT NULL,
        FOREIGN KEY (cleaned_id) REFERENCES CleanedData(cleaned_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Labels (
        label_id SERIAL PRIMARY KEY,
        feature_id INTEGER NOT NULL,
        label TEXT NOT NULL,
        FOREIGN KEY (feature_id) REFERENCES FeatureExtraction(feature_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS PreprocessedData (
        preprocess_id SERIAL PRIMARY KEY,
        feature_id INTEGER NOT NULL,
        label_id INTEGER NOT NULL,
        preprocess_timestamp TIMESTAMPTZ NOT NULL,
        FOREIGN KEY (feature_id) REFERENCES FeatureExtraction(feature_id),
        FOREIGN KEY (label_id) REFERENCES Labels(label_id)
    );
    """
]

# Execute each SQL command to create the tables
for command in commands:
    cur.execute(command)

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

print("Tables created successfully.")