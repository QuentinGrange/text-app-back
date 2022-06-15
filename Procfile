release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2