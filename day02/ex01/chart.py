import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:

    df = pd.read_sql_table('customers', connection, columns=['event_time', 'price', 'user_id'], parse_dates=['event_time'])
    print(df)

    dates = list(set([(date.year, date.month) for date in df['event_time'].dt.date]))
    dates.sort()
    print(dates)

    sales = [df.loc[df['event_time'].dt.month == month, 'price'].sum() for month in [date[1] for date in dates]]
    print(sales)

    # Plot 1: Total sales (bars)
    chart = plt.bar(range(len(dates)), sales, tick_label=[date[1] for date in dates])
    chart = plt.bar(range(len(dates)), sales)
    plt.xlabel('Months')
    plt.ylabel('Total sales in millions of USD')
    plt.yticks(list(range(0,int(max(sales))))[::10000000])
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.bar_label(chart, fmt='%d')
    plt.savefig('./day02/ex01/total_sales.png')

    # Plot 2: Total customers (simple plot)
    df['dates'] = df['event_time'].dt.date
    # df.drop_duplicates(subset=['dates', 'user_id'], inplace=True)
    df_customers_per_date = df[['dates', 'user_id']].groupby('dates', as_index=False).size()
    fig = plt.figure()
    foo = plt.plot_date(df_customers_per_date['dates'], df_customers_per_date['size'], '-')
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.ylabel('Number of customers')
    plt.savefig('./day02/ex01/total_customers.png')

    # Plot 3: Average spend per customer (stackplot)
    average_spend_per_day = df.groupby(['dates', 'user_id'])['price'].mean().groupby('dates').mean().reset_index()
    plt.figure()
    plt.fill_between(average_spend_per_day['dates'], average_spend_per_day['price'])
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.ylabel('Average spend/customers in USD')
    plt.savefig('./day02/ex01/average_spend.png')