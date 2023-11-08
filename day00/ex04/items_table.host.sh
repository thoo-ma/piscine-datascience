#!/bin/bash

# brands=$(awk -F, '{print $4}' /sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/item/item.csv | awk NF | sort | uniq)
# category=$(awk -F, '{print $3}' /sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/item/item.csv | sed 's/\./\n/g' | awk NF | sort | uniq)

# echo $brands
# echo $brands | wc -w

# echo $category
# echo $category | wc -w

csv=/sgoinfre/goinfre/Perso/trobin/piscine-datascience/item/item.csv
script=day00/ex04/items_table.container.sh
container=piscine-datascience-db-1

tail -n +2 ${csv} | sort | uniq > _tmp
(head -1 ${csv}; cat _tmp) > /tmp/foo
rm _tmp

docker cp ${csv} ${container}:/tmp
docker cp ${script} ${container}:/tmp/
docker exec ${container} bash /tmp/$(basename ${script})