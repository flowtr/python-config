from flowtr_config.source.source import YamlConfigSource
from typed_models.base import Model
from typed_models.fields import StringField
from flowtr_config import Config

import unittest


class Person(Model):
    username = StringField()
    email = StringField()


class ConfigTest(unittest.TestCase):
    def test_config_env(self):
        config = Config[Person](Person).read(path="tests/tests.env")
        self.assertEqual(config.get().username, "joe")

    def test_config_yaml(self):
        yamlConfig = Config[Person](Person, sources=[YamlConfigSource(Person)]).read(
            path="tests/tests.yaml"
        )
        self.assertEqual(yamlConfig.get().email, "theo@toes.tech")
