import sqlalchemy
import pandas as pd


csv = '/home/youngbenjaminhorne/42/piscine-datascience/subject/item/item.csv'

# Step 1: open csv
try:
    df = pd.read_csv(csv, on_bad_lines='warn')
    print(df.shape)
    # NOTE: Same rationale for droping duplicates than previous exercise.
    # However, remove duplicates here is more tricky.
    # See `test/duplicates.ipynb` for more explanations.
    df = df.groupby('product_id', as_index=False).first()
    print(df.shape)
except Exception as e:
    print(e)
    exit()

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    # Step 2: create table
    table = 'items'
    statement = sqlalchemy.text(f"""
        CREATE TABLE {table} (
        product_id INTEGER,
        category_id BIGINT,
        category_code VARCHAR(50),
        brand VARCHAR(50));""")
    connection.execute(statement)
    connection.commit()

    # Step 3: fill table
    df.to_sql(name=table, con=connection, if_exists='append', index=False)
