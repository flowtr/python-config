from typing import Generic, List, Type, TypeVar
from typed_models.base import Model
from flowtr_config.source.source import ConfigSource, EnvironmentConfigSource

T = TypeVar("T", bound=Model)


class Config(Generic[T]):
    sources: List[ConfigSource]
    value: T
    model: Type[T]

    def __init__(
        self,
        model: Type[T],
        default: T = None,
        sources=None,
    ) -> None:
        self.sources = sources or [EnvironmentConfigSource(model=model)]
        self.model = model
        self.value = default

    def read(self, source=0, **args):
        self.sources[source].read(**args)
        self.value = self.sources[source].value
        return self

    def write(self, source=0, **args):
        self.sources[source].write(**args)
        return self

    def get(self) -> T:
        return self.value
