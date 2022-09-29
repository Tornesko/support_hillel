# Support Hillel

The essence of the project is that users can create tickets in which they describe the problem they are interested in
and send these tickets to the managers of the support service, and then a chat starts where the manager helps the user
solve his problem.
___

# Run application with docker

```bash
docker build -t support_django .
docker run -p 8000:80 -v $PWD:/app/ --rm -it support_django
```

___

# With docker-compose

```bash
docker-compose up -d
```

___

## dump database

```bash

docker exec -t support_postgres pg_dump -c -U support > dump.sql
```

## restore database

```bash
cat dump.sql | docker exec -i support_postgres psql -U support
``` 

___

## Setup the environment

```
pip install pipenv
pipenv shell
```

___

# Code quality tools

### Install codequality utils

```
pip install black && pip install isort && pip install flake 8
```

#### Use them in *pre-commit-config.yaml*

___

## Startproject

```
pip install django
django startproject name
```

___

# DataBase

![](/home/tornesko/PycharmProjects/HillelSupport/docs/database.png)

# Apps

![](/home/tornesko/PycharmProjects/HillelSupport/docs/file_structure.jpeg)

### Authentication:

```
./manage.py startapp Authentication
```

- Here are defined *User* and *Role* models for authentication
- Also, settings for view of admin panel

### Config:

- It is main configuration directory for django project

### Core:

```
./manage.py startapp Core
```

- Main app of project
- Here are defined *Tickets* and *Comments* models for db
- ***Api*** for frontend developers

___

# Other files

- **Share** dir it is package with third party utils
- **db.sqlite3**: database
- **.gitignore**: GitHub ignore
- **manage.py**: This manage.py utility provides various commands that you must have while working with Django.
- **.flake8**: configurations for linter
- **templates**: for templates of ***html*** or ***xml*** pages

___

## Useful links

- [django docs](https://docs.djangoproject.com/en/4.1/)
- [DRF docs](https://www.django-rest-framework.org/)

