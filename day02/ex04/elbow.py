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
# Moreover, it doesn't specify in which dimensions the clusters elements lives.
# Examples we ave above are one dimension spaces. But forbusiness logic,
# two or more dimensions might be relevant.
# More than being vague, the subject could be qualified as nonsensical.
# Indeed, depending on what data we looking at, the optimal number of clusters
# might vary. Hence, as the subject seems to insinuate to the beginner in the
# field we are, there is no generic 'optimal number of clusters to make'.

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")
with engine.connect() as connection:
    df = pd.read_sql_table('customers', connection)
    print(df.columns)
    print(df.head())
