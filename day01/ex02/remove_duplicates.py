import sqlalchemy
import pandas as pd

# NOTE USELESS (cf. day01/ex01/)

# NOTE memory consumption too high (at least on my laptop...)
def alternative_one(connection):
    df = pd.read_sql_table('customers', connection, parse_dates=['event_time'])
    print(f'before: {df.shape[0]} rows')
    df.drop_duplicates(inplace=True)
    print(f'after:  {df.shape[0]} rows')
    df.to_sql(name='customers', con=connection, if_exists='replace', index=False)

# NOTE This take SO MUCH TIME.
# Actually don't know if it will finish one day.
# At this point customers table is 20M lines.
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

def main():
    engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

    with engine.connect() as connection:
        # alternative_one(connection)
        # alternative_two(connection)
        pass

if __name__ == "__main__":
    main()