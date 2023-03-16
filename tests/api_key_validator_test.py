import unittest
from unittest import mock
from unittest.mock import PropertyMock
from app.api_key_validator import ApiKeyValidator


class ApiKeyValidatorTests(unittest.TestCase):
    @mock.patch('app.configuration.Configuration.api_key', new_callable=PropertyMock)
    def test_validate_success(self, mock_api_key):
        mock_api_key.return_value = '123456'
        # Call the validate method with the correct API key
        validator = ApiKeyValidator('123456')
        self.assertTrue(validator.validate())

    @mock.patch('app.configuration.Configuration.api_key', new_callable=PropertyMock)
    def test_validate_failure(self, mock_api_key):
        mock_api_key.return_value = '123456'
        # Call the validate method with an incorrect API key
        validator = ApiKeyValidator('654321')
        self.assertFalse(validator.validate())