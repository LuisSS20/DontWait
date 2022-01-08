FROM python:3.9-slim-bullseye

LABEL maintainer="LuisSS20 <luissoriano@correo.ugr.es>"

#Creo usuario sin privilegios
RUN groupadd -r usuario && useradd -m -r -g usuario usuario
USER usuario

WORKDIR /app/

COPY pyproject.toml poetry.lock tasks.py ./

WORKDIR /app/test


ENV PATH=$PATH:/home/usuario/.local/bin

RUN pip install poetry; poetry config virtualenvs.create false; poetry install

ENTRYPOINT ["invoke", "test"]
