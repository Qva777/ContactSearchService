import unittest
from unittest.mock import patch, MagicMock

from tasks import update_contacts_from_nimble


class TestUpdateContactsFromNimble(unittest.TestCase):
    """Test case for the update_contacts_from_nimble function """

    @patch('tasks.get_db_connection')
    @patch('tasks.fetch_nimble_contacts')
    def test_update_contacts_from_nimble(self, mock_fetch, mock_db_conn):
        mock_fetch.return_value = [
            {'first_name': 'John', 'last_name': 'Doe', 'emails': [{'email': 'john@example.com'}]}
        ]

        mock_cursor = MagicMock()
        mock_cursor.__enter__.return_value = mock_cursor
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db_conn.return_value = mock_conn

        update_contacts_from_nimble()

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO contacts (first_name, last_name, email) "
            "VALUES (%s, %s, %s) "
            "ON CONFLICT (email) DO UPDATE SET first_name = %s, last_name = %s",
            ('John', 'Doe', 'john@example.com', 'John', 'Doe')
        )
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
