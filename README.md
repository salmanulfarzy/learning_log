# Learning Log  [![Heroku](https://img.shields.io/badge/heroku-deployed-brightgreen.svg)](https://sfarzy-learning-log.herokuapp.com/)

Django application to take notes while you study them. Each user can add new topics and entries.

Entries are categorized on topics added by user.  User's are requested to register if they are not logged in and only registered usrs will be able add topics, entries or edit entries. App has basic bootstrap styling.

There are two applications in this project. `learning_log` will manage the notes and `users` will manage user operations like login, logout and user authentication.

## Installation

Follow the below steps to set it up on a machine. Preferably manage python packages using virtual environments like [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [virtualenv](https://pypi.python.org/pypi/virtualenv) or [venv](https://docs.python.org/3/library/venv.html) which comes along with `python` >= 3.3
```
git clone https://github.com/sfarzy/learning_log.git
cd learning_log
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

### TODO

- <strike>Markdown support</strike>
- Email for user registration
- User specific topic id's
- Abilityt to update password

### Dependencies
 
- [django](https://www.djangoproject.com/)
- [django-bootstrap](https://github.com/dyve/django-bootstrap3)
- [django-markdownx](https://github.com/adi-/django-markdownx)
