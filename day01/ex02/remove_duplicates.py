import sqlalchemy
import pandas as pd

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

    for table in tables:
        df = pd.read_sql_table(table, connection, parse_dates=['event_time'])
        print(table, df.shape)

    # df = pd.read_sql_table('customers', connection, parse_dates=['event_time'])
    # print(df.head())
    # print(df.shape)

    # df.drop_duplicates(inplace=True)
    # print(df.head())
    # print(df.shape)

    # labels, sizes = np.unique(df, return_counts=True)
    # print(labels)
    # print(sizes)

    # _sum = sum(sizes)
    # _sizes = [s / _sum * 100 for s in sizes]
    # print(_sizes)

    # plt.pie(_sizes, labels=labels, autopct='%.1f%%')
    # # plt.show()
    # plt.savefig('./day02/ex00/pie.png')

