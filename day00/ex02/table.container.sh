#!/bin/bash

csv=(
    '/tmp/data_2022_oct.csv'
    '/tmp/data_2022_nov.csv'
    '/tmp/data_2022_dec.csv'
    '/tmp/data_2023_jan.csv'
)

psql -U trobin piscineds << END
    CREATE TYPE event_type AS ENUM ('view', 'cart', 'remove_from_cart', 'purchase');
END

for csv in ${csv[@]}
do
    file=$(basename ${csv} .csv)

    # create table
    psql -U trobin piscineds << END
    CREATE TABLE ${file} (
        event_time TIMESTAMP,
        event_type event_type,
        product_id INTEGER,
        price REAL,
        user_id BIGINT,
        user_session VARCHAR(50)
    );
END

    # upload csv
    psql -U trobin piscineds << END
    COPY ${file}(event_time, event_type, product_id, price, user_id, user_session)
    FROM '${csv}'
    DELIMITER ','
    CSV HEADER;
END
done