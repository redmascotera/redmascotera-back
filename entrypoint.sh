#!/bin/sh

set -e

echo "Importing environment variables"

. "app/.env"

echo "Flush the manage.py command at startup of project"

# while ! python manage.py flush --no-input 2>&1; do
#   echo "Running flush command"
#   sleep 3
# done

echo "Preparing Database Migrations"
while ! python manage.py makemigrations 2>&1; do
  echo "Make Migrations in process"
  sleep 3
done

echo "Executing Migrations"

while ! python manage.py migrate  2>&1; do
   echo "Migration in process"
   sleep 3
done

echo "Entry point completed"

exec "$@"