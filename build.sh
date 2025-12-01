#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth.models import User
import os
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'dhruv')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'dhruv@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created')
elif User.objects.filter(username=username).exists():
    print(f'Superuser {username} already exists')
else:
    print('DJANGO_SUPERUSER_PASSWORD not set, skipping superuser creation')
"
