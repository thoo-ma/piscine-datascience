#!//bin/bash

csv=day01/data/data_2023_feb.csv
script=day01/ex01/customers_table.container.sh
container=piscine-datascience-db-1

docker cp ${csv} ${container}:/tmp
docker cp ${script} ${container}:/tmp
docker exec ${container} bash /tmp/$(basename ${script})
