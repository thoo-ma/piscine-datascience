import sqlalchemy
import pandas as pd

# TODO
def print_columns(engine, table):
    columns = sqlalchemy.inspect(engine).get_columns(table)
    return { column['name']: column['type'] for column in columns }

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    print(print_columns(engine, 'customers'))

    stmt = sqlalchemy.text("""
        SELECT * FROM customers
        FULL JOIN items ON customers.product_id = items.product_id
    """)
    connection.execute(stmt)
    connection.commit()

    print(print_columns(engine, 'customers'))

    df_items = pd.read_sql_table('items', connection)
    print(df_items.head())
    print(df_items.shape)

    # Subject say not to lose any information
    # BUT how are we supposed to manage those duplicates...
    df_items.drop_duplicates(subset='product_id', inplace=True)
    print(df_items.head())
    print(df_items.shape)

    df_customers = pd.read_sql_table('customers', connection)
    print(df_customers.head())
    print(df_customers.shape)

    df_concat = pd.concat([df_customers, df_items], ignore_index=True)
    print(df_concat.head())
    print(df_concat.shape)

    print_columns(engine, 'customers')
    df_concat.to_sql('customers', connection, if_exists='replace', index=False)
    print(pd.read_sql_table('customers', connection))

