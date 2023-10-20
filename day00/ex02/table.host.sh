#!/bin/bash

src_dest=/tmp/
container=piscine-datascience-db-1
csv=(
  'day00/subject/customer/data_2022_oct.csv'
  'day00/subject/customer/data_2022_nov.csv'
  'day00/subject/customer/data_2022_dec.csv'
  'day00/subject/customer/data_2023_jan.csv'
)

for csv in ${csv[@]}
do docker cp ${csv} ${container}:${src_dest}
done

docker cp day00/ex02/table.container.sh ${container}:${src_dest}
docker exec ${container} bash ${src_dest}table.container.sh

# script=day00/ex02/table.container.sh
# docker cp ${script} ${container}:/tmp
# docker exec ${container} bash /tmp/$(basename ${script})