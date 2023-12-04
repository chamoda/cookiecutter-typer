FROM python:3.10-slim

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /project

COPY requirements.txt /project/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY pyproject.toml /project/pyproject.toml
COPY README.md /project/README.md
COPY {{cookiecutter.app_slug }} /project/{{cookiecutter.app_slug }}

RUN pip install -e .

ENTRYPOINT ["{{ cookiecutter.project_slug }}"]

