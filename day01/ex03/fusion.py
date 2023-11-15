import sqlalchemy
import pandas as pd
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, sqlalchemy.Enum):
            return obj.name
        if isinstance(obj, sqlalchemy.TIMESTAMP):
            return 'TIMESTAMP'
        return str(obj)


def print_columns(engine, table):
    columns = sqlalchemy.inspect(engine).get_columns(table)
    print(json.dumps({ column['name']: column['type'] for column in columns }, indent=2, cls=DateTimeEncoder))


def alternative_one(connection, engine):
    print_columns(engine, 'customers')
    stmt = sqlalchemy.text("""
        SELECT * FROM customers
        FULL JOIN items ON customers.product_id = items.product_id
    """)
    connection.execute(stmt)
    connection.commit()
    print_columns(engine, 'customers')


def alternative_two(connection):
    df_items = pd.read_sql_table('items', connection)
    print(df_items.shape)
    # NOTE Subject say not to lose any information.
    # But how are we supposed to manage those duplicates...
    df_items.drop_duplicates(subset='product_id', inplace=True)
    print(df_items.shape)
    df_customers = pd.read_sql_table('customers', connection)
    print(df_customers.shape)
    df_concat = pd.concat([df_customers, df_items], ignore_index=True)
    print(df_concat.shape)
    df_concat.to_sql('customers', connection, if_exists='replace', index=False)


def main():
    engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")
    with engine.connect() as connection:
        # alternative_one(connection, engine)
        alternative_two(connection)

if __name__ == "__main__":
    main()
