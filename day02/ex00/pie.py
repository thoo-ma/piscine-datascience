import sqlalchemy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    df = pd.read_sql_table('customers', connection, columns=['event_type'])
    print(df)

    labels, sizes = np.unique(df, return_counts=True)
    print(labels)
    print(sizes)

    _sum = sum(sizes)
    _sizes = [s / _sum * 100 for s in sizes]
    print(_sizes)

    plt.pie(_sizes, labels=labels, autopct='%.1f%%')
    # plt.show()
    plt.savefig('./day02/ex00/pie.png')
