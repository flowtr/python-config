# flowtr-config

A typed configuration package for python 3 that can be read from various sources.

## Inspiration

This project was inspired by the package typed-config, but its autocompletion didn't work for me (specifically in VSCode).
One of the nice features about this package is the *Validator* class.

## Example

```py
from typed_models.base import Model
from typed_models.fields import StringField

from flowtr_config import Config

class User(Model):
    username = StringField()
    password = StringField(default="1234")

config = Config[User](User).read(path=".env")
print(config.get().username) # .user can autocomplete in your IDE as username

```

More documentation coming soon.

## Built With

This package was created using:

- python 3.8
- poetry
- black
- unittest
- firstclass-dotenv
- typed-models

## TODO

- Better validation errors (more context to what went wrong)
- Json5/json config source
- Toml config source
- Combine sources into a single object option
