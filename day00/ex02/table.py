import sqlalchemy
import pandas as pd
import os


csv = '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_oct.csv'


# Step 1: open csv
try:
    df = pd.read_csv(csv, on_bad_lines='warn', parse_dates=['event_time'])
    # NOTE This is not asked by the subject.
    # (Even more, this is not recommended since we asked to remove duplicates
    # once all data_ tables have been merged into the customers one.)
    # We do it anyway because there is so much lines and compute
    # all those useless duplicated would be -- and has been -- very painful.
    # Even less painful, would be to remove duplicates from the file
    # directly, avoiding loading duplicated lines into the DataFrame.
    # GNU `sort` and `uniq` would do the trick.
    # However, this is more convient to just `drop_duplicates()`.
    df.drop_duplicates(inplace=True)
except Exception as e:
    print(e)
    exit()

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    # Step 2: create type
    stmt = sqlalchemy.text("CREATE TYPE event_type AS ENUM ('view', 'cart', 'remove_from_cart', 'purchase');")
    connection.execute(stmt)
    connection.commit()

    # Step 3: create table
    # TODO
    # https://stackoverflow.com/q/58220421
    # https://stackoverflow.com/q/68219690
    table = os.path.basename(csv).split('.')[0]
    stmt = sqlalchemy.text(f"""
        CREATE TABLE {table} (
            event_time TIMESTAMP,
            event_type event_type,
            product_id INTEGER,
            price REAL,
            user_id BIGINT,
            user_session VARCHAR(50));""")
    connection.execute(stmt)
    connection.commit()

    # Step 4: fill table
    df.to_sql(name=table, con=connection, if_exists='append', index=False)

    # Step 4 (alternative)
    # NOTE `csv` needs to be a valid path in the container filesystem
    # stmt = sqlalchemy.text(f"""
    #     COPY {table}(event_time, event_type, product_id, price, user_id, user_session)
    #     FROM '{csv}'
    #     DELIMITER ','
    #     CSV HEADER;""")
    # connection.execute(stmt)
    # connection.commit()
