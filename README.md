# Knowledge Bytes

This is a simple Quiz application built with Flask and SQLAlchemy. The application allows users to create quizzes and questions, and view them via a REST API.

## Prerequisites(Refer requirements.txt)

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/knowledgebytes.git
   cd knowledgebytes
   ```

2. **Create Virtual Environment**:
    ```python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```

3. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Execute Code**:
    ```
    python3 run.py
    ```

5. **Running Tests**:
    ```
    export PYTHONPATH=$(pwd)   # On macOS/Linux
    set PYTHONPATH=%cd%        # On Windows
    ```

## Setup Instructions

### Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
export PYTHONPATH=$(pwd)
```
### Install Dependencies ###
```
pip install -r requirements.txt
```

### Run Tests ###
```
pytest -s
```

### Load the Environment (Please make sure to update the .env by referring .env-sample) ###
```
source .env
```

### Upgrade the database ###
```
flask db upgrade
```

### Run the application
```
python run.py
```

## Project Structure for reference ##

```
KNOWLEDGEBYTES
├── .venv
├── app
│   ├── static
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       └── signup.html
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── routes.py
├── gunicorn-logs
├── migrations
│   ├── versions
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── tests
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_routes.py
├── .env (Actual environment file holding all credentials)
├── .env-sample (reference)
├── .gitignore
├── gunicorn_config.py
├── manage.py
├── pytest.ini
├── README.md
├── requirements.txt
├── run.py
├── server.conf
└── wsgi.py

```

