all:	;	docker compose --file docker-compose.yml up --detac

it:		;	docker compose --file docker-compose.yml exec db bash

.PHONY: all it