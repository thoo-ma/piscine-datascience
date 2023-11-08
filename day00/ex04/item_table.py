import sqlalchemy
import pandas as pd
import os


csv = '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/item/item.csv'

try:
    df = pd.read_csv(csv, on_bad_lines='warn')
except Exception as e:
    print(e)
    exit()

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    table = 'items'
    stmt = sqlalchemy.text(f"""
        CREATE TABLE {table} (
        product_id INTEGER,
        category_id BIGINT,
        category_code VARCHAR(50),
        brand VARCHAR(50));""")
    connection.execute(stmt)
    connection.commit()

    df.to_sql(name=table, con=connection, if_exists='append', index=False)
