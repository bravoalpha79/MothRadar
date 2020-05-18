# MothRadar

[![Build Status](https://travis-ci.org/bravoalpha79/MothRadar.svg?branch=master)](https://travis-ci.org/bravoalpha79/MothRadar)


MothRadar is a ticket tracker app for a fictional application called UnicornAttractor. MothRadar enables the users of the UnicornAttractor to raise tickets on issues encountered during the app use, to browse through existing tickets, and to comment on them. It also provides the users with the ability to upvote existing tickets, thus helping the UnicornAttractor app owner to prioritise fixes among existing bugs.

_"MothRadar never loses track of any bug that enters its scope."_

## UX

MothRadar is intended primarily for the users of the UnicornAttractor app. It also aims to facilitate the owner's maintenance work on the app by providing user feedback in the form of tickets, comments and upvotes.

Visitors (unregistered users and users not logged-in) have only the option to browse, search and filter existing tickets and view individual ticket details (read-only access).

Registered and logged-in users have access to the full set of features of the MothRadar app: new ticket creation, commenting on existing tickets, and upvoting tickets. 

Tickets can be raised as one of two types: **Bug** (for UnicornAttractor app issues) or **Feature** (for suggestions on app improvement). The structure and handling of either ticket type in MothRadar is identical, with the exception of the Upvote feature which is free for Bug tickets but requires payment for Feature tickets.   

### User Stories

Based on the above general requirements, the following user stories have been identified:

As a user:
1. I want to be provided with some general information on the MothRadar app's available features and how to use them.
2. I want to be able to create a new ticket.
3. I want to be able to edit/amend a ticket that I have created.
4. I want to be able to browse existing tickets.
5. I want to be able to search existing tickets by keyword(s) to narrow my browsing scope.
6. I want to be able to view the most upvoted tickets.
7. I want to be able to filter my tickets only.
8. I want to be able to filter by Bugs only or Features only.
9. I want to be able to view all details of a selected ticket, including date created, author, upvotes count, and existing comments on the ticket.
10. I want to be able to comment on an existing ticket in order to provide more details if I have them.
11. I want to be able to edit my comment(s).
12. I want to be able to delete my comment(s).
13. I want to be able to upvote a ticket I find relevant for me, so I can get it fixed sooner.
14. I want to be able to view my account details.
15. I want to be able to edit my account details.
16. I want to be able to change my password.
17. I want to be able to log out so I can protect my account when I am finished working with the app.
18. I want to be able to reset my password via email if I forget it.

As app owner:   
1. (19) I want to have a user login functionality.    
2. (20) I want only logged-in users to be able to make changes to the existing ticket data (ticket details, comments and upvotes).
3. (21) I want a logged-in user to be able to edit ticket details only for tickets they have created, and only if the ticket is still in its initial status.
4. (22) I want not logged-in users to be able to browse-only the site.
5. (23) I want to provide a visitor with the option to register and create a user account.
6. (24) I want to have a payment process for logged-in users upvoting Feature tickets.




### UI structure

#### Essential elements

_Due to time constraints, it has been decided that, with regards to comments, in this version of the app only creation of comments will be enabled. Editing and deleting of existing comments (by their creator only) - **user stories 11 and 12 - will need to be implemented in a future version.**_ 

The following UI elements are essential for the implementation of the user stories:

- navigation bar/menu,
- landing page,
- ticket creation form,
- ticket search form,
- ticket filters/views:
    - most upvoted,
    - created by user,
    - Bugs only,
    - Features only,
- new comment form,
- upvote button and counter,
- logout button,
- user login form,
- user registration form,
- payment form.

The full stack of the app is built using the [Django](https://www.djangoproject.com/) framework.

Most of the needed forms are obtained either directly from Django default forms (User) or by defining Model forms (Ticket and Upvote) and rely on Django form validation. [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) are used for rendering of all Django-based forms.

The two exceptions to this are: 
- the Ticket Search form, which uses a GET method and therefore does not require validation, and 
- the comments "form", which uses JavaScript processing (including an Ajax call to backend) and is therefore not defined as an HTML form element but just as an HTML text area with a button to trigger the JavaScript script.


#### Visual layout

[Bootstrap](https://getbootstrap.com/) styling has been used as much as possible to assure full responsivity of the site. 

A top-fixed Bootstrap navbar with the essential links is present at all times. At screen sizes below 992px this is reduced to just the Logo and the "burger icon" which opens a "sidenav" with the links.
On screen sizes below 992px all content is displayed in single-column layout (screen-wide), while on large screens (992px and above) it is dependent on the actual page displayed.
Four [wireframe.cc](https://wireframe.cc/) wireframes (for desktop-size display) were produced during the prototyping phase of the project:

- [Home/Landing page](https://wireframe.cc/eGJAA4)
- [All Tickets view](https://wireframe.cc/3aDo54)
- [Ticket detail view](https://wireframe.cc/WFyuKF)
- [New ticket form](https://wireframe.cc/1KlXoR)

The only major departures from the initial design is in that the sidebar has been placed to the left of the main content (as opposed to the right in the wireframes) and that it has been removed on detail views as not needed.   
Also, the "by status" filter has been replaced by a "my tickets" filter.

#### Font and colour scheme

The "Open Sans" font from [Google Fonts](https://fonts.google.com/) was chosen for its professional appearance and readability. 

The colour scheme was chosen to mimic the "dark mode" settings of Windows, IDEs, Stack Overflow, Slack etc.    
Thus the basic background colour is a very dark (near-black) grey (#222121) with lighter or darker grey elements on top of it, whereas the main font colour is a very light grey (#b9b7b7) - pure white and off-white have not been used in order to avoid too strong a contrast.  
The only elements departing from this general scheme are buttons and badges (styled with Bootstrap default colour classes), alerts (default Bootstrap colour classes with occasional custom adjustments), links/anchors (default blue colour) and ticket type and status tags (custom colours). These details were chosen in order to add clear highlight to elements that point to a certain functionality, or to subtly highlight specific ticket data.


## Features

### Existing features

#### Navbar
The navbar is implemented as a Bootstrap top-fixed navbar with responsive layout (breakpoint 992px). The contents (links) in the navbar change dynamically depending on whether the user is logged in or not.

#### Landing page
The landing page is designed in the form of interactive cards which, when clicked, expand to reveal the details of certain features of the application.

#### Ticket list view
The default ticket list view displays the list of all tickets in the database sorted by date and time created (newest first).

#### Ticket list view filters/sorting
Four sort/filter options are available to all users: sort by most recent (default view), sort by most upvoted, filter Bug tickets only, and filter Feature tickets only.    
For logged-in users, a third filter is available to display only the tickets created by that user, the total number of those tickets being indicated in the sidebar.

The current selected view/filter is clearly indicated by the UI by colour-highlighting the corresponding view's link/button in the sidebar.

Pagination (5 tickets per page) is implemented in all list views.

#### Ticket list search
The search function is implemented as a simple search box with a button to trigger the search. 
The search is performed on top of any current view filters, so if e.g. the user has selected the "Features only" filter, the search will be performed among Feature tickets only.    

_Note: the current search functionality uses a simple `__icontains` on the Ticket model's `description` field. The plan is to implement a more complex search algorithm, and include both the `title` and the `description` fields, in a future version of the app._  

#### Ticket detail view
The ticket detail view provides any user with all details of the ticket (author, creation date, title, description, ticket type and ticket status), plus the upvotes count and the complete list of comments for the ticket.   
For logged-in users, this is expanded by:
- a button to upvote the ticket (if not already upvoted),
- a button to edit the ticket (if raised by the current user and if in "OPENED" i.e. initial status),
- a text area and a button to post comments.

#### Upvoting system

Ticket upvoting is login-dependent. Any ticket can be upvoted only once by an individual user.    

##### Bug ticket upvoting 
Bug ticket upvoting is free of charge.   
The status of the upvote button provides clear feedback on the availability of the upvote function for the current user (greyed out if the ticket is already upvoted by the user, and completely absent if the user is not logged in).   
A click on the available Upvote button provides the user with success feedback, greys out the button, and updates the upvote count.
##### Feature ticket upvoting
The UI for the initiation of Ticket upvoting is near-identical to the one described above, with two differences:
- a lock icon is displayed on the Upvote button in Feature tickets, to indicate a reserved feature, and
- click on the available Upvote button triggers a confirmation modal which informs the user that it is a paid service (including the price) and provides the user with the option to cancel the action or to continue.

Confirmation of the modal redirects the user to a Stripe Card Payment processing form. Only credit card details (card number, CVV, expiry month and expiry year) are required to complete payment, the user is asked for no personal information.

The user is informed about the payment status on every step of the process, either by an error text next to the payment button (in case of invalid CVV or expiry date/month) or by a closable Bootstrap alert at the top of the screen. 

#### User handling
User handling relies completely on Django authorisation and forms to create and update user data and to authorise users. Thus the user has the option to register, log in, log out, edit password, edit profile data, and reset password via email.  


#### Defensive design

Defensive design principles have been implemented wherever possible, namely by restricting the ability to add to the database (ticket creation, ticket updating, adding of comments, upvoting) to logged-in users only and by restricting the edit possibilities only to the data "owned" (authored) by the current logged-in user.   
 Wherever possible, the restrictions have been implemented both at the frontend (absence of access to buttons/views) and at the backend (login_required view decoration, filtering querysets by author).

### Features left to implement

1. Add a better search algorithm (ability to search by complex phrases, as well as to search on both ticket title and description).

2. For the logged-in user, add the ability to edit and delete own comments.

3. Add additional ticket statuses (e.g. "Analysed" - to indicate that the ticket has been attended to i.e. it is no longer in initial state - and "Closed", to indicate that either the fix has been fully validated or that a ticket has been resolved in some other way).

4. Add an algorithm to prevent the user from accidentally creating a duplicated ticket by going back to a previously created ticket's form (time constraints prevented this from being implemented in the current version).


## Database structure

On top of the Django User model, which has not been modified for this project, three more models have been created:

1. **Ticket** - with User as Foreign Key (`author`).

    <table><tr><th>id</th><th>title</th><th>description</th><th>ticket_type</th><th>status</th><th>author_id</th><th>date_created</th><tr><tr><td>2</td><td>Some issue 1</td><td>Some description of issue 1 edited</td><td>FEATURE</td><td>SOLVED</td><td>3</td><td>2020-05-02</td></tr><tr><td>4</td><td>Some issue 2</td><td>Description of Issue 2 in a few words...</td><td>BUG</td><td>INPROG</td><td>3</td><td>2020-05-02</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

2. **Comment** - with User and Ticket as Foreign Keys (`author` and `rel_ticket`).

    <table><tr><th>id</th><th>text</th><th>created</th><th>rel_ticket_id</th><th>author_id</th><tr><tr><td>1</td><td>Here is my very fist comment to a ticket.</td><td>2020-05-04 11:47:20.171831</td><td>2</td><td>1</td></tr><tr><td>2</td><td>One more comment to this issue</td><td>2020-05-04 11:47:38.591623</td><td>2</td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>


3. **Upvote** - with User and Ticket as Foreign Keys (`upvoter` and `ticket`).

    <table><tr><th>id</th><th>ticket_id</th><th>upvoter_id</th><tr><tr><td>46</td><td>23</td><td>1</td></tr><tr><td>47</td><td>21</td><td>1</td></tr><tr><td></td><td></td><td></td></tr></table>


All Foreign Keys have been set with `on_delete=models.CASCADE`.

Each of the four models is handled by a separate app - `users`, `tickets`, `comments` and `upvotes`.





## Deployment

**The deployed app can be found here: [MothRadar](https://mothradar-ba79.herokuapp.com/)**

The application has been deployed to Heroku using the following procedure:

1. On Heroku, create a new app **mothradar-ba79**.
2. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).
3. In the project workspace's virtual environment, use `pip install` to install `dj-database-url`, `whitenoise` and `gunicorn` (psycopg2 has already been installed).
4. Run `pip freeze --local > requirements.txt` to update the requirements file.
5. From Heroku App Config Vars (Settings tab), copy the DATABASE_URL.    
In env.py, add the `DATABASE_URL`, a `DEVELOPMENT` environment variable with the value of `"1"`, and a `LOCALHOST` variable`.
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

9. In settings.py, under `DATABASES`, uncomment the Sqlite database and set the database selection (Sqlite and Postgres) depending on the `DATABASE_URL` variable:
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

12. Still in the root, create a folder named "static".

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

17. In Heroku App DashBoard, under the Deploy tab, select GitHub as Deployment method. In the search box, type the name of the GitHub repo (MothRadar) and click "Connect".     
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

    **Remember to check immediately that the `env.py` file is listed in your `.gitignore` file to prevent your sensitive data from being committed and pushed to GitHub.**

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

## Code validation

### HTML 

Validated using [W3C Markup Validation Service](https://validator.w3.org/).   
Issues found:
1. Register form -  "Element **ul** not allowed as child of element **small** in this context."
2. Password Reset Confirm form -  "Element **ul** not allowed as child of element **small** in this context."
3. Password Change form -  "Element **ul** not allowed as child of element **small** in this context."

These issues are related to the way Crispy Forms handles the HTML rendering of the respective Django forms.

Given that:
- these errors are not related to author-written code in any way,
- no display errors have been observed in rendering of the forms concerned in any of the test browsers, and
- elimination of the errors would imply dispensing with Crispy Forms altogether or at least a "manual" redesign of the forms concerned, which is time-prohibitive,   
it has been decided to proceed with deployment regardless of the aforementioned errors.


### CSS

Validated using [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/).   
No issues were found.

### JS

Validated using [JSHint](https://jshint.com/).   
No issues were found.

### Python 
Validated using [PEP8 online](http://pep8online.com/).   

Issues found: "Line too long" in lines 111 and 113-115 of `settings.py`:
```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]
```
Considering my insufficient experience as well as the absence of an unambiguous confirmation that configurations like these should also be split into concatenated multi-line strings, this snippet has been left as-is regardless of the raised pep8 errors. 






## Technologies Used

Languages:

- HTML for page structure and content;
- CSS for content styling;
- JavaScript for HTML DOM manipulation, Ajax server requests and Stripe payment processing;
- Python 3 for application logic;

Framework:
- [Django](https://www.djangoproject.com/) framework (v3.0.5) for application backend, development database provision (SQLite3), routing and template manipulation; 

Libraries:
- [Bootstrap](https://getbootstrap.com/) was used for responsive design, styling, navigation bar, buttons, alerts and modal implementation;
- [jQuery](https://jquery.com/) for easier DOM manipulation and for Stripe payment;
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to facilitate HTML rendering of Django forms;
- Fonts were obtained from [Google Fonts](https://fonts.google.com/);
- Icons were obtained from [FontAwesome](https://fontawesome.com/);

Development:
- [Visual Studio Code](https://code.visualstudio.com/) was used as the IDE for development and Git version control;
- [GitHub](https://github.com/) was used for source code storage;
- Google Chrome Developer Tools were used for development and testing, debugging and as a styling aid;
- [Travis CI](https://travis-ci.org/) for continuous integration;

Code validation tools:
- [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML and CSS code;
- [JSHint](https://jshint.com/) was used to validate JavaScript code;
- [PEP8 online](http://pep8online.com/) to validate Python code;

Deployment:
- [WhiteNoise](http://whitenoise.evans.io/en/stable) to facilitate Django static files serving on Heroku;
- [Heroku](https://www.heroku.com/) for application online deployment and production database provision (PostgreSQL);


Utilities:
- [wireframe.cc](https://wireframe.cc/) for wireframe creation;
- [W3schools.com Color Converter](https://www.w3schools.com/colors/colors_converter.asp) was used to convert colours between default, HEX and RGB for CSS coding purposes;
- [Autoprefixer CSS online](https://autoprefixer.github.io/) was used for correct vendor prefixing of CSS styles where required;
- [convertio.co](https://convertio.co/) was used to convert favicon image from SVG to PNG;
- [Favicon.io](https://favicon.io/) was used for favicon creation;

External (third-party) services:
- [Gmail](https://mail.google.com/) for sending of Password Reset messages to users;
- [Stripe](https://stripe.com/) v2 was used for credit card payment processing.


## Credits

### Code

#### HTML
1. The solution to highlight the currently active link in the sidebar within the ticket_list.html template (`{% if path == ... %}`) was found on [Stack Overflow](https://stackoverflow.com/).
2. The custom script to pass the Stripe Publishable Key into JavaScript (in upvotes.html) was obtained from the Code Institute course videos.   

#### JavaScript
The complete Stripe payment processing script (stripe.js file) was obtained from Code Institute course videos.

#### Python / Django
MothRadar being my first independent Django project, I had to still tackle the basics of Django together with building a full-fledged app. Thus I had to rely heavily on external resources, primarily on [Corey Schafer's YouTube Django series](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) tutorial and then on Code Institute course videos as well.   
While I never wanted to just copy-paste any code, especially not without understanding it, in the beginning stages of my project (the `users` app and the initial stage of the `tickets` app) I was coding along with the tutorials a lot, while adapting the code to the specific needs of my app. In later stages I relied mostly on Django documentation and occasionally on Stack Overflow to implement the desired functionality.    
Thus, while the concrete app implementation is definitely my own, the significant influence of Corey's videos is inevitable. This includes the idea to use Bootstrap cards to display the main items (tickets and comments), a sidebar, as well as the use of Crispy Forms to render Django forms.   
I have honestly tried to do all the coding as independently as I could once my understanding of Django and of documentation broadened, but at this stage of my coding education building a full Django app of this size completely independently would have been impossible, especially in the given timeframe. 

### Media
- Favicon image was obtained from [publicdomainvectors.org](https://publicdomainvectors.org/).


### Acknowledgements
Above all I would like to thank Chris (**ckz8780**) who helped me immensely on this project with his knowledge of Django. While never providing me with complete solutions, on multiple occasions he was able to point me to the right direction to look for them. He also helped me debug the Stripe payment functionality when I got completely stuck. Thanks, Chris!

Also, many thanks to all my fellow CI Slack members who also helped either by pointing me to various Django resources, by sharing their experiences, having walked the same path before me, or simply by encouraging me when I lost my momentum. **Anna**, **Jo**, **Simen**, **Johan** and **Anthony** - I owe you all bigtime!!  

Finally, a special THANK YOU to my mentor Narender, who always patiently tries and manages to find a way to push my limits just that tiny bit further. :) 



