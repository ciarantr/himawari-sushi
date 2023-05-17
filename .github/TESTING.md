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