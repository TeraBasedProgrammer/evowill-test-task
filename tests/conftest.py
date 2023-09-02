import sqlite3

import pytest

TEST_ACTIVITY = {
    "key": 12345,
    "activity": "Mocked Activity",
    "type": "mock",
    "participants": 2,
    "price": 0.5,
    "link": "https://youtu.be/V5nzZWEtCnE?si=_0d3S3mVu92g0wMZ",
    "accessibility": 0.3,
}


@pytest.fixture(scope="function")
def session() -> sqlite3.Cursor:
    connection = sqlite3.connect("tests/test.sqlite")
    with connection:
        db_session = connection.cursor()
        yield db_session


@pytest.fixture(scope="function", autouse=True)
def create_table(session: sqlite3.Cursor):
    session.execute(
        """CREATE TABLE activities(id INT PRIMARY KEY, title TEXT, type VARCHAR(50), participants INT, price REAL, link TEXT NULL, accessibility REAL);"""
    )
    yield
    session.execute("""DROP TABLE activities;""")


@pytest.fixture(scope="function")
def get_activity(session: sqlite3.Cursor):
    def get_activity():
        result = session.execute("""SELECT * FROM activities;""")
        return result.fetchall()

    return get_activity
