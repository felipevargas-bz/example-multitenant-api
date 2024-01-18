# example-multitenant-api

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Descripción

`example-multitenant-api` es una aplicación de ejemplo que muestra cómo crear una API REST multitenant utilizando Flask, SQLAlchemy, Flask-JWT-Extended y Marshmallow-SQLAlchemy.

## Propósito del Proyecto

El propósito principal de este proyecto es proporcionar un ejemplo claro y funcional de cómo implementar una aplicación multitenant utilizando tecnologías populares de Python.

## Características Principales

- Serializadores eficientes con Marshmallow-SQLAlchemy.
- Autenticación y autorización basada en tokens con Flask-JWT-Extended.
- Soporte para multitenant, permitiendo la gestión de datos para múltiples inquilinos.

## Tecnologías Utilizadas

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Marshmallow-SQLAlchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)

## Cómo Instalar el Proyecto

1. Clona el repositorio:

   ```bash
   git clone https://github.com/felipevargas-bz/example-multitenant-api.git
   ```
2. Opcional: Crea un ambiente virtual:
   # Puedes usar venv
    ```bash
    python -m venv venv
    ```
    # o con virtualenv
   ```bash
    virtualenv venv
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Crea un archivo .env tomando como ejemplo el archivo .env_example.

5. Ejecuta la aplicación:
   ```bash
   python run.py
   ```
### Cómo Utilizar el Proyecto
Para utilizar el proyecto, se proporciona una colección de Postman que puedes encontrar en este enlace.

Estado del Proyecto
Actualmente, el proyecto se encuentra en fase de desarrollo.


## Autor
Felipe Vargas
