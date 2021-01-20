from tests.config import ConfigTest
from tests.validation import ConfigValidationTest, ValidationTest
from colour_runner.runner import ColourTextTestRunner

import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ValidationTest("test_email"))
    suite.addTest(ValidationTest("test_url"))
    suite.addTest(ConfigValidationTest("test_email"))
    suite.addTest(ConfigTest("test_config_env"))
    suite.addTest(ConfigTest("test_config_yaml"))
    return suite


if __name__ == "__main__":
    runner = ColourTextTestRunner()
    runner.run(suite())
