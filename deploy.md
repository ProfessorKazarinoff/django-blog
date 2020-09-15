# Deployment

## Deploy using Heroku

Make sure the Heroku CLI is installed

```
python -m pip install django-heroku
python -m pip install gunicorn
python -m pip install whitenoise
python -m pip freeze > requirements.txt
git add .
git commit -m "ready for Heroku deployment"
git push origin master
heroku login
heroku create miaowl-blog
heroku config:set SECRET_KEY=XXXXXMy_Secret_KeyXXXXXXXXXX
git push heroku master:main
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open
```

To remove the app from Heroku

```
heroku apps         # see the name of the Heroku app
heroku apps:destroy miaowl-blog   # use the name of the Heroku app
```
