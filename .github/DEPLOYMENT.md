# Deployment 🚀

[Navigate back to README Documentation](./README.md)

> 🔥 **Important**
>
> You will need the following installed on your system:
> 1. [Python3](https://www.python.org/downloads/)
> 2. [Node.js](https://nodejs.org/en/download/)
> 3. This project uses [pnpm](https://pnpm.io/installation) as the package manager, but you can use npm or yarn if you
     prefer. You will need to remove the pnpm-lock.yaml file and replace it with the appropriate lock file for your
     package manager of choice.

> 🔥 **Important**
>
> When you make changes to either TypeScript or CSS files, you will need to run `pnpm build` or `npm run build` to
> compile the changes to the `dist` folder and
> run `python3 manage.py collectstatic  python manage.py collectstatic --upload-unhashed-files` to upload the assets to
> cloudinary. This on only when you are ready to deploy to production so the manifest file matches the correct static file
> name & hash.

## 🏗 Remote Deployment

The live deployed application can be found deployed on [Heroku](https://himawari-sushi.herokuapp.com/).

## 🐘 ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: himawari-sushi).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### ☁️ Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku
doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build,
run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> 💁 **Tip**
>
> Django has a built in `SECRET_KEY` generator, which can be used to generate a new key for your app.
> Run the following command in the Terminal/CLI:
>
> `python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
> This will generate a new secure key, which you can copy and paste into the Heroku Config Vars.

| Key                     | Value                                                                |
|-------------------------|----------------------------------------------------------------------|
| `CLOUDINARY_URL`        | user's own value                                                     |
| `DATABASE_URL`          | user's own value                                                     |
| `PRODUCTION_HOSTNAME`   | user's own value  (your heroku app url)                              |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY`            | user's own value                                                     |
| `DEVELOPMENT`           | `False` (for production)                                             |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment 🛠️

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python

import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("Development", "True")

```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Start vite server: `pnpm dev` or `npm run dev`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ciaran-io/himawari-sushi)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your
   clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/ciaran-io/himawari-sushi.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ciaran-io/himawari-sushi)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make
changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ciaran-io/himawari-sushi)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork"
   Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

During local development, you will need to run one server for Django, and another for Vite. This is because Vite is used
to serve the TypeScript and CSS files, and Django is used to serve the HTML & image files. During deployment, Heroku
will run the Django server, and Vite will no longer be needed.

When you are make further changes to either the CSS or TypeScript files and are ready for a new deployment, will need to
run `pnpm build` or `npm run build`
to compile the files into the `dist` folder. Then you will need to
run `python manage.py collectstatic --upload-unhashed-files` to upload the new files to Cloudinary.

🔝 [Back to Top](#deployment-)