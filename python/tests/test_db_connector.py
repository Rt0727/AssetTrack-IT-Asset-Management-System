# test_db_connector.py

import unittest
from db_connector import get_db_connection

class TestDBConnector(unittest.TestCase):

    def test_connection(self):
        connection = get_db_connection()
        self.assertIsNotNone(connection)
        connection.close()