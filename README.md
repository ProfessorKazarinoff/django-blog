# django-blog

Repo for the code to a Django blog for my daughter. Follows Will Vincent's book Django for Beginners and Corey Schafer's Django Blog video series. Deployed on Heroku using the Heroku CLI and Windows Subsystem for Linux (WSL).


## Local Setup

clone repo, create virtual env, install requirements.txt

```
cp .env-example .env   # insert SECRET_KEY in .env file
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
mkdir media
mkdir media/images
python manage.py collectstatic
python manage.py runserver
```
