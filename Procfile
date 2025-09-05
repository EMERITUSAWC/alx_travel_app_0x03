web: python manage.py runserver 0.0.0.0:8000
worker: celery -A alx_travel_app.celery_app worker --loglevel=info
beat: celery -A alx_travel_app.celery_app beat --loglevel=info
