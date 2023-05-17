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

