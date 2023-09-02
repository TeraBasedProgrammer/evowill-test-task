from unittest.mock import patch

from src.wrapper import Wrapper
from tests.conftest import TEST_ACTIVITY


def test_get_random_activity():
    with patch("src.wrapper.requests.get") as mock_get:
        mock_get.return_value.json.return_value = TEST_ACTIVITY

        wrapper = Wrapper()
        with patch.object(wrapper, "db") as mock_db, patch.object(
            wrapper, "prettify_data"
        ) as mock_prettify_data:
            wrapper.get_random_activity(
                type="test_type",
                participants=3,
                minprice=0.1,
                maxprice=0.8,
                minaccessibility=0.2,
                maxaccessibility=0.7,
            )

            # Assert that the mock_response data is inserted and prettified
            mock_db.insert_activity.assert_called_once_with(TEST_ACTIVITY)
            mock_prettify_data.assert_called_once_with([TEST_ACTIVITY])
