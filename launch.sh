cd HCapp
sudo fuser -k 8000/tcp
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
xdg-open http://127.0.0.1:8000/
