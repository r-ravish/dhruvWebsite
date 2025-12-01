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

# Create default categories if they don't exist
python manage.py shell -c "
from store.models import Category

default_categories = [
    ('Trading Cards', 'trading-cards'),
    ('Collectible Toys', 'collectible-toys'),
    ('Board Games', 'board-games'),
    ('Video Games', 'video-games'),
    ('Comics & Books', 'comics-books'),
    ('Figures & Statues', 'figures-statues'),
]

for name, slug in default_categories:
    category, created = Category.objects.get_or_create(
        slug=slug,
        defaults={'name': name}
    )
    if created:
        print(f'Created category: {name}')
    else:
        print(f'Category exists: {name}')
"

echo "Build completed successfully!"
