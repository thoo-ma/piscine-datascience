import sqlalchemy
import pandas as pd


csv = '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2023_feb.csv'

# NOTE
# $: cat data_2023_feb.csv | wc -l
# 4156683
#
# $: tail -n 2 data_2023_feb.csv
# 2023-02-08 04:32:33 UTC,view,5870961,2.05,609248725,f16945fe-a3aa-e3e0-68a7-fbd6407198d4
# 2023-02-08 04:32:34 U
#
# Last line is truncated as you can see.
# However, pandas `read_csv()` ignore this line.
# And even more, surprisingly, remove this line from the csv file !
# Without any warning...

# NOTE Remove duplicates.
# Next exercise becomes useless.
def alternative_one(connection):
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


# NOTE Does not remove duplicates
def alternative_two(connection, tables):

    # Create `customers` table with the same columns as `data_2022_oct`.
    # The former is taken arbitratly within all `data_*` tables
    # (we suppose they all have commum column names and types.)
    stmt = sqlalchemy.text("CREATE TABLE customers AS SELECT * FROM data_2022_oct WHERE FALSE;")
    connection.execute(stmt)
    connection.commit()
    print('create table customers')

    # Copy each `data_*` table to `customers` (doesn't remove duplicates)
    for table in tables:
        stmt = sqlalchemy.text(f"SELECT COUNT(*) FROM {table};")
        rows = connection.execute(stmt).scalar()
        stmt = sqlalchemy.text(f"INSERT INTO customers SELECT * FROM {table};")
        connection.execute(stmt)
        connection.commit()
        print(f'copied {rows} rows from {table} to customers')


# NOTE Does not remove duplicates
# Take SO MUCH TIME
def alternative_three(connection, tables):

    # Create `customers` table with the same columns as `data_2022_oct`.
    # The former is taken arbitratly within all `data_*` tables
    # (we suppose they all have commum column names and types.)
    # Just to be sure we preserve types integrity from `data_` tables to `customers` tables.
    stmt = sqlalchemy.text("CREATE TABLE customers AS SELECT * FROM data_2022_oct WHERE FALSE;")
    connection.execute(stmt)
    connection.commit()
    print('create table customers')

    # Generators FTW
    for table, df in ((table, pd.read_sql_table(table, connection, parse_dates=['event_time'])) for table in tables):
        df.to_sql(name='customers', con=connection, if_exists='append', index=False)
        print(f'copied {df.shape[0]} rows from {table} to customers')


def main():

    # Step 1: open csv
    try:
        df = pd.read_csv(csv, on_bad_lines='warn', parse_dates=['event_time'])
        # NOTE Same rationale for droping duplicates than previous exercises.
        df.drop_duplicates(inplace=True)
    except Exception as e:
        print(e)
        exit()

    engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

    with engine.connect() as connection:

        # Step 2: create table
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

        # Step 3: fill table
        df.to_sql(name='data_2023_feb', con=connection, if_exists='append', index=False)
        print('fill table data_2023_feb')

        # Step 4: join tables
        tables = [
            'data_2022_oct',
            'data_2022_nov',
            'data_2022_dec',
            'data_2023_jan',
            'data_2023_feb'
        ]

        # alternative_one(connection)
        alternative_two(connection, tables)
        # alternative_three(connection, tables)


if __name__ == "__main__":
    main()