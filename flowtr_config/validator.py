from typing import Generic, List, TypeVar, Union
import re

T = TypeVar("T")


class ValidationError(Exception):
    msg: str


class Validator(Generic[T]):
    regex: List[str]

    def __init__(self) -> None:
        super().__init__()
        self.regex = []

    def email(self):
        """"""
        self.regex.append(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return self

    def url(self, protocols=["https", "http"], credentials=False):
        """
        Validates this string as a valid url with specified protocols (defaults to: ["https", "http"]).
        """
        # TODO: implement credentials
        self.regex.append(
            rf"{protocols.join('|')}:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*"
        )

    def parse(self, value: T) -> Union[T, None]:
        if all(re.match(regex, value) is not None for regex in self.regex):
            return value
        else:
            raise ValidationError({"value": value, "regex": self.regex})

    def validate(self, value: T):
        return all(re.match(regex, value) is not None for regex in self.regex)
