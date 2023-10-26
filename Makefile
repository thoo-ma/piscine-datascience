all:	;	docker compose --file docker-compose.yml up --detach

it:		;	docker compose --file docker-compose.yml exec db bash

.PHONY: all it