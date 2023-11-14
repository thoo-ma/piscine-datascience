import sqlalchemy
import json

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, sqlalchemy.Enum):
            return obj.name
        if isinstance(obj, sqlalchemy.TIMESTAMP):
            return 'TIMESTAMP'
        return str(obj)

def get_table_column_types(engine, table_name):
    columns = sqlalchemy.inspect(engine).get_columns(table_name)
    return { column['name']: column['type'] for column in columns }

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")
table_name = 'data_2022_oct'

column_types_dict = get_table_column_types(engine, table_name)

print(column_types_dict)
print(json.dumps(column_types_dict, indent=2, cls=DateTimeEncoder))
