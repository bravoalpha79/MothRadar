# Code Institute Milestone Project 4 - Django bug tracker app

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)



## Deployment

**The deployed app can be found here: [MothRadar](https://mothradar-ba79.herokuapp.com/)**

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use `pip install` to install `dj-database-url`, `whitenoise` and `gunicorn` (psycopg2 has already been installed).
4. Run `pip freeze --local > requirements.txt` to update the requirements file.
5. From Heroku App Config Vars (Settings tab), copy the DATABASE_URL.    
In env.py, add the `DATABASE_URL`, a `DEVELOPMENT` environment variable with the value of `"1"`, and a `LOCALHOST`variable`.
6. In settings.py, import the `DEVELOPMENT` variable and set `DEBUG` dependent on the value of the `DEVELOPMENT` variable:
```python
if os.environ.get("DEVELOPMENT"):
    development = True
else:
    development = False
DEBUG = development
```
7. In settings.py, import dj_database_url.
Under `DATABASES`, comment out the Sqlite database and add the Postgres database:
```python
DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
```

8. Run `python manage.py makemigrations` and then `python manage.py migrate`.

9. In settings.py, under `DATABASES`, uncomment the Sqlite database and set the database selection (Sqlite and Postgres) depending on the `DEVELOPMENT` variable:
```python
if os.environ.get("DATABASE_URL"):
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
10. In settings.py, under `MIDDLEWARE`, add `whitenoise.middleware.WhiteNoiseMiddleware`.   
At the bottom of the file, add:
```python
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

11. In the root of the project workspace, create a Procfile (capital P!) with the following content:
`web: gunicorn mothradar.wsgi:application`
Save the file.

12. Still in the root create a folder named "static".

13. From env.py, copy the following environment variables and their values (without quotes!) into Heroku App Config Vars:
```python
SECRET_KEY
EMAIL_ADDRESS
EMAIL_PASSWORD
STRIPE_PUBLISHABLE
STRIPE_SECRET
```
Add a `DISABLE_COLLECTSTATIC` Config Var and set its value to 1.

14. In settings.py, get the `LOCALHOST` environment variable as `localhost`.   
Under `ALLOWED_HOSTS`, add `mothradar-ba79.herokuapp.com` and `localhost`.

15. In Terminal, `run python manage.py collectstatic`.

16. Commit and push all changes to GitHub master. 

17. In Heroku App DashBoard, under the Deploy tab, select GitHub as Deplyoment method. In the searchbox, type the name of the GitHub repo (MothRadar) and click "Connect".     
Under Manual deploy, make sure that the selected branch is **master**, and click Deploy Branch.

18. The app is now deployed on Heroku.


## Local development

Prerequisites:
- IDE of your choice with:    
    - installed [Python 3](https://www.python.org/downloads/) and  
    - installed [pip](https://pypi.org/project/pip/), 
- created [Gmail](https://mail.google.com/) account with two-factor authentication enabled, and
- created [Stripe](https://stripe.com/) free account. 


_Note: the Terminal commands in the following steps assume a Windows environment and a Command Prompt shell. If you are using a different operating system and/or shell, the commands will need to be adapted to your environment._

If you want to work on this project locally, follow these steps:

1. Clone or download the MothRadar GitHub repository into your local IDE.

2. To install the project's dependencies, it is recommended to create a virtual environment to prevent the dependencies from being installed globally on your system.     
To create a virtual environment for your project, in the Terminal, in the project's root directory, enter:

    `python -m venv venv`

    and then activate the created virtual environment with

    `venv\Scripts\activate`

4. Upgrade `pip` if needed:

    `python -m pip install --upgrade pip`

3. Install the project dependencies using  the following command:

    `pip install -r requirements.txt`


4. In the root directory of the project (where the `manage.py` file is located), create a file named `env.py`.

    **Remember to check immediately that the `env.py` file is listed in your `.gitignore` file to prevent your sensitive data from being commited and pushed to GitHub.**

    Inside the `env.py` file, enter the following commands and variables:

    _Note: all variable values must be **in quotes**._

   ```python
    import os

    os.environ["DEVELOPMENT"] = "1"
    os.environ["LOCALHOST"] = "127.0.0.1"

    os.environ["SECRET_KEY"] =      # your secret key
    os.environ["EMAIL_ADDRESS"] =   # your Gmail email address 
    os.environ["EMAIL_PASSWORD"] =  # your Gmail two-factor authentication app password

    os.environ["STRIPE_PUBLISHABLE"] = # your Stripe Publishable Key 
    os.environ["STRIPE_SECRET"] = # your Stripe Secret Key
   ```

    _Note: setting the_ `"DEVELOPMENT"` _variable serves to set_ `DEBUG=True` _during development. If you want_ `DEBUG=False`, _simply omit the_ `"DEVELOPMENT"` _variable definition._ 

    Save the `env.py` file.


5. In the Terminal, run 

    `python manage.py makemigrations` 

    to create the migrations for your Django database, and then

    `python manage.py migrate`

    to apply the migrations to the database.


6. In the Terminal, run

    `python manage.py createsuperuser`

    When prompted, enter a username, email, password, and repeat password, to complete superuser creation.


  **The application can now be run locally using the following command:**

`python manage.py runserver`
***

## Technologies Used

The languages, frameworks, libraries, and other tools used during this project: 

- HTML for page structure and content;
- CSS for content styling;
- JavaScript for HTML DOM manipulation, Ajax server requests and Stripe payment processing;
- Python 3 for application logic;
- [Django](https://www.djangoproject.com/) framework (v3.0.5) for application backend, development database provision (Sqlite), routing and template manipulation; 
- [Bootstrap](https://getbootstrap.com/) was used for responsive design, styling, navigation bar, buttons, alerts and modal implementation;
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to facilitate HTML rendering of Django forms;
- [jQuery](https://jquery.com/) for easier DOM manipulation and for Stripe payment;
- [Gmail](https://mail.google.com/) for sending of Password Reset messages to users;
- [Stripe](https://stripe.com/) v2 was used for credit card payment processing;
- Fonts were obtained from [Google Fonts](https://fonts.google.com/);
- Icons were obtained from [FontAwesome](https://fontawesome.com/);
- [convertio.co](https://convertio.co/) was used to convert favicon image from SVG to PNG;
- [Favicon.io](https://favicon.io/) was used for favicon creation;
- [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML and CSS code;
- [JSHint](https://jshint.com/) was used to validate JavaScript code;
- [PEP8 online](http://pep8online.com/) to validate Python code;
- [W3schools.com Color Converter](https://www.w3schools.com/colors/colors_converter.asp) was used to convert colours between default, HEX and RGB for CSS coding purposes;
- [Autoprefixer CSS online](https://autoprefixer.github.io/) was used for correct vendor prefixing of CSS styles where required;
- Google Chrome Developer Tools were used for development and testing, debugging and as a styling aid;
- [Visual Studio Code](https://code.visualstudio.com/) was used as the IDE for development and Git version control;
- [GitHub](https://github.com/) was used for source code storage;
- [WhiteNoise](http://whitenoise.evans.io/en/stable) to facilitate Django static files serving on Heroku;
- [Heroku](https://www.heroku.com/) for application online deployment and production database provision (Postgres).



## Acknowledgements

- Favicon image was obtained from [publicdomainvectors.org](https://publicdomainvectors.org/).


## Code validation:

### HTML 

Validated using [W3C Markup Validation Service](https://validator.w3.org/).
Issues found:
1. Register form -  "Element **ul** not allowed as child of element **small** in this context."
2. Password Reset Confirm form -  "Element **ul** not allowed as child of element **small** in this context."
3. Password Change form -  "Element **ul** not allowed as child of element **small** in this context."

These issues are related to the way Crispy Forms handles the respective Django forms. 

### CSS

Validated using [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/).   
No issues were found.

### JS

Validated using [JSHint](https://jshint.com/).   
No issues were found.

