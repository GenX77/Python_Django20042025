#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate


# Crear superusuario automáticamente (si se define la variable de entorno)
# if [[ $CREATE_SUPERUSER ]]
# then
#   python manage.py createsuperuser --no-input
# fi