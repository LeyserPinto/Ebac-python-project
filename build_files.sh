# pip3 install -r requirements.txt 
# python3.9 manage.py collectstatic

pip3 install poetry
poetry install
poetry run python manage.py collectstatic
