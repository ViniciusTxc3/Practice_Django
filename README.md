Init studies about Getting started with Django.

Ref.: [https://www.djangoproject.com/](https://www.djangoproject.com/)

# Install Django

> python -m pip install Django

# Version Django

> python -m django --version

# Create a project

First  init Django

> django-admin startproject mysite

# Verify

Enter in /mysite, then:

> python manage.py runserver 8080

Visit http://127.0.0.1:8000/ with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!

# Polls

> python manage.py startapp polls

# RUN

> python manage.py runserver

# Banco de dados

Comando para rodar as aplicações incluidas em INSTALLED_APPS em /mysite/settings.py

> python manage.py migrate

------
File /mysite/mysite/settings.py is in *.gitignore*
