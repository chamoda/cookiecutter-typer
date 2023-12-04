![Logo](logo.svg)

# Cookiecutter Typer

Modern cookiecutter template for python cli apps with,

* 🖥️ [Typer](https://github.com/tiangolo/typer) as main cli libarary.
* 📦 [Poetry](https://python-poetry.org/) for dependancy management.
* 🤖 [Pre-commit](https://pre-commit.com/) with [Ruff](https://github.com/astral-sh/ruff) for code formatting and [MyPy](https://mypy-lang.org) as type checker.
* 🦺 [Pytest](https://docs.pytest.org/) for unit testing.
* 🐋 [Docker](https://www.docker.com/) setup.


## Requirements

* Python 3.10 or greater.
* Pipx (install [instructions](https://pipx.pypa.io/stable/installation)).

## Installation

* Intall `cookiecutter` using `pipx install cookiecutter`.
* Install `poetry` using `pipx install poetry`.
* Run `cookiecutter https://github.com/chamoda/cookiecutter-typer.git` to create a new project from template.

## Getting started

After template created following steps gets you ups and running with the working cli app.

* Create git repo inside the template with `git init && git add . && git commit -m "Init"`
* Create a virtual enviroment with `python3 -m venv venv` and active it using `source venv/bin/activate`
* Go to newly create project directory and run `poetry install`
* Run `pre-commit install` to install git hooks.
* Run `cli-template` or equalant name you used for `app-slug` to run cli.
* Run tests with `pytest`

# Contributing

* Clone this project
* Run `cookiecutter PATH_TO_PROJECT --replay --overwrite-if-exists` rerun changes to project back into created template for testing.

