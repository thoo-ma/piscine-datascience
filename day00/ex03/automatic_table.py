import sqlalchemy
import pandas as pd
import os


csvs = [
    '/home/youngbenjaminhorne/42/piscine-datascience/subject/customer/data_2022_nov.csv',
    '/home/youngbenjaminhorne/42/piscine-datascience/subject/customer/data_2022_dec.csv',
    '/home/youngbenjaminhorne/42/piscine-datascience/subject/customer/data_2023_jan.csv'
]

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    for csv in csvs:

        # Step 1: create table
        table = os.path.basename(csv).split('.')[0]
        statement = sqlalchemy.text(f"""
            CREATE TABLE {table} (
                event_time TIMESTAMPTZ,
                event_type event_type,
                product_id INTEGER,
                price REAL,
                user_id BIGINT,
                user_session VARCHAR(50));""")
        connection.execute(statement)
        connection.commit()
        print(f'created table {table}')

        # Step 2: fill table
        chunksize = 100000
        for chunk in pd.read_csv(csv, chunksize=chunksize, on_bad_lines='warn', parse_dates=['event_time']):
            chunk.drop_duplicates(inplace=True) # NOTE: is it necessary at this point
            chunk.to_sql(name=table, con=connection, if_exists='append', index=False)
            print(f'added chunk (100k rows) to table {table}')
        print(f'filled table {table}')

