import pytest
import psycopg2

@pytest.fixture(scope="session")
def db_connection():
    conn = psycopg2.connect(
        dbname="database_name",
        user="username",
        password="password",
        host="host",
        port="port",
    )
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()
