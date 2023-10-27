all:	;	docker compose --file docker-compose.yml up --detach

db:		;	docker compose --file docker-compose.yml up --detach db

it:		;	docker compose --file docker-compose.yml exec db bash

.PHONY: all db it