import sqlalchemy
import pandas as pd


csv = '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2023_feb.csv'

try:
    df = pd.read_csv(csv, on_bad_lines='warn', parse_dates=['event_time'])
except Exception as e:
    print(e)
    exit()

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    # Create table
    stmt = sqlalchemy.text("""
        CREATE TABLE data_2023_feb (
            event_time TIMESTAMP,
            event_type event_type,
            product_id INTEGER,
            price REAL,
            user_id BIGINT,
            user_session VARCHAR(50));""")
    connection.execute(stmt)
    connection.commit()
    print('create table data_2023_feb')

    # Load and validate data
    # df = pd.read_csv(csv, on_bad_lines='warn', parse_dates=['event_time'])

    # print(df[df.isna().any(axis=1)])
    # df.dropna(inplace=True)

    # print('== before ==')
    # print(df.tail())
    # print(df.shape)

    # Last line buggy
    # Maybe a better solution with `date_format=` into `read.csv()`
    df = df[:-1]

    # print('== after ==')
    # print(df.tail())
    # print(df.shape)
    # print(df.dtypes)

    # Fill the new table
    # df.to_sql(name='data_2023_feb', con=connection, if_exists='append', index=False)
    # print('fill table data_2023_feb')

    # Join tables
    stmt = sqlalchemy.text("""
        CREATE TABLE customers
        AS
            SELECT * FROM data_2022_oct
                UNION
            SELECT * FROM data_2022_nov
                UNION
            SELECT * FROM data_2022_dec
                UNION
            SELECT * FROM data_2023_jan
                UNION
            SELECT * FROM data_2023_feb;
        """)
    connection.execute(stmt)
    connection.commit()
    print('create table customers')
