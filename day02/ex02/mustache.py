import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:
    df = pd.read_sql_table('customers', connection, columns=['price', 'user_id'])

    print(f'count: {df["price"].count()}')
    print(f'mean: {df["price"].mean()}')
    print(f'std: {df["price"].std()}')
    print(f'min: {df["price"].min()}')
    print(f'max: {df["price"].max()}')
    print(f'50%: {df["price"].median()}')
    print(f'25%: {df["price"].quantile(0.25)}')
    print(f'75%  {df["price"].quantile(0.75)}')

    # global plot
    plt.boxplot(df['price'], vert=False)
    plt.yticks([])
    plt.xlabel('price')
    plt.show()
    # plt.savefig('./day02/ex02/plotbox.png')

    # just to zoom on the winker
    Q1 = df['price'].quantile(0.25)
    Q3 = df['price'].quantile(0.75)
    IQR = Q3 - Q1

    whisker_width = 1.5 * IQR
    lower_whisker = max(Q1 - whisker_width, df['price'].min())
    upper_whisker = min(Q3 + whisker_width, df['price'].max())

    plt.boxplot(df['price'], vert=False)
    plt.yticks([])
    plt.xlabel('price')
    plt.xlim([lower_whisker, upper_whisker])
    plt.show()
    # plt.savefig('./day02/ex02/plotbox_zoom.png')

    # average price per user
    # TODO result differ from subject
    average_price_per_user = df.groupby('user_id')['price'].mean()
    plt.boxplot(average_price_per_user, vert=False)
    plt.yticks([])
    plt.xlabel('average price per user')
    plt.show()
    # plt.savefig('./day02/ex02/average_per_user.png')