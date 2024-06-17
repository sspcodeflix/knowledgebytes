import os
import sqlite3
from app import create_app, db

def create_tables_if_not_exists(database_path, sql_file_path):
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='quizzes';")
        table_exists = cursor.fetchone()
        if not table_exists:
            with open(sql_file_path, 'r') as sql_file:
                sql_script = sql_file.read()
            cursor.executescript(sql_script)
            print("Database tables created from SQL file.")

def apply_migrations():
    os.system('flask db upgrade')

if __name__ == '__main__':
    app = create_app('development')

    database_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/site.db')
    sql_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'create_tables.sql')

    # Check and create tables if they don't exist
    create_tables_if_not_exists(database_path, sql_file_path)

    # Apply migrations
    apply_migrations()

    # Run the Flask application
    app.run()
