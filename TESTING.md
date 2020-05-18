# MothRadar - Test Process and Findings

This document details the testing conducted on the deployed application, as well as the issues encountered, their analysis and solutions.

**Note to Assessors: to enable assessment of the backend/admin side of the app (if needed), a 'staff' account with read-only privileges has been created:**  

- **_username_: demoadmin**   
- **_password_: admintest456**


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

Particular attention has been paid to testing these forms during manual testing (see below) and no issues with rendering/display have been identified. 


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

## Continuous integration

[Travis CI](https://travis-ci.org/) has been used for continuous integration since the earliest stages of the project.   
The production build passes all integration tests. 

## Automated testing

Automated testing has been minimal. I managed to create several tests for users/views (see `users/test_views.py`) but quickly realised that the Django automated testing has a learning curve of its own and that drafting any meaningful automated test coverage would require significantly more time than the project deadline allowed for. Therefore automated testing was not implemented beyond the aforementioned cases, the focus was placed on manual testing instead.

## Manual testing

Manual testing was performed in three "stages":
- testing of User Stories,
- Testing of Features and Defensive Design, and
- Responsive design testing.

### User stories

_Note: As detailed in the UX section above, User Stories 11 and 12 (editing and deleting of user's comments) have not been implemented in this version and are therefore not tested._

All user stories have been tested. 

The following issues have been observed:
***
**Issue #1: Search filter view reverts to all tickets view upon "Next page" click.**

_Analysis: Upon Search, the queryset is set correctly (the number of pages is correct), but requesting the next page deletes the search call and reverts to the default queryset (and number of pages) of TicketListView._

_Solution: I have tried to override reverting to the default queryset but all my attempts have been unsuccessful. In the end a workaround has been implemented in the form of disabling pagination altogether for the search view (`self.paginate_by=None`), which is based on a post from Stack Overflow._

_Validation: Revalidate Python code of tickets/views.py. Verify that pagination is disabled for the search view, but is unaffected for other ticket list views and filters._ 

Outcome: Fix implemented, Python code successfully revalidated. Search view is no longer paginated so the issue is absent, and pagination on all other views/filters is unaffected.

**Conclusion: the issue has been fixed with a workaround. A better fix will be attempted in a future version.**
***
**Issue #2: Ticket list view and detail view needlessly display time (H:MM) of ticket creation.**

_Analysis: In a late stage of development, the date_created field format in the Ticket model has been changed to DateTimeField. However, in the ticket_list and ticket_detail templates no filter was added to filter out the time part._

_Solution: Add filter (display only date) to the display of object.date_created in the ticket_detail template and of ticket.date_created in the ticket_list template._  

_Validation: Revalidate HTML code of ticket_list.html and ticket_detail.html. Re-check display of concerned data in ticket list and ticket detail views._  

Outcome: Fix implemented, HTML code successfully revalidated, display of ticket list and ticket detail views checked. Issue has been fixed.

**Conclusion: Issue #2 is fixed and can be closed.**
*** 


### Features

#### Navbar 
1. Check that the navbar contents change dynamically dependent on whether the user is logged in or not.
2. Check that all links are working in both cases.
3. Check that the Create ticket button is not present if user is not logged in.

_All Navbar features have been tested successfully. No issue was found._

#### Landing page
1. Check that the landing page renders properly.
2. Check that the four information cards are responsive (colour highlight, toggle expand) upon clicking or hovering.
3. Check that the information cards display the desired textual information.
4. Check that the login and register anchors are only present if a user is not logged in.
5. Check that the registration and login anchors, when present, are functional.
6. Check that the footer anchor is functional and opens the link in a new tab.

_All Landing page features have been tested successfully. No issue was found._

#### Ticket list view, sorting and search
1. Check that the ticket list view displays all expected information.
2. Check that pagination is present.
3. Check that all pagination links (First, Prev, Next, Last) work as expected.
4. By going to the admin pages, check that the total list of tickets displayed corresponds to the total list of tickets in the database.
5. Check that the search box and sidebar links are rendered correctly.
6. Check that the sidebar view "My tickets" is only present if a user is logged in and then contains the correct number of tickets raised by that user.
7. Check that the default view in ticket list sorts tickets descending by date created.
8. Check that the "Most recent" view sorts tickets as expected.
9. Check that the "Most upvoted" view sorts tickets as expected.
10. Check that the "Bugs only" and "Features only" views filter tickets as expected.
11. Check that the search functionality works as expected. 

_All Ticket list view features have been tested successfully. No issue was found except as related to point 11, which is already highlighted in **Issue #1**._

_Note: during testing it has been observed that the Ticket view on the admin pages only logs the ticket title, which makes it difficult to check the number of tickets per author or type. Therefore an adjustment has been made to tickets/models.py to display all details (except date_created and description) in the admin pages. The corresponding Python code has been revalidated successfully._


#### Ticket detail view

1. Check that the Ticket detail view displays all ticket information, including upvotes count.
2. Check that the Upvote button is only present if a user is logged in. 
3. Check that the upvote button is greyed out if the logged-in user has already upvoted the ticket.
4. Check that the comments text area and Post comment button are only present if a user is logged in.
5. Check that existing comments (if any) are displayed regardless if a user is logged in or not.
6. Check that the "Edit ticket" button is only present if the logged-in user is the ticket author AND the ticket is in status "OPENED". If the edit button is not present, check that a manual (via URL) attempt to access the edit route for the ticket results in a "Not found" error.
7. If the Edit ticket button is available, check that it is possible to edit the title, description and ticket type fields of the ticket, and that all fields are mandatory. Check that, upon submission, the modified ticket details are updated. 

_All Ticket list view features have been tested successfully. No issue was found._

#### Upvoting system

1. Check that the Upvote button is displayed with a lock icon for Feature tickets (if not yet upvoted by the current logged-in user). Check that the lock icon is not displayed for Bug tickets under identical conditions.
2. Check that the Upvote button is greyed out and insensitive if the current logged-in user has already upvoted the ticket.
3. In a Bug ticket, upon clicking the Upvote button, check that the button becomes greyed out, a success message is displayed next to the button, and the upvote counter is increased by 1. Upon a repeated click, check that a message "Already upvoted." is displayed.
4. In a Feature ticket, upon clicking the Upvote button, check that a modal opens informing the user that this is a paid service (including the price) and offering the user the options to cancel or to proceed.
5. If the user selects Cancel, check that the modal closes, and the ticket's upvote count and the availability of the upvote button remain unchanged.
6. If the user selects Proceed, check that the browser redirects to the Payment Processing form.
7. Check that the Payment Processing form is displayed as expected.
8. Check that, upon entering of invalid card data:
    - card number shorter than 12 digits, or
    - CVV shorter than 3 digits, or
    - expiry month in the past,

    and clicking the Submit payment button, a corresponding error text is presented to the user next to the Submit payment button.   
9. Check that, upon entering valid card data and clicking Submit payment, if the payment is unsuccessful (e.g. due to card processing errors), a red alert banner is displayed below the Navbar. Check that the alert banner can be closed.
10. If the payment is successful, check that the browser redirects to the upvoted ticket's detail view, a green alert closable banner is displayed below the Navbar, the upvote button is greyed out, and the upvote count has been increased by 1.

_The upvoting system has been tested successfully. No issue was found._

#### Comments system

1. In the Ticket detail view, if a logged-in user attempts to submit a comment without entering any content into the comment text area, check that an information message is displayed next to the Submit comment button.
2. If a logged-in user submits a non-empty comment, check that the comment becomes displayed at the bottom of the existing comments (if any) and highlighted in green.
3. Upon page refresh, check that the newly submitted comment is displayed without highlight.
4. Check that the existing comments are sorted from newest at the top.
5. Check that there is a "No comments yet." paragraph if no comments have been submitted for the ticket yet. 

_The comments system has been tested successfully. No issue was found._

#### User handling
1. In the Register view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user.
2. In the Profile Update view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user. Check that it is not possible to change the username if a user of the same name already exists.
3. In the Password Change view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user.
4. In the Password Reset Confirm view, check that the form cannot be submitted with empty or invalid data. Check that clear feedback on invalid data is provided to the user.

_The user handling system has been tested successfully. No issue was found._

#### Defensive design
1. If the user is not logged in, check that a "manual" (via URL editing) attempt to access: 
    - ticket create view,
    - ticket edit view, 
    - profile view, 
    - upvote view (for Bug tickets), or
    - upvote-feature view (for Feature tickets)

    will redirect to login view.

2.  If a logged-in user attempts to manually (via URL) access the upvote-feature route for a ticket they have already upvoted, and they submit valid payment data, check that the browser redirects to the concerned ticket, a yellow alert closable banner is displayed below the Navbar, and the upvote count remains unchanged.   


### Responsive design

For all tests listed until now, Google Chrome has been used as the test browser. No issues except the already documented ones have been identified.

All relevant user stories have been retested using:
-  Mozilla Firefox, 
- Microsoft Edge,
- Google Chrome Developer Tools emulated device mode - iPhone X.

Particular attention was paid to the three forms (Register form, Password Reset Confirm form, Password Change form) which returned an error during HTML code validation.  

On Mozilla Firefox, no new issue was observed. The three aforementioned forms rendered without issues.

On Microsoft Edge, no new issue was observed. The three aforementioned forms rendered without issues.

On Google Chrome emulated device mode, the following issues were observed:
***
**Issue #3: The footer bar is displayed as a strip, not touching the bottom of the screen, and the footer text is stretching outside of it.**

_Analysis: Due to the narrow(er) screen width, the footer text splits into two lines. Since the current footer CSS height (4vh) is insufficient to cover two lines, the resulting text cannot be contained in the footer._

_Solution: in style.css, change the footer property to `min-height:4vh`, which will keep its current height on large screens but enable it to stretch if necessary on smaller ones._   

_Validation: Revalidate CSS code of style.css. Perform collectstatic and push the code to Heroku. Re-check display of footer on test screen and on desktop screen._   

Outcome: CSS code revalidated OK. Collectstatic performed and code redeployed to Heroku. Display unchanged on desktop, issue no longer present on test screen. Issue resolved.

**Conclusion: Issue #3 is fixed and can be closed.**
***
**Issue #4: In ticket list view, the search button is pushed to the second line, not aligned with the search box.**   

_Analysis: the search box width on small screens was set to Bootstrap_ `col-9 col-lg-8`, _which, together with margin settings, caused the button to wrap onto a second line on small screens._

_Solution: in ticket__ _list.html, modify the search box width to_ `col-8 col-md-9 col-lg-8` _to remove the issue on small screens and keep the good display on medium and large+ screens._  

_Validation: Revalidate HTML code of ticket__ _list.html. Re-check display of search box and buttons on test screen and on medium and desktop screens._ 

Outcome: HTML code revalidated OK. Display unchanged on medium and larger screens, issue no longer present on test screen. Issue resolved.   

**Conclusion: Issue #4 is fixed and can be closed.**
***
**Issue #5: In the slide-down navigation menu, the Create ticket button is abnormally wide (full screen width) with an unwanted left margin.**   

_Analysis: In base.html, the current Bootstrap margin styling of the Create ticket button (_`mt-5`_) only catered for the display on desktop screens. This needs to be adjusted for screens of lower width._

_Solution: in base.html, modify the Create ticket button Bootstrap styling to_ `mr-auto px-2 ml-lg-5` _to keep the button appearance on desktop screens, but to remove the unwanted margin and reduce the button width on smaller screens._   

_Validation: Revalidate HTML code of base.html. Re-check display of Create ticket button on test screen and on larger screens._ 

Outcome: HTML code revalidated OK. Create ticket button display unchanged on large+ screens, issue no longer present on test screen and sizes below large. Issue resolved.

**Conclusion: Issue #5 is fixed and can be closed.**
***

**Issue #6: In Ticket detail view, the upvote message unexpectedly pushes the Upvote button to the beginning of a new row.**

_Analysis: On large screens this issue is not visible, but on small widths the screen is not wide enough to contain the upvote count, the message, and the upvote button on one line._

_Solution: in upvotes.html, add a Bootstrap class of_ `d-none d-sm-inline` _to the upvoteMessage span, to keep the message hidden on small screens and prevent the button from being pushed to another row._ 

_Validation: Revalidate HTML code of upvotes.html. Re-check display of upvote message and Upvote button on test screen and on larger screens._

Outcome: HTML code revalidated OK. Issue no longer present on test screen, behaviour unchanged on larger screens. Issue resolved.   

**Conclusion: Issue #6 is fixed and can be closed.**
***
**Issue #7: In payment form view, the inline message for erroneous payment data is broken across two lines.**

_Analysis: On large screens this issue is not visible, but on small widths the screen is not wide enough to contain the whole the whole error message in one row, and the existing Bootstrap margin of `ml-3` looks awkward._

_Solution: in payment.html, modify the Bootstrap class of the stripe-error-message span to_ `d-block d-md-inline ml-md-3` _to force the whole message to be displayed below the button on small screens and to apply the margin only on screens from medium above._ 

_Validation: Revalidate HTML code of payment.html. Re-check display of payment error message and payment button on test screen and on larger screens._

Outcome: HTML code revalidated OK. Issue no longer present on test screen, behaviour unchanged on medium screens and above. Issue resolved.

**Conclusion: Issue #7 is fixed and can be closed.**
***
All five issues raised during Responsive design testing (Issues #3 - #7) have been fixed and closed. No new issues have been identified. The rendering of HTML forms that had raised errors during HTML validation shows no issues.

***
## Conclusion

A total of seven issues have been identified. Six of them have been fixed completely, and for one (Issue #1) a workaround solution has been implemented.   
The HTML code errors raised during code validation caused no issues in the functioning of the app.

**The application is considered ready for production.**