#!/bin/bash

script=day01/ex03/fusion.container.sh
container=piscine-datascience-db-1

docker cp ${script} ${container}:/tmp
docker exec ${container} bash /tmp/$(basename ${script})