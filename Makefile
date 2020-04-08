.PHONY:

pull:
	docker-compose pull
build: pull
	docker-compose build
up: build
	docker-compose up -d
down:
	docker-compose down
volume: down
	docker volume prune -f
migrations:
	# docker-compose run --rm api python minimal.py makemigrations
migrate: migrations
	# docker-compose run --rm api python minimal.py migrate
populatedb: migrate
	docker-compose run --rm api python minimal.py populatedb
	docker-compose run --rm api python minimal.py seed app --number=20
logs:
	docker-compose logs
	docker ps -a
init: volume up migrate logs
postgres:
	docker-compose exec db psql -U postgres
app:
	docker-compose exec app sh
su:
	docker-compose run --rm app python manage.py createsuperuser
test:
	docker-compose run --rm api python minimal.py test
deploy:
	docker-compose run --rm api sls deploy
