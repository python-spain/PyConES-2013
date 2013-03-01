# Symposion

A conference management solution from Eldarion.

Built with the generous support of the Python Software Foundation.

See http://eldarion.com/symposion/ for commercial support, customization and hosting

## Quickstart

- `pip install -r requirements.txt`
- `python manage.py syncdb`
- `python manage.py loaddata fixtures/*`

## Setup Heroku remote

- `heroku login`
- `heroku keys:add`
- `heroku git:remote --app pycones`

## Deploy

- `git push heroku master`
