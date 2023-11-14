import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# TODO
# Subject here is too vague.
# It doesn't specify according to which metric users should be clusterized.
# It only says we should cluster 'customer types'.
# Indeed, we could cluster (types of) users according to:
# - the total value they spend
# - the type of items the buyed
# - the number of time they ordered
# - etc.
# Sounds we should arbitrary choose one of these metric to clusterize users.

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")
with engine.connect() as connection:
    df = pd.read_sql_table('customers', connection)
    print(df.columns)
    print(df.head())
