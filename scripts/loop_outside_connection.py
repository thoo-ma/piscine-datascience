from sqlalchemy import create_engine, MetaData, Table, func
from memory_profiler import profile

username = "trobin"
password = "mysecretpassword"
host = "localhost:5432"
database = "piscineds"
tables = [
    "data_2022_oct",
    "data_2022_nov",
    "data_2022_dec",
    "data_2023_jan",
    "data_2023_feb"
]

engine = create_engine(f"postgresql://{username}:{password}@{host}/{database}")
metadata = MetaData()

@profile
def main():
    for table_name in tables:
        table = Table(table_name, metadata, autoload_with=engine)
        with engine.connect() as connection:
            row_count = connection.execute(func.count().select().select_from(table)).scalar()
            print(f"Table {table_name} has {row_count} rows.")

if __name__ == "__main__":
    main()
