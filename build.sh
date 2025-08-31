#!/usr/bin/env bash
# Simple build script for Render

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Applying database migrations ==="
python manage.py migrate