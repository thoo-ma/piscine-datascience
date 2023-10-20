#!/bin/bash

brands=$(awk -F, '{print $4}' day00/subject/item/item.csv | awk NF | sort | uniq)
category=$(awk -F, '{print $3}' day00/subject/item/item.csv | sed 's/\./\n/g' | awk NF | sort | uniq)

echo $brands
echo $brands | wc -w

echo $category
echo $category | wc -w

csv=day00/subject/item/item.csv
script=day00/ex04/items_table.container.sh
container=piscine-datascience-db-1

docker cp ${csv} ${container}:/tmp
docker cp ${script} ${container}:/tmp/
docker exec ${container} bash /tmp/$(basename ${script})