#!/bin/bash

# Array of PostgreSQL table names
tables=(
    "data_2022_oct.csv"
    "data_2022_nov.csv"
    "data_2022_dec.csv"
    "data_2023_jan.csv"
    "data_2023_feb.csv"
)

# Loop over each table and count the number of rows
for table in "${tables[@]}"
do
    # Use psql to execute a count query for each table
    row_count=$(psql -U trobin -d piscineds -t -c "SELECT COUNT(*) FROM $table")

    # Print the result
    echo "Table $table has $row_count rows."
done
