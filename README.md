# Code Institute Milestone Project 4 - Django bug tracker app

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)



## Deployment

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use `pip install` to install `dj-database-url`, `whitenoise` and `gunicorn` (psycopg2 has already been installed).
4. Run `pip freeze --local > requirements.txt` to update the requirements file.
5. From Heroku Config Vars, copy the DATABASE_URL.    
In env.py, add the `DATABASE_URL`, and a `DEVELOPMENT` environment variable with the value of `"1"`.
6. In settings.py, import the `DEVELOPMENT` variable and set `DEBUG` to the value of the `DEVELOPMENT` variable:
```python
development = os.environ.get("DEVELOPMENT")
DEBUG = development
```
7. In settings.py, import dj_database_url.    
Under `DATABASES`, set the database (Sqlite and Postgres) depending on the `DEVELOPMENT` variable:
```python
if development:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
```

8. Run `python manage.py makemigrations` and then `python manage.py migrate`.

9. In settings.py, under `MIDDLEWARE`, add `whitenoise.middleware.WhiteNoiseMiddleware`.   
At the bottom of the file, add:
```python
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"))
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

10. In the root of the project workspace, create a Procfile (capital P!) with the following content:
`web: gunicorn mothradar.wsgi:application`
Save the file.

11. From env.py, copy the following environment variables and their values (without quotes!) into Heroku App Config Vars:
```python
SECRET_KEY
EMAIL_ADDRESS
EMAIL_PASSWORD
STRIPE_PUBLISHABLE
STRIPE_SECRET
```

12. In settings.py, under `ALLOWED_HOSTS`, add `mothradar-ba79.herokuapp.com/`.
13. Commit and push all changes to GitHub master. 

13. In Heroku App DashBoard, under the Deploy tab, select GitHub as Deplyoment method. In the searchbox, type the name of the GitHub repo (MothRadar) and click "Connect".   
Under Automatic deploys, make sure that the selected branch is **master**. Tick the checkbox "Wait for CI to pass" and click "Enable Automatic Deploys."   
Finally, undel Manual deploy, make sure that the selected branch is **master**, and click Deploy Branch.



