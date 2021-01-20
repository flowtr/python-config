from typed_models.base import Model
from typing import Any, Type, TypeVar, Generic, Union
from abc import ABC, abstractmethod
import os
from firstclass_dotenv import Dotenv
import copy

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

    def write(self, path: str = ".env"):
        print("Warning: Writing environment config sources is work in progress.")
        pass
