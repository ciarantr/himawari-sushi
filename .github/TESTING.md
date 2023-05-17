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
