#!/bin/bash

# create table
psql -U trobin piscineds << END
CREATE TABLE items (
    product_id INTEGER,
    category_id BIGINT,
    category_code VARCHAR(50),
    brand VARCHAR(50)
);
END

# upload csv
psql -U trobin piscineds << END
    COPY items(product_id, category_id, category_code, brand)
    FROM '/tmp/item.csv'
    DELIMITER ','
    CSV HEADER;
END