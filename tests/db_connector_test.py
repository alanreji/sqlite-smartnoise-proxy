import unittest
from snsql.metadata import Metadata
from unittest.mock import patch, MagicMock
from app.db_connector import DBConnector


class DBConnectorTests(unittest.TestCase):
    @patch('sqlite3.connect')
    def test_get_database_connection(self, mock_connect):
        # mock the sqlite3.connect() function to return a MagicMock object
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        # call the method and check if it returns the mocked object
        conn = DBConnector.get_database_connection()
        self.assertIsInstance(conn, MagicMock)
        mock_connect.assert_called_once_with(DBConnector._DBConnector__SQLITE_PATH, check_same_thread=False)

    @patch.object(Metadata, 'from_file')
    def test_get_database_metadata(self, mock_from_file):
        mock_metadata = MagicMock(spec=Metadata)
        mock_from_file.return_value = mock_metadata

        metadata = DBConnector.get_database_metadata()
        self.assertIsNotNone(metadata)
        self.assertIsInstance(metadata, Metadata)

        mock_from_file.assert_called_once_with(DBConnector._DBConnector__METADATA_PATH)