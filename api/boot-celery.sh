#Boot the Celery Worker for the Application using app-worker.py
set -o allexport; source .env; set +o allexport

celery -A app-worker.celery worker --loglevel=WARNING --concurrency=10 -n $APP_NAME@%d