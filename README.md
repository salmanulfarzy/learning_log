# Learning Log  [![Heroku](http://heroku-badge.herokuapp.com/?app=sfarzy-learning-log&style=flat)](https://sfarzy-learning-log.herokuapp.com/)

https://sfarzy-learning-log.herokuapp.com/  

Django application to take notes while you study them. Each user can add new topics and entries. 

Entries are categorized on topics added by user.  User's are requested to register if they are not logged in and only registered usrs will be able add topics, entries or edit entries. App has basic bootstrap styling.

There are two applications in this project. `learning_log` will manage the notes and `users` will manage user operations like login, logout and user authentication.

## Installation

Follow the below steps to set it up on a machine. Preferably manage python packages using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

```
git clone https://github.com/sfarzy/learning_log.git
cd learning_log
pip install -r requirements.txt
python manage.py runserver
```

### TODO

 - [ ] Markdown support
 - [ ] Email for user registration
 - [ ] Abilityt to update password
 - [ ] User specific topic id's
 
