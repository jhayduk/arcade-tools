# arcade-tools

A collection of utilities and tools for a collection of arcade hobby projects.

## Usage

In Pipfile add:

```
[packages]
arcade-tools = {git = "https://github.com/jhayduk/arcade-tools.git", ref = "main", editable = true}
```

Use in code like any other package. For example:

```python
from arcade_tools.GameElement import GameElement

class Background(GameElement):
    ...
```

## Contributing

This library is meant as a personal hobby project and is not really intended to be a public library. It may be intermittently broken and there is no real maintenance implied for it.

### Install pre-commit in pipenv shell Environment

```commandline
pipenv install
pipenv shell
pip install pre-commit
pre-commit install
```
