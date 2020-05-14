# Code Institute Milestone Project 4 - Django bug tracker app

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)



## Deployment

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use pip to install dj-database-url, whitenoise and gunicorn (psycopg2 has already been installed).
4. Run pip freeze --local > requirements.txt to update the requirements file.
5. From Heroku Config Vars, copy the DATABASE_URL.    
In env.py, add the DATABASE_URL, and DEVELOPMENT environment variable with the value of "1".
6. In settings.py, import the DEVELOPMENT variable and set DEBUG to the value of the DEVELOPMENT variable:
development = os.environ.get("DEVELOPMENT")
DEBUG = development
7. In settings.py, import dj_database_url. 
Under DATABASES, set the database (Sqlite and Postgres) edpending on the DEVELOPMENT variable:
if development:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}

