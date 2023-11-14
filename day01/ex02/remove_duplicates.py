import sqlalchemy
import pandas as pd

# TODO USELESS (cf. day01/ex01/)

tables = [
    'data_2022_oct',
    'data_2022_nov',
    'data_2022_dec',
    'data_2023_jan',
    'data_2023_feb'
]

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    # dfs = [pd.read_sql_table(table, connection, parse_dates=['event_time']) for table in tables]
    # map(lambda df: print(df.shape), dfs)
    # df = pd.concat(dfs)
    # print(df.shape)

    total_before = 0
    total_after = 0
    for table in tables:
        df = pd.read_sql_table(table, connection, parse_dates=['event_time'])
        print(f'== {table} ==')
        print(f'before: {df.shape[0]} rows')
        total_before += df.shape[0]
        df.drop_duplicates(inplace=True)
        total_after += df.shape[0]
        print(f'after:  {df.shape[0]} rows')

    print(f'== total ==')
    print(f'before: {total_before}')
    print(f'after:  {total_after}')

    df = pd.read_sql_table('customers', connection, parse_dates=['event_time'])
    print(f'== customers ==')
    print(f'before: {df.shape[0]} rows')
    df.drop_duplicates(inplace=True)
    print(f'after:  {df.shape[0]} rows')


