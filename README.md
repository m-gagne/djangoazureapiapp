# README

A sample Django API app that can be deployed as an Azure API App (part of an Azure App Service). This project uses common Pything/Django tools such as
    - djangorestframework
    - PyMySQL
    - waitress

## Dev Setup

Assumption is you are running Ubuntu or WSL (Windows Subsystem for Linux/Bash on Windows). If you are using OSX just replace apt-get with homebrew equivalents.

1. Install [pipenv](https://docs.pipenv.org/)

        sudo apt install software-properties-common python-software-properties
        sudo add-apt-repository ppa:pypa/ppa
        sudo apt update
        sudo apt install pipenv

    - Or follow whatever instructions from the [official site](https://docs.pipenv.org/).

1. Install a local [MySQL](https://www.mysql.com/) server

        sudo apt-get install mysql-server

    - *Note* if you are running this under WSL (bash on Windows) you will need to manually start the sql service by running `sudo service mysql start`

1. Setup Database

    - Connect to mysql server `mysql -u root -p` and run the following SQL below, be sure to change the password in the CREATE USER statement.

          create database djangoapi;
          CREATE USER 'apiuser'@'localhost' IDENTIFIED BY '<<YOUR_PASSWORD>>';
          GRANT ALL PRIVILEGES ON djangoapi.* to 'apiuser'@'localhost';
          FLUSH PRIVILEGES;

1. Rename `.env.sample` to `.env` and edit as necessary.
    - The .env file is excluded by the `.gitignore` file and should **never** be checked in.
1. Install required packages

        pipenv shell
        pipenv install

1. Run migration

        python manage.py migrate

1. Add a sample user

        python manage.py createsuperuser --email admin@example.com --username admin

## Azure Setup

1. Create your API app
1. Connect to your git/github repo
1. Go into `App Settings` and enable Python 3.4
1. Go to `Extensions` and install `Python 3.5.3 x64`
1. In cloud shell in d:\home\site\wwwroot run the following (run migrations and setup a super user)

        env\scripts\python manage.py migrate

        echo from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'password') | env\scripts\python manage.py shell