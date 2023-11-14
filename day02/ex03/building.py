import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt

def frequency(df):
    # Count the number of occurrences of each user_id
    print(df['user_id'].head())

    user_counts = df['user_id'].value_counts(sort=False)
    print(user_counts.head())

    # TODO
    user_counts = user_counts[user_counts <= 50]

    # exit()
    # Create a new figure and get the axes
    fig, ax = plt.subplots()

    # Create bins of size 50 from 0 to the maximum total price
    # TODO see subject: don't start from 0
    bins = range(0, 50, 10)

    # Plot histogram with bars on top of the grid
    ax.hist(user_counts, bins=bins, edgecolor='black', color='skyblue')

    # Set labels
    ax.set_xlabel('Number of Rows Indexed by User')
    ax.set_ylabel('Number of Users')

    # Disable scientific notation on y-axis
    ax.ticklabel_format(style='plain', axis='y')

    # Set x ticks
    plt.xticks(bins)

    # Set labels
    plt.xlabel('frequency')
    plt.ylabel('customers')

    # Show plot
    plt.show()

def value(df):
    total_price_per_user = df.groupby('user_id')['price'].sum()

    # TODO
    print(f'{total_price_per_user.shape[0]} rows')
    total_price_per_user = total_price_per_user[total_price_per_user <= 200]
    print(f'{total_price_per_user.shape[0]} rows')

    print(total_price_per_user.head())
    print(total_price_per_user.max())
    print(int(total_price_per_user.max()))

    # Create bins of size 50 from 0 to the maximum total price
    # bins = range(0, int(total_price_per_user.max()) + 50, 50)
    # TODO see subject: don't start from 0
    bins = range(0, 250, 50)

    # Set grey background
    # plt.figure(facecolor='grey')

    # Create a new figure and get the axes
    fig, ax = plt.subplots()

    # Set grey background
    # ax.set_facecolor('grey')
    # ax.set_facecolor('#F0F0F0')

    # Add grid with white lines
    # plt.grid(color='white')

    # Plot histogram
    plt.hist(total_price_per_user, bins=bins, edgecolor='black')
    # plt.hist(total_price_per_user, bins=bins, edgecolor='black', color='skyblue', zorder=3)

    # Set labels
    plt.xlabel('monetary value in A') # TODO
    plt.ylabel('customers')

    # Set x ticks
    plt.xticks(bins)

    # Disable scientific notation on y-axis
    plt.ticklabel_format(style='plain', axis='y')

    # Show plot
    plt.show()

def main():
    engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")
    with engine.connect() as connection:
        df = pd.read_sql_table('customers', connection, columns=['price', 'user_id'])
        # value(df)
        frequency(df)

if __name__ == '__main__':
    main()