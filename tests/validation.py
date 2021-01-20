import unittest
from flowtr_config import Validator


class ValidationTest(unittest.TestCase):
    def test_email(self):
        self.assertEqual(Validator[str]().email().validate("theo@mail.toes.tech"), True)
