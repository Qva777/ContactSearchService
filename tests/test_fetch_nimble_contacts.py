import unittest
from unittest.mock import Mock, patch
from fetch_nimble_contacts import fetch_nimble_contacts


class TestFetchNimbleContacts(unittest.TestCase):
    """Test case for the fetch_nimble_contacts function """

    @patch('requests.get')
    def test_fetch_nimble_contacts(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'first_name': 'John', 'last_name': 'Doe'}]

        mock_get.return_value = mock_response

        contacts_data = fetch_nimble_contacts()

        self.assertEqual(len(contacts_data), 1)
        self.assertEqual(contacts_data[0]['first_name'], 'John')
        self.assertEqual(contacts_data[0]['last_name'], 'Doe')


if __name__ == '__main__':
    unittest.main()
