# TaskPro

Welcome to TaskPro, a basic task manager built with Python Flask!
The goal of this project was learning python and the flask package to create a cool web app.
This app manages user registration and adding and deleting tasks.

## Prerequisites

- Python 3.7 or higher
- Pip package manager

## Setting up a Virtual Environment (optional)

It's recommended to use a virtual environment to manage project dependencies.

1. Create a virtual environment:
  ```
  python -m venv my_env
  ```
2. Activate the virtual environment:
- For Windows:
  ```
  my_env\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source my_env/bin/activate
  ```

## Adding the environnement variables

1. Open .env.exemple and change the name of the variables:

```python
SECRET_KEY=your_secret_key
DB_NAME=your_database_name.db
```

2. Rename .env.exemple to .env

## Installing Dependencies

1. Install project dependencies:
  ```
  pip install -r requirements.txt
  ```

## Running the Application

1. Start the Flask development server:
  ```
  python3 main.py
  ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.



