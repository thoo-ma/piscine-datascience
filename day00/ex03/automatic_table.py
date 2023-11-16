import sqlalchemy
import pandas as pd
import os


csvs = [
    '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_nov.csv',
    '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_dec.csv',
    '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2023_jan.csv'
]

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    for csv in csvs:

        # Step 1: open csv
        try:
            df = pd.read_csv(csv, on_bad_lines='warn', parse_dates=['event_time'])
            print(f'open {csv}')
            # NOTE Same rationale for droping duplicates than previous exercise.
            df.drop_duplicates(inplace=True)
        except Exception as e:
            print(e)
            continue

        # Step 2: create table
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
        print(f'create table {table}')

        # Step 3: fill table
        df.to_sql(name=table, con=connection, if_exists='append', index=False)
        print(f'fill table {table}')

