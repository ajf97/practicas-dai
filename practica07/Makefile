
all:
	docker-compose up

build:
	docker-compose build

django-startproject:
	sudo docker-compose run web django-admin startproject sitio_web .
	sudo chown -R ${USER}:${USER} .

django-startapp:
	sudo docker-compose run web python manage.py startapp práctica_06
	sudo chown -R ${USER}:${USER} .

django-migrate:
	docker-compose run web python manage.py migrate 

django-make-migrations:
	docker-compose run web python manage.py makemigrations

django-createsuperuser:
	docker-compose run web python manage.py createsuperuser

django-shell:
	docker-compose run web python manage.py shell