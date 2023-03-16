import os
import sqlite3
from snsql.metadata import Metadata


class DBConnector:
    __SQLITE_PATH = os.path.realpath("data/employees.db")
    __METADATA_PATH = os.path.realpath("data/metadata.yaml")

    @staticmethod
    def get_database_connection():
        """Returns the default database connection."""
        return sqlite3.connect(DBConnector.__SQLITE_PATH, check_same_thread=False)

    @staticmethod
    def get_database_metadata() -> Metadata:
        """Returns the metadata of the datasource."""
        return Metadata.from_file(DBConnector.__METADATA_PATH)