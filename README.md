# DJANGO Study Project 1
Study project with goal of leaning about new release of DJANGO 5.2.
This project is a simple web application for sharing and discovering recipes.

## Installation
1. Clone the repository:
   ```bash
   git clone

   cd django-study-project-1
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```
7. Open your web browser and navigate to `http://localhost:8000` to view the application.

Enjoy!!! 😉

## Features


## Routines
1. Create statis production files
    ```bash
    python manage.py collectstatic
    ```
    comment: dont forget to set STATIC_ROOT in settings.py
