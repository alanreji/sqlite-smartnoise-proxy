import unittest

# Import test modules
from tests.query_validator_test import ValidateQueryTests
from tests.db_connector_test import DBConnectorTests
from tests.private_query_runner_test import PrivateQueryRunnerTests
from tests.api_key_validator_test import ApiKeyValidatorTests

# Create test suite
test_suite = unittest.TestSuite()

# Add tests from test modules to test suite
test_suite.addTest(unittest.makeSuite(ValidateQueryTests))
test_suite.addTest(unittest.makeSuite(DBConnectorTests))
test_suite.addTest(unittest.makeSuite(PrivateQueryRunnerTests))
test_suite.addTest(unittest.makeSuite(ApiKeyValidatorTests))

# Run tests
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)