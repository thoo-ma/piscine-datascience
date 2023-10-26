#!/bin/bash

tables=(
  'data_2022_oct'
  'data_2022_nov'
  'data_2022_dec'
  'data_2023_jan'
  'data_2023_feb'
)

# Create table
psql -U trobin piscineds << END
  CREATE TABLE ${tables[4]} (
    event_time TIMESTAMP,
    event_type event_type,
    product_id INTEGER,
    price REAL,
    user_id BIGINT,
    user_session VARCHAR(50)
  );
END

# Fill table
  psql -U trobin piscineds << END
  COPY ${tables[4]}(event_time, event_type, product_id, price, user_id, user_session)
  FROM '/tmp/data_2023_feb.csv'
  DELIMITER ','
  CSV HEADER;
END

# Union tables
psql -U trobin piscineds << END
  CREATE TABLE customers
  AS
    SELECT * FROM ${tables[0]}
      UNION
    SELECT * FROM ${tables[1]}
      UNION
    SELECT * FROM ${tables[2]}
      UNION
    SELECT * FROM ${tables[3]}
      UNION
    SELECT * FROM ${tables[4]};
END
