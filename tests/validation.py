from flowtr_config.validator import ValidationError
from typed_models.base import Model
from typed_models.fields import StringField
from flowtr_config import Config, Validator, ValidationField
import unittest


class ValidationTest(unittest.TestCase):
    def test_email(self):
        self.assertEqual(Validator[str]().email().validate("theo@mail.toes.tech"), True)

    def test_url(self):
        self.assertEqual(
            Validator[str]()
            .url()
            .validate("https://joe.example.test.com/joe?key=value&username=joe"),
            True,
        )


class User(Model):
    email = ValidationField(StringField(), email=True)


class ConfigValidationTest(unittest.TestCase):
    def test_email(self):
        with self.assertRaises(ValidationError):
            config = Config[User](User).read(path="tests/tests.env")
            print(config.get().email)
            self.assertEqual(config.get().email, "theo@toes.tech")
