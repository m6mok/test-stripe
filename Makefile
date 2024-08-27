collect : # freeze recently installed dependencies
	uv pip freeze | uv pip compile - -o requirements.txt

up : # docker compose local
	touch ./env/local/.env
	cat ./env/local/ports.env ./env/local/postgres.env ./env/local/database.env > ./env/local/.env
	docker compose -f ./docker-compose.local.yml --env-file ./env/local/.env up

prod : # docker compose production
	docker compose -f ./docker-compose.production.yml --env-file ./env/production/.env up -d

refresh : # run container again
	make --ignore-errors _refresh

_refresh :
	docker stop test-stripe-web-1
	docker rm test-stripe-web-1
	docker rmi test-stripe-web
	docker volume rm test-stripe_app
	make up

rebuild : # run container again with clearing caches
	make --ignore-errors _rebuild

_rebuild :
	docker stop test-stripe-web-1
	docker rm test-stripe-web-1
	docker rmi test-stripe-web
	docker volume rm test-stripe_app
	docker builder prune -f
	make up

drop :
	make --ignore-errors _drop

_drop : # deletes the volume of database
	docker stop test-stripe-db-1
	docker rm test-stripe-db-1
	docker volume rm test-stripe_db
