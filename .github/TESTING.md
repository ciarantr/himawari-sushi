# Testing 🧪

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
Some pages require a user to be logged-in and authenticated, in order to view the page. so I have used the
[validate by input](https://validator.w3.org/#validate_by_input) method, which requires you to copy/paste
the entire HTML code into the validator.

Pages that have (validate by input) next to them, require you to copy/paste the entire HTML code into the validator.

| Page                                    | W3C URL                                                                                     | Screenshot                                                                    | Notes     |
|-----------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| About                                   | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/about)          | ![screenshot](../docs/testing/w3-validator/about-page.png)                    | No errors |
| Contact                                 | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/contact)        | ![screenshot](../docs/testing/w3-validator/contact-page.png)                  | No errors |
| Contact form success(validate by input) | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/contact)        | ![screenshot](../docs/testing/w3-validator/contact-success-page.png)          | No errors |
| Create booking(validate by input)       | [W3C](https://himawari-sushi.herokuapp.com/nu/#textarea)                                    | ![screenshot](../docs/testing/w3-validator/create-booking-logged-in-page.png) | No errors | 
| Create booking (logged out)             | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/booking/create) | ![screenshot](../docs/testing/w3-validator/create-booking-page.png)           | No errors |
| Home                                    | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/)               | ![screenshot](../docs/testing/w3-validator/home-page.png)                     | No errors |
| Menu                                    | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/menu)           | ![screenshot](../docs/testing/w3-validator/menu-page.png)                     | No errors |
| Register                                | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/register)       | ![screenshot](../docs/testing/w3-validator/register-page.png)                 | No errors |
| Login                                   | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/login)          | ![screenshot](../docs/testing/w3-validator/login-page.png)                    | No errors |
| Profile(validate by input)              | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/#textarea)      | ![screenshot](../docs/testing/w3-validator/profile-dashboard-page.png)        | No errors |
| Profile details(validate by input)      | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/#textarea)      | ![screenshot](../docs/testing/w3-validator/profile-details-page.png)          | No errors |
| Profile bookings(validate by input)     | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/#textarea)      | ![screenshot](../docs/testing/w3-validator/profile-bookings-page.png)         | No errors |
| Reservations                            | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/reservations)   | ![screenshot](../docs/testing/w3-validator/reservations-page.png)             | No errors |
| Subscribe success(validate by input)    | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/#textarea)      | ![screenshot](../docs/testing/w3-validator/subscribe-success-page.png)        | No errors |
| Subscribe success (validate by input)   | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/#textarea)      | ![screenshot](../docs/testing/w3-validator/subscribe-success-page.png)        | No errors |
| Error 404 (validate by input)           | [W3C](https://validator.w3.org/nu/?doc=https://himawari-sushi.herokuapp.com/#textarea)      | ![screenshot](../docs/testing/w3-validator/error-404-page.png)                | No errors |

[🔝 Back to Top](#testing-)

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

There is only one single css file compiled & minified from all the other css files.

> 🔥**Important**
>
> CSS validation has returned 56 CSS parsing errors. This issue is a result of the final ccs build
> using [Tailwindcss](https://tailwindcss.com/). The maintainer of TailwindCSS has discussed this issue and provided a
> solution; however, the recommended fix cannot be used as it is causing issues with the styles used within the
>
application. [Remove --tw- variables from universal selector #7317](https://github.com/tailwindlabs/tailwindcss/discussions/7317)
> 🔗

| File     | W3C URL                                                                                                                                                                | Screenshot                                                     | Notes           |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------|
| main.css | [w3c validator](https://jigsaw.w3.org/css-validator/validator?uri=https://himawari-sushi.herokuapp.com/&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](../docs/testing/w3-validator/css-validation.png) | Fail: 56 errors |

### TypeScript

I have used [Eslint](https://eslint.org/) to validate all of my TypeScript files. I have used the recommended
Eslint & [typescript-eslint](https://typescript-eslint.io/) plugins to validate all of my TS files with a custom
configuration located in `.tsconif.json` at the root directory.

This evolved using pnpm to install the Eslint with TypeScript plugins located in `package.json` located at the root
directory. I can run the following command to validate all of my TS files:

> **Note**
>
> You will need to have [pnpm](https://pnpm.io/) installed to run the following command, or you can use npm or yarn.

```bash
pnpm  eslint --fix-dry-run static/src/js/main.ts
```

The ide im using [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) is also highlighting any
TypeScript / Eslint errors in the code. This is based on the configuration in
the `.eslintrc.yml` & `tsconfig.json` file.

Pycharm generated report:

| File                      | Screenshot                                                             | Notes                                                    |                                                    
|---------------------------|------------------------------------------------------------------------|----------------------------------------------------------|
| Pycharm inspection report | ![screenshot](../docs/testing/jetbrains/javascript/pycharm-report.png) | Eslint redundant double negation (no-extra-boolean-cast) |

### Python

I have used the
recommended [PyCharm quality Assistance](https://www.jetbrains.com/help/pycharm/tutorial-code-quality-assistance-tips-and-tricks.html)
with built-in pep8 support to validate all of my Python files. This provides both instant analyses of the code along
with ability to generate a report. All python files were validated using pycharm inspection tools with the exceptions of
the following files:

- `All files located in migrations directories`
- `__init__.py`

| File                      | Screenshot                                                      | Notes     |
|---------------------------|-----------------------------------------------------------------|-----------|
| pycharm inspection report | ![screenshot](../docs/testing/jetbrains/python/pep8-report.png) | No errors |

> **IMPORTANT**: Django settings.py
>
> The Django settings.py has been configured to ignore the following errors:
> - `E501 line too long (82 > 79 characters)`

`noqa` = **NO Quality Assurance**

Example:

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

[🔝 Back to Top](#testing-)

## Browser testing

I utilised both manual and automated testing to test the application on various browsers and devices.
I used the following browsers to test the application:

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Safari](https://support.apple.com/downloads/safari)

### Manual testing

Pages tested:

| Page                        | Sizes                     | Notes             |
|-----------------------------|---------------------------|-------------------|
| About page                  | Mobile - Tablet - Desktop | Works as expected |
| Booking page                | Mobile - Tablet - Desktop | Works as expected |
| Contact page                | Mobile - Tablet - Desktop | Works as expected |
| Login Page                  | Mobile - Tablet - Desktop | Works as expected |
| Menu page                   | Mobile - Tablet - Desktop | Works as expected |
| Profile page                | Mobile - Tablet - Desktop | Works as expected |
| Profile page - bookings     | Mobile - Tablet - Desktop | Works as expected |
| Profile page - user details | Mobile - Tablet - Desktop | Works as expected |
| Register Page               | Mobile - Tablet - Desktop | Works as expected |
| Reservations Page           | Mobile - Tablet - Desktop | Works as expected |

> **Note**
>
> I used [Polypane](https://polypane.app/) to test the application on multiple devices at the same time
> with the following configurations to ensure the application is responsive on all devices:
>
> - Mobile: 375px x 812px
> - Tablet: 744px x 1024px
> - Desktop: 1440px x 1080px

After inspection of all pages, I took screenshots of each page & on all device sizes noted above. They are available in
the [polypane folder](../docs/testing/polypane/) directory. Due
to the number of pages and screens tested, I have only included a few examples below.

| Page      | Mobile                                                              | Tablet                                                              | Desktop                                                               | Notes             |
|-----------|---------------------------------------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------|
| Home Page | ![screenshot](../docs/testing/polypane/mobile/home-page-mobile.jpg) | ![screenshot](../docs/testing/polypane/tablet/home-page-tablet.jpg) | ![screenshot](../docs/testing/polypane/desktop/home-page-desktop.jpg) | Works as expected |

### Automated testing

I used [Playwright](https://playwright.dev/) to test the application on multiple browsers and devices. The following
browsers & user actions were tested:

> **Note**
>
> All tests where recorded and are available in the [playwright folder](../docs/testing/e2e/playwright/videos)
> directory. Below are a few examples of the tests, you can find the playwright test files in the
> [test/playwright](../tests/playwright) directory.

Authentication testing:

| Browser                 | Device  | Page | Action            | Expected Result           | Actual Result       | Notes |
|-------------------------|---------|------|-------------------|---------------------------|---------------------|-------|
| Chrome, Safari, Firefox | Desktop | Home | test registration | user can register account | successful register | pass  |
| Chrome, Safari, Firefox | Mobile  | Home | test registration | user can register account | successful register | pass  |
| Chrome, Safari, Firefox | Mobile  | Home | test login        | user can login to account | successful login    | pass  |
| Chrome, Safari, Firefox | Desktop | Home | test login        | user can login to account | successful login    | pass  |
| Chrome, Safari, Firefox | Desktop | Home | test login fail   | display error message     | fail login          | pass  |
| Chrome, Safari, Firefox | Desktop | Home | test logout       | user logout               | successfully logout | pass  |

Booking testing:

| Browser                 | Device  | Page                        | Action              | Expected Result           | Actual Result             | Notes |
|-------------------------|---------|-----------------------------|---------------------|---------------------------|---------------------------|-------|
| Chrome, Safari, Firefox | Desktop | Booking create page         | test create booking | user can create a booking | successful booking        | pass  |
| Chrome, Safari, Firefox | Desktop | Profile booking delete page | test delete booking | user can delete a booking | successful booking delete | pass  |
| Chrome, Safari, Firefox | Desktop | Profile booking edit page   | test edit booking   | user can edit a booking   | successful booking edit   | pass  |

Contact form testing:

| Browser                 | Device  | Page         | Action            | Expected Result                           | Actual Result           | Notes |
|-------------------------|---------|--------------|-------------------|-------------------------------------------|-------------------------|-------|
| Chrome, Safari, Firefox | Desktop | Contact page | test contact form | user can send a message with contact form | successful message sent | pass  |

User profile form testing:

| Browser                 | Device  | Page         | Action            | Expected Result                               | Actual Result             | Notes |
|-------------------------|---------|--------------|-------------------|-----------------------------------------------|---------------------------|-------|
| Chrome, Safari, Firefox | Desktop | Profile page | test user profile | user can update profile & details are correct | successful profile update | pass  |

[🔝 Back to Top](#testing-)

## Lighthouse Audit

I used [Lighthouse cli](https://github.com/GoogleChrome/lighthouse) to audit the application. I tested the application
for each page on both mobile and desktop devices.

> **Note**
>
> I Added the results to the [lighthouse folder](../docs/testing/lighthouse) directory. It contains an HTML report for
> each page and device size. Please note I originally named the heroku url **django-suhshi.herokuapp.com**, but I
> changed
> it to **himawari-sushi.herokuapp.com**. The lighthouse reports are named using the original url; however, the results
> are correct. This change was for consistency with the project name.

| Page                    | Device  | Performance | Best Practices | Accessibility | SEO |
|-------------------------|---------|-------------|----------------|---------------|-----|
| Home page               | Mobile  | 87          | 100            | 100           | 100 |
| About page              | Mobile  | 94          | 100            | 100           | 100 |
| Booking Create page     | Mobile  | 98          | 100            | 100           | 100 |
| Menu page               | Mobile  | 98          | 100            | 100           | 100 |
| Contact page            | Mobile  | 98          | 100            | 100           | 100 |
| Reservations page       | Mobile  | 95          | 100            | 100           | 100 |
| Login page              | Mobile  | 98          | 100            | 100           | 100 |
| Register page           | Mobile  | 99          | 100            | 100           | 100 |
| Profile page            | Mobile  | 98          | 100            | 100           | 92  |
| Profile page - bookings | Mobile  | 98          | 100            | 100           | 92  |
| Profile page - details  | Mobile  | 98          | 100            | 100           | 92  |
| Home page               | Desktop | 97          | 100            | 100           | 97  |
| About page              | Desktop | 97          | 100            | 100           | 96  |
| Booking create page     | Desktop | 97          | 100            | 100           | 96  |
| Menu page               | Desktop | 98          | 100            | 100           | 96  |
| Contact page            | Desktop | 97          | 100            | 100           | 97  |
| Reservations page       | Desktop | 98          | 100            | 100           | 96  |
| Login page              | Desktop | 98          | 100            | 100           | 100 |
| Register page           | Desktop | 98          | 100            | 100           | 100 |
| Profile page            | Desktop | 100         | 100            | 92            | 90  |
| Profile page - bookings | Desktop | 100         | 100            | 92            | 90  |
| Profile page - details  | Desktop | 100         | 100            | 92            | 90  |

[🔝 Back to Top](#testing-)

## Python coverage

I used [coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/) package to test the python code coverage. I used the CLI to run the tests and generate the report. All results are in the [coverage folder](../tests/htmlcov)

The following table shows the coverage for each app.

| App      | Screen Shot                                                     | Coverage |
|----------|-----------------------------------------------------------------|----------|
| Accounts | ![screenshot](../docs/testing/coverage/report-app-home.png)     | 93%      |
| Booking  | ![screenshot](../docs/testing/coverage/report-app-bookings.png) | 86%      |
| Customer | ![screenshot](../docs/testing/coverage/report-app-customer.png) | 87%      |
| Home     | ![screenshot](../docs/testing/coverage/report-app-home.png)     | 93%      |

## Defensive Programming

Forms:

> **Important**
>
> All forms have validation on the front-end and back-end. The validation rules are set in the model and form classes.
> The front-end validation uses pattern matching to ensure the user enters the correct data type. The back-end
> validation will send an error message if the user enters the wrong data type or if nefarious data is entered.

- Contact form
  - The contact form uses the `required` & `pattern` attribute to ensure the user enters the correct data type.
  - The user will receive an error message if any of the form fields are incorrect.
- Login form
  - The login form uses the `required` & `pattern` attribute to ensure the user enters the correct data type.
  - The user will receive an error message if the username or password is incorrect.
- Register form
  - The register form uses the `required` & `pattern` attribute to ensure the user enters the correct data type.
  - The user will receive an error message if the username or email is already in use.
- Booking form
  - The booking form uses the `required` & `pattern` attribute to ensure the user enters the correct data type.
  - The booking form already has a booking date and time set. The user can only select a date and time in the future.
- Profile form
  - The profile form uses the `required` & `pattern` attribute to ensure the user enters the correct data type.
  - The user will receive an error message if the username or email is already in use.

Prevent unauthorized access (Django middleware):

- Users profile page
  - Users cannot access the profile page if they are not logged in. The user will be redirected to the login page.


- Users bookings / edit or delete booking
  - Users cannot edit a booking unless they are the owner of the booking & logged in. The user will be redirected to the
    home page & receive an error message.

| Page             | User Action                                 | Expected Result                                    | Pass/Fail | Comments              |
|------------------|---------------------------------------------|----------------------------------------------------|-----------|-----------------------|
| Home Page        |                                             |                                                    |           |                       |
|                  | Click on Logo                               | Redirection to Home page                           | Pass      |                       |
|                  | Click on Book link in navbar                | Redirection to Booking create page                 | Pass      |                       |
|                  | Click on Menu link in navbar                | Redirection to Menu page                           | Pass      |                       |
|                  | Click on Login link in navbar               | Redirection to Login page                          | Pass      |                       |
|                  | Click on Sign up link in navbar             | Redirection to Register page                       | Pass      |                       |
|                  | Click on Explore more link in About section | Redirection to About page                          | Pass      |                       |
|                  | Click on Subscribe link after email input   | Redirection to Subscribe success page              | Pass      |                       |
|                  | Click on About link in footer               | Redirection to About page                          | Pass      |                       |
|                  | Click on Menu link in footer                | Redirection to Menu page                           | Pass      |                       |
|                  | Click on Book link in footer                | Redirection to Book page                           | Pass      |                       |
|                  | Click on Contact us link in footer          | Redirection to Contact us page                     | Pass      |                       |
|                  | Click on Reservations link in footer        | Redirection to Reservations page                   | Pass      |                       |
|                  | Click on Facebook link in footer            | Redirection to Facebook page                       | Pass      |                       |
|                  | Click on Instagram link in footer           | Redirection to Instagram page                      | Pass      |                       |
|                  | Click on Twitter link in footer             | Redirection to Twitter page                        | Pass      |                       |
| Contact Page     |                                             |                                                    |           |                       |
|                  | Click on Contact link in footer             | Redirection to Contact page                        | Pass      |                       |
|                  | Enter full name                             | Field will accept freeform text                    | Pass      |                       |
|                  | Enter valid email address                   | Field will only accept email address format        | Pass      |                       |
|                  | Enter valid phone number                    | Field will only accept telephone format            | Pass      |                       |
|                  | Enter message in textarea                   | Field will accept freeform text                    | Pass      |                       |
|                  | Click the send message button               | Redirects user to contact success page             | Pass      |                       |
| Sign Up          |                                             |                                                    |           |                       |
|                  | Click on Sign Up link                       | Redirection to Sign Up page                        | Pass      |                       |
|                  | Enter valid email user name                 | Field will only accept freeform text               | Pass      |                       |
|                  | Enter valid email address                   | Field will only accept email address format        | Pass      |                       |
|                  | Enter valid password (twice)                | Field will only accept password format             | Pass      |                       |
|                  | Click on Sign Up button                     | User is logged in and redirected to home page      | Pass      |                       |
| Log In           |                                             |                                                    |           |                       |
|                  | Click on the Login link                     | Redirection to Login page                          | Pass      |                       |
|                  | Enter valid email address                   | Field will only accept email address format        | Pass      |                       |
|                  | Enter valid password                        | Field will only accept password format             | Pass      |                       |
|                  | Click Login button                          | Redirects user to home page                        | Pass      |                       |
| Log Out          |                                             |                                                    |           |                       |
|                  | Click Logout button                         | Redirects user to logout page                      | Pass      | Confirms logout first |
|                  | Click Confirm Logout button                 | Redirects user to home page                        | Pass      |                       |
| Profile          |                                             |                                                    |           |                       |
|                  | Click on Profile button                     | User will be redirected to the Profile page        | Pass      |                       |
|                  | Click on the View booking                   | User will be redirected to the their bookings page | Pass      |                       |
| Profile bookings |                                             |                                                    |           |                       |
|                  | Click on the Edit booking                   | User will be redirected to the edit bookings page  | Pass      |                       |
|                  | Click on the Delete booking                 | User will be prompted to confirm via a dialog      | Pass      |                       |
| Profile account  |                                             |                                                    |           |                       |
|                  | Click on the Update link                    | User will be prompted to confirm via a dialog      | Pass      |                       |

[🔝 Back to Top](#testing-)

## User Story Testing

### New Site Users

| User Story           | As a new site user, I would like to...                                    | So that I can...                         | status |
|----------------------|---------------------------------------------------------------------------|------------------------------------------|--------|
| Account registration | receive feedback if there is a problem registering                        | Sign up successfully                     | ✅      |
| Contact form         | receive feedback if there is a problem with submitting a contact form     | Confirm my message has sent successfully | ✅      |
| Subscribe            | receive feedback if there is a problem with submitting a subscribing form | Confirm my  subscript                    | ✅      |

### Returning Site Users

| User Story                 | As a returning site user, I would like to...                  | So that I can...                 | status |
|----------------------------|---------------------------------------------------------------|----------------------------------|--------|
| Account login              | receive feedback if there is a problem logging in             | Insure I Logged in successfully  | ✅      |
| Account logout             | receive feedback if there is a problem logging out            | Insure I Logged out successfully | ✅      |
| Account information update | receive feedback if my account information updated            | Insure my information is correct | ✅      |
| Booking creation           | receive feedback if there is a problem creating a new booking | Successfully make a booking      | ✅      |
| Booking editing            | receive feedback if there is a problem editing a booking      | Successfully edit a booking      | ✅      |
| Booking deletion           | receive feedback if there is a problem deleting a booking     | Successfully delete a booking    | ✅      |

### Site Admin

| User Story                     | As a site admin, I would like to... | So that I can...          | status |
|--------------------------------|-------------------------------------|---------------------------|--------|
| Edit / delete customer booking | remove or make changes to bookings  | make changes where needed | ✅      |
| Edit / delete customers        | remove or make changes to customers | make changes where needed | ✅      |

## 🐛 Bugs

There are no remaining bugs that I am aware of in the application. Any bugs that were identified during development were fixed.

## Unfixed Bugs (Python package)

- I am using the [django vite](https://pypi.org/project/django-vite/) pip package to integrate vite into my django project. This is a new package and I have found a bug with it. All css has to be imported into the TypeScript file otherwise the css is loaded by a script tag and not a link tag during production, & causes a `500 server error`. The only workaround is to import the css file into a TypeScript or JavaScript file. This is not ideal as it means I have to import all css files rather than using directly in a html file.

[🔝 Back to Top](#testing-)
