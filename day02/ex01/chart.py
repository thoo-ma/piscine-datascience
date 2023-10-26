import sqlalchemy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    df = pd.read_sql_table('customers', connection, columns=['event_time', 'price', 'user_id'], parse_dates=['event_time'])
    print(df)

    dates = list(set([(date.year, date.month) for date in df['event_time'].dt.date]))
    dates.sort()
    print(dates)

    sales = [df.loc[df['event_time'].dt.month == month, 'price'].sum() for month in [date[1] for date in dates]]
    print(sales)

    # Total sales (bars)
    chart = plt.bar(range(len(dates)), sales, tick_label=[date[1] for date in dates])
    plt.xlabel('Months')
    plt.ylabel('Total sales in millions of USD')
    plt.yticks(list(range(0,int(max(sales))))[::10000000])
    plt.bar_label(chart, fmt='%d')
    plt.savefig('./day02/ex01/total_sales.png')
    # plt.show()

    # Total customers (simple plot)

    # dict: date -> nb_customers (work but too long...)
    # customers_per_day = { date: len(df.loc[df['event_time'].dt.date == date, 'user_id']) for date in np.unique(df['event_time'].dt.date) }
    # print(customers_per_day)

    df['dates'] = df['event_time'].dt.date
    df_customers_per_date = df[['dates', 'user_id']].groupby('dates', as_index=False).size()

    fig = plt.figure()
    foo = plt.plot_date(df_customers_per_date['dates'], df_customers_per_date['size'])
    plt.ylabel('Number of customers')
    plt.xticks()
    plt.savefig('./day02/ex01/total_customers.png')

    months = df['event_time'].dt.month.u

    # Average spend per customer (stackplot)
    # plt.figure()
    # plt.stackplot(dates, sales)
    # plt.ylabel('Average spend/customers in USD')
    # plt.savefig('./day02/ex01/average_spend.png')