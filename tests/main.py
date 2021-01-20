from tests.config import ConfigTest
from tests.validation import ValidationTest
from colour_runner.runner import ColourTextTestRunner

import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ValidationTest("test_email"))
    suite.addTest(ConfigTest("test_config"))
    return suite


if __name__ == "__main__":
    runner = ColourTextTestRunner()
    runner.run(suite())
