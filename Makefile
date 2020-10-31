.PHONY:
init: down up migrate logs
pull:
	docker-compose pull
build: pull
	docker-compose build
up: build
	docker-compose up -d
down:
	docker-compose down --remove-orphans -v
migrations:
	docker-compose run --rm minimal python minimal.py makemigrations
migrate: migrations
	docker-compose run --rm minimal python minimal.py migrate
populatedb: migrate
	docker-compose run --rm minimal python minimal.py populatedb
	docker-compose run --rm minimal python minimal.py seed app --number=20
logs:
	docker-compose logs
	docker ps -a
postgres:
	docker-compose exec db psql -U postgres
app:
	docker-compose exec app sh
su:
	docker-compose run --rm minimal python manage.py createsuperuser
test:
	docker-compose run --rm minimal python minimal.py test
