import unittest
from app.query_validator import validate_query

class ValidateQueryTests(unittest.TestCase):
    def test_query_with_supported_function(self):
        query = 'SELECT SUM(column) FROM table'
        supported_functions = ['SUM']
        self.assertTrue(validate_query(query, supported_functions))

    def test_query_with_unsupported_function(self):
        query = 'SELECT AVG(column) FROM table'
        supported_functions = ['SUM', 'COUNT']
        self.assertFalse(validate_query(query, supported_functions))

    def test_query_without_function(self):
        query = 'SELECT column FROM table'
        supported_functions = ['SUM', 'COUNT']
        self.assertFalse(validate_query(query, supported_functions))

    def test_invalid_query(self):
        query = 'INVALID QUERY'
        supported_functions = ['SUM', 'COUNT']
        self.assertFalse(validate_query(query, supported_functions))

if __name__ == '__main__':
    unittest.main()
