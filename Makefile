dev-docker-build:
	docker compose -f docker-compose.yaml build
dev-docker-up:
	docker compose -f docker-compose.yaml up
dev-docker-db-bash:
	docker compose run db bash
dev-docker-down:
	docker compose -f docker-compose.yaml down