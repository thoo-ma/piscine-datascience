import sqlalchemy

engine = sqlalchemy.create_engine("postgresql://trobin:mysecretpassword@localhost:5432/piscineds")

with engine.connect() as connection:
    connection.execute(sqlalchemy.text("""
        CREATE TABLE customers_tmp
        AS (
            SELECT
                c.event_time,
                c.event_type,
                c.product_id,
                i.category_id,
                i.category_code,
                i.brand,
                c.price,
                c.user_id,
                c.user_session
            FROM customers c
            FULL JOIN items i ON c.product_id = i.product_id
        );
    """))
    connection.execute(sqlalchemy.text("DROP TABLE customers;"))
    connection.execute(sqlalchemy.text("ALTER TABLE customers_tmp RENAME TO customers;"))
    connection.commit()
