# Code Institute Milestone Project 4 - Django bug tracker app

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)



## Deployment

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use pip to install dj-database-url, whitenoise and gunicorn (psycopg2 has already been installed).
4. Run pip freeze --local > requirements.txt to update the requirements file.
