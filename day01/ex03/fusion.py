import sqlalchemy
import pandas as pd

# engine = sqlalchemy.create_engine("postgresql+psycopg://trobin:mysecretpassword@localhost:5432/piscineds")
engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    df_items = pd.read_sql_table('items', connection)
    print(df_items)

    # Subject say not to lose any information
    # BUT how are we supposed to manage those duplicates...
    df_items.drop_duplicates(subset='product_id', inplace=True)
    print(df_items)

    df_customers = pd.read_sql_table('customers', connection)
    print(df_customers)

    df_concat = pd.concat([df_customers, df_items], ignore_index=True)
    print(df_concat)

    df_concat.to_sql('customers', connection, if_exists='replace', index=False)
    print(pd.read_sql_table('customers', connection))

    # df_foo = pd.read_sql_table('foo', connection)
    # df_bar = pd.read_sql_table('bar', connection)
    # df_baz = pd.concat([df_foo, df_bar], ignore_index=True)

    # print(df_foo)
    # print(df_bar)
    # print(df_baz)

    # df_baz.to_sql('baz', connection, if_exists='replace', index=False)

    # print(pd.read_sql_table('baz', connection))
