#!//bin/bash

csv=(
  'day00/subject/customer/data_2022_oct.csv'
  'day00/subject/customer/data_2022_nov.csv'
  'day00/subject/customer/data_2022_dec.csv'
  'day00/subject/customer/data_2023_jan.csv'
  'day01/subject/customer/data_2023_feb.csv'
)

csv=day01/subject/customer/data_2023_feb.csv
script=day01/ex01/customers_table.container.sh

# docker cp ${csv} ${container}:/tmp
# docker cp ${script} ${container}:/tmp
# docker exec ${container} bash /tmp/$(basename ${script})

# comm -12 <(sort ${csv[0]}) <(sort ${csv[1]})
