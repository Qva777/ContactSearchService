import unittest
from contacts_search_service import app


class TestContactSearchService(unittest.TestCase):
    """Test case for the Contact Search Service API """
    def setUp(self):
        self.app = app.test_client()

    def test_search_contacts(self):
        response = self.app.get('/search?query=Ken')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, list))
        self.assertTrue(all('first_name' in contact for contact in data))


if __name__ == '__main__':
    unittest.main()
