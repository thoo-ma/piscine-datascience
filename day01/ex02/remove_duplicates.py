import sqlalchemy
import pandas as pd

# NOTE USELESS (cf. day01/ex01/)
# NOTE None of the alternatives below can be executd. They all take too much time.

# NOTE Memory consumption too high (at least on my laptop).
# Table is too big, script gets killed.
def alternative_one(connection):
    df = pd.read_sql_table('customers', connection, parse_dates=['event_time'])
    print(f'before: {df.shape[0]} rows')
    df.drop_duplicates(inplace=True)
    print(f'after:  {df.shape[0]} rows')
    df.to_sql(name='customers', con=connection, if_exists='replace', index=False)


# NOTE This take SO MUCH TIME.
# Actually don't know if it will finish one day.
# At this point customers table is around 20M lines.
# Don't even know if it works actually...
def alternative_two(connection):
    stmt = sqlalchemy.text("SELECT COUNT(*) FROM customers;")
    rows = connection.execute(stmt).scalar()
    print(f'before: {rows} rows')

    stmt = sqlalchemy.text("""
    WITH duplicates AS (
        SELECT MIN(ctid) as ctid
        FROM customers
        GROUP BY event_time, event_type, product_id, price, user_id, user_session
        HAVING COUNT(*) > 1
    )
    DELETE FROM customers
    WHERE ctid NOT IN (SELECT ctid FROM duplicates);
    """)
    connection.execute(stmt)
    connection.commit()

    stmt = sqlalchemy.text("SELECT COUNT(*) FROM customers;")
    rows = connection.execute(stmt).scalar()
    print(f'after:  {rows} rows')


# TODO test it
def alternative_three(connection):

    def get_table_rows(connection, tablename):
        stmt = sqlalchemy.text(f"SELECT COUNT(*) FROM {tablename};")
        return connection.execute(stmt).scalar()

    stmt = sqlalchemy.text("""
    CREATE TABLE customers_temp AS
    SELECT DISTINCT * FROM customers;
    """)
    connection.execute(stmt)

    total_rows_before = get_table_rows(connection, 'customers')
    total_rows_after = get_table_rows(connection, 'customers_temp')

    print(f'before: {total_rows_before} rows')
    print(f'after:  {total_rows_after} rows')

    connection.execute(sqlalchemy.text("DROP TABLE customers;"))
    connection.execute(sqlalchemy.text("ALTER TABLE customers_temp RENAME TO customers;"))
    connection.commit()

def main():
    engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

    with engine.connect() as connection:
        # alternative_one(connection)
        # alternative_two(connection)
        alternative_three(connection)

if __name__ == "__main__":
    main()