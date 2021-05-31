dev-docker-build:
	docker compose -f docker-compose.yaml build --no-cache
dev-docker-up:
	docker compose -f docker-compose.yaml up
dev-docker-db-bash:
	docker compose run --rm db
dev-docker-web-bash:
	docker compose run --rm web
dev-docker-down:
	docker compose -f docker-compose.yaml down