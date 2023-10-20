from sqlalchemy import create_engine, Table
from sqlalchemy.orm import Session
# import sqlalchemy

engine = create_engine('postgresql://trobin:mysecretpassword@localhost:5432/piscineds', echo=True)
print(engine)

session = Session(engine)
print(session)

table = Table('items', metadata)
print(table)
