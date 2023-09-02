import random

from src.db import DataLayer
from tests.conftest import TEST_ACTIVITY


def test_insert_activity(get_activity) -> None:
    db = DataLayer("tests/test.sqlite")
    db.insert_activity(TEST_ACTIVITY)

    activity = get_activity()
    assert activity[0] == tuple(TEST_ACTIVITY.values())


def test_get_activities() -> None:
    activity_data = TEST_ACTIVITY.copy()

    # Fill data with random keys
    activities = []
    for _ in range(5):
        activity_data["key"] = random.randint(10000, 20000)
        activities.append(activity_data.copy())

    # Insert data into the database
    db = DataLayer("tests/test.sqlite")
    for activity in activities:
        db.insert_activity(activity)

    data = db.get_activities()

    # Sort test data and received data in order to compare it
    activities.sort(key=lambda x: x["key"])
    data.sort(key=lambda x: x["key"])

    for i, activity in enumerate(activities):
        assert activity == data[i]
