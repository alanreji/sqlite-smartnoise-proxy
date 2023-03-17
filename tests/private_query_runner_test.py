import unittest
from unittest.mock import MagicMock
from app.private_query_runner import PrivateQueryRunner
from snsql.sql.private_reader import PrivateReader
from snsql.sql.odometer import OdometerHeterogeneous


class PrivateQueryRunnerTests(unittest.TestCase):
    def setUp(self):
        self.reader_mock = MagicMock(spec=PrivateReader)
        self.reader_mock.odometer = MagicMock(spec=OdometerHeterogeneous)

    def test_run_query_success(self):
        # Mock reader.execute() to return a dummy result
        self.reader_mock.execute.return_value = 42

        # Call the method and assert that it returns the expected result
        query = 'SELECT count(*) FROM employees'
        expected_result = ({'result': 42, 'total_privacy_used': self.reader_mock.odometer.spent}, 200)
        self.assertEqual(PrivateQueryRunner.run_query(query, self.reader_mock), expected_result)
        self.reader_mock.execute.assert_called_once_with(query)

    def test_run_query_error(self):
        # Mock reader.execute() to raise an exception
        self.reader_mock.execute.side_effect = Exception('Something went wrong')

        # Call the method and assert that it returns an error response
        query = 'SELECT * FROM employees'
        expected_result = ({'query error': 'Something went wrong'}, 500)
        self.assertEqual(PrivateQueryRunner.run_query(query, self.reader_mock), expected_result)
        self.reader_mock.execute.assert_called_once_with(query)
