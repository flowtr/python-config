from typing import Callable, Dict, Generic, List, Literal, TypeVar, Union
import re
from typed_models.base import Field


T = TypeVar("T")


class ValidationError(Exception):
    msg: str


class Validator(Generic[T]):
    regex: List[str]
    custom: List[Callable]

    def __init__(self) -> None:
        super().__init__()
        self.regex = []
        self.custom = []

    def email(self):
        """"""
        self.regex.append(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return self

    def url(self, protocols: List[str] = ["https", "http"], credentials=False):
        """
        Validates this string as a valid url with specified protocols (defaults to: ["https", "http"]).
        """
        # TODO: implement credentials
        self.regex.append(
            rf"{'|'.join(protocols)}:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        )
        return self

    def length(self, min: float = 0, max: float = float("inf")):
        self.custom.append(lambda x: len(x) in range(min, max))
        return self

    def parse(self, value: T) -> Union[T, None]:
        if all(re.match(regex, value) is not None for regex in self.regex) and all(
            v() is True for v in self.custom
        ):
            return value
        else:
            return None

    def validate(self, value: T) -> bool:
        return all(re.match(regex, value) is not None for regex in self.regex) and all(
            v(value) is True for v in self.custom
        )

    def validateOrError(self, value: T) -> Union[Literal[True], None]:
        if not self.validate(value):
            raise ValidationError(
                {"value": value, "regex": self.regex, "custom": self.custom}
            )
        return True


F = TypeVar("F", bound=Field)


class ValidationField(Field, Generic[F]):
    parent: F
    valaidator: Validator

    def __init__(
        self,
        parent: F,
        email=False,
        url: Union[Literal[False], Dict] = False,
        length: Union[Literal[False], Dict] = False,
    ):
        super().__init__()
        self.parent = parent
        self.validator = Validator()
        if email == True:
            self.validator.email()
        if isinstance(url, dict):
            self.validator.url(**url)
        if isinstance(length, dict):
            self.validator.length(**length)

    def parse(self, value):
        self.validator.validateOrError(value)
        return super().parse(value)

    def get(_, field_value):
        return super().get(field_value)

    def set(_, field_value, value):
        return super().set(field_value, value)

    def default_serializer(_, value):
        return super().default_serializer(value)

    def get_default(_):
        return super().get_default()
