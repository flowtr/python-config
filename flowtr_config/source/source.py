from typed_models.base import Model
from typing import Type, TypeVar, Generic, Union
from abc import ABC, abstractmethod
import os
from firstclass_dotenv import Dotenv
from typed_models.serializer import DefaultSerializer
import yaml

T = TypeVar("T", bound=Model)


class ConfigSource(Generic[T], ABC):
    value: T
    model: Type[T]

    def __init__(self, model: Type[T]) -> None:
        super().__init__()
        self.model = model
        self.value = None

    @abstractmethod
    def read(self, default: T = None, path: str = ".env"):
        raise NotImplementedError()

    @abstractmethod
    def write(self, path: str = ".env"):
        raise NotImplementedError()


def read_env(path: Union[str, None], model: Type[T]):
    if path is not None:
        dotenv = Dotenv()
        dotenv.load(path)
        return model(**os.environ)
    return path


class EnvironmentConfigSource(Generic[T], ConfigSource[T]):
    def __init__(_, model: Type[T]) -> None:
        super().__init__(model)

    def read(self, default: T = None, path: str = ".env"):
        self.value = default or read_env(path, self.model)
        return self

    def write(self, path: str = ".env"):
        print("Warning: Writing environment config sources is work in progress.")
        pass


class YamlConfigSource(Generic[T], ConfigSource[T]):
    def __init__(_, model: Type[T]) -> None:
        super().__init__(model)

    def read(
        self,
        default: T = None,
        path: str = "config.yaml",
        loader: yaml.Loader = yaml.FullLoader,
    ):
        with open(path, "r") as file:
            self.value = default or self.model(**yaml.load(file.read(), Loader=loader))
            file.close()
        return self

    def write(self, path: str = "config.yaml", serializer=DefaultSerializer):
        with open(path, "w") as file:
            file.write(yaml.dump(self.value.serialize(serializer=serializer)))
            file.close()
        return self
