from typed_models.base import Model
from typed_models.fields import StringField, ListField

from flowtr_config import Config, Validator
import unittest


class Person(Model):
    username = StringField()


class ConfigTest(unittest.TestCase):
    def test_config(self):
        config = Config[Person](Person).read(path="tests/tests.env")
        self.assertEqual(config.get().user, "joe")
