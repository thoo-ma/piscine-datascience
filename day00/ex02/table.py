import sqlalchemy
import pandas as pd
import os


csv = '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_oct.csv'

try:
    df = pd.read_csv(csv, on_bad_lines='warn', parse_dates=['event_time'])
    # print(df.head())
    # print(df.shape)
    # print(df.columns)
    # print(df.dtypes)
except Exception as e:
    print(e)
    exit()

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    stmt = sqlalchemy.text("CREATE TYPE event_type AS ENUM ('view', 'cart', 'remove_from_cart', 'purchase');")
    connection.execute(stmt)
    connection.commit()

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

    df.to_sql(name=table, con=connection, if_exists='append', index=False)

    # For this solution the db need to access the csv file on the container filesystem
    # stmt = sqlalchemy.text(f"""
    #     COPY {table}(event_time, event_type, product_id, price, user_id, user_session)
    #     FROM '{csv}'
    #     DELIMITER ','
    #     CSV HEADER;""")
    # connection.execute(stmt)
    # connection.commit()
