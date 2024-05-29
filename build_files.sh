pip3 install -r requirements.txt 

pip3 install poetry
pip install wheel
pip3 install psycopg2

python3.9 manage.py collectstatic

# pip3 install poetry
poetry install
poetry run python manage.py collectstatic
