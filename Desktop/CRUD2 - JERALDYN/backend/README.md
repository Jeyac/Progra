# Backend del sistema CRUD de alumnos

Este proyecto representa la parte del backend de un sistema CRUD para la gestión de alumnos, desarrollado con Flask como framework principal y utilizando PostgreSQL como base de datos.

En este directorio se incluyen los archivos esenciales para ejecutar el servidor backend:

- `app.py`: archivo principal de la aplicación Flask; define las rutas (endpoints) para crear, leer, actualizar y eliminar alumnos.
- `database.py`: gestiona la conexión con la base de datos PostgreSQL utilizando SQLAlchemy.
- `models.py`: contiene el modelo de datos que representa la tabla alumno en la base de datos.
- `requirements.txt`: archivo con las dependencias necesarias para instalar el entorno de Python.

El objetivo del backend es proporcionar una API REST que permita realizar las operaciones CRUD sobre los registros de alumnos, de forma sencilla y escalable.

## Requisitos previos

- Python 3.8 o superior
- PostgreSQL instalado y un usuario con permisos para crear una base de datos
- Las variables de entorno configuradas en un archivo `.env` para proteger credenciales

## Ejemplo de archivo .env

Crea un archivo llamado `.env` en el directorio raíz del backend con el siguiente contenido (ajusta los valores a tu configuración local):

```
DB_USER=postgres
DB_PASSWORD=mi_password_segura
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crud
```

## ¿Cómo correr la aplicación?

1. Instala las dependencias en un entorno virtual (opcional, pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # en Linux/Mac
venv\Scripts\activate     # en Windows
pip install -r requirements.txt
```

2. Configura el archivo `.env` con tus credenciales de PostgreSQL.

3. Levanta el servidor Flask:

```bash
python app.py
```

4. La API estará disponible en: `http://127.0.0.1:5000`

## Endpoints principales

- `GET /alumnos` – lista todos los alumnos
- `POST /alumnos` – crea un nuevo alumno
- `PUT /alumnos/<id>` – actualiza los datos de un alumno por ID
- `DELETE /alumnos/<id>` – elimina un alumno por ID

## Tecnologías utilizadas

- Python 3
- Flask
- SQLAlchemy
- PostgreSQL
- Dotenv