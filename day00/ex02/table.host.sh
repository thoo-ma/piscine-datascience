#!/bin/bash

csv=(
  'day00/data/customer/data_2022_oct.csv'
  'day00/data/customer/data_2022_nov.csv'
  'day00/data/customer/data_2022_dec.csv'
  'day00/data/customer/data_2023_jan.csv'
)
container=piscine-datascience-db-1
script=day00/ex02/table.container.sh

for csv in ${csv[@]}
  do

  # Remove duplicates
  tail -n +2 ${csv} | sort | uniq > _tmp

  # Add back the header (would have been be sorted otherwise)
  (head -1 ${csv}; cat _tmp) > /tmp/foo

  rm _tmp

  # Copy the cleaned csv from host to container
  docker cp /tmp/foo ${container}:/tmp/$(basename ${csv})
done

docker cp ${script} ${container}:/tmp
docker exec ${container} bash /tmp/$(basename ${script})