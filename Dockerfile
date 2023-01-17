FROM thomasve/fastapi-cookiecutter-base:3.9

WORKDIR src
COPY src/ .
COPY pyproject.toml ./stub.toml

EXPOSE 7070
RUN pip install uvicorn
