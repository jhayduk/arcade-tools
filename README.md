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

## Branching Strategy

This repository follows the Gitflow Workflow as outlined at https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow. Code is developed in feature branches and pushed to the `develop` branch when ready. When it is time to create a release, the version is updated, and the `develop` branch is tagged and pushed to the `main` branch.

## Releasing

Changes for an upcoming release are gathered in the `develop` branch. To create a release fro that, do the following:

1. Switch to `develop` branch and update local repository.
    ```commandline
    git switch dev
    git pull
    ```
2. Update CHANGELOG.md file. Commit and push.
3. Update `version` in `setup()` call in setup.py file. Commit and push.
4. Place tag and push.
    ```commandline
    git tag -a tagName -m "message"
    git push origin tagName
    ```
5. Merge `dev` branch **into** `main` branch.
    ```commandline
    git switch main
    git pull
    git merge dev
    ```
