import sqlalchemy
import pandas as pd


csv = '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/item/item.csv'

# Step 1: open csv
try:
    df = pd.read_csv(csv, on_bad_lines='warn')
    # NOTE Same rationale for droping duplicates than previous exercise.
    df.drop_duplicates(inplace=True)
except Exception as e:
    print(e)
    exit()

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    # Step 2: create table
    table = 'items'
    stmt = sqlalchemy.text(f"""
        CREATE TABLE {table} (
        product_id INTEGER,
        category_id BIGINT,
        category_code VARCHAR(50),
        brand VARCHAR(50));""")
    connection.execute(stmt)
    connection.commit()

    # Step 3: fill table
    df.to_sql(name=table, con=connection, if_exists='append', index=False)
