#!/usr/bin/env bash
# Exit on error
set -o errexit

# Print current directory to check where we start
echo "Current directory before installing dependencies:"
pwd
ls -la

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Print directory structure after installing dependencies
echo "Directory structure after pip install:"
pwd
ls -la

# cd into correct directory
cd todo_app

# Print directory structure inside todo_app
echo "Directory structure inside todo_app:"
pwd
ls -la

# Check if tree is available for a more detailed view
if command -v tree &> /dev/null
then
  echo "Directory structure inside todo_app (tree view):"
  tree
else
  echo "tree command not found, listing files manually"
  ls -R
fi

# Convert static asset files
echo "Running collectstatic..."
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
echo "Running migrations..."
python manage.py migrate

# List files again after migrations
echo "Directory structure after migrations:"
pwd
ls -la

# Create superuser if not created yet
if [[ $CREATE_SUPERUSER ]];
then
  echo "Creating superuser..."
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
