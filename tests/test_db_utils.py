import unittest
from db_utils import get_db_connection


class TestDBUtils(unittest.TestCase):
    """ Test connect yo db """
    def test_db_connection(self):
        conn = get_db_connection()
        self.assertIsNotNone(conn)
        conn.close()


if __name__ == '__main__':
    unittest.main()
