release:python manage.py migrate
web gunicorn shopify.wsgi --log-file -