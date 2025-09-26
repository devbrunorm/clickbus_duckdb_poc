import duckdb

with duckdb.connect() as conn:
    print(conn.sql("SELECT * EXCLUDE id FROM read_csv_auto('./input/product.csv')").df())

    print(conn.sql("SELECT * REPLACE (id + 1 AS id) FROM read_csv_auto('./input/product.csv')").df())

    print(conn.sql("SELECT * RENAME (id AS new_id) FROM read_csv_auto('./input/product.csv')").df())

    print(conn.sql("SELECT * SIMILAR TO 'pr*' FROM read_csv_auto('./input/product.csv')").df())

    print(conn.sql("SELECT COLUMNS('^pr.*') FROM read_csv_auto('./input/product.csv')").df())

    print(conn.sql("SELECT TRY_CAST(id AS FLOAT) AS id_float FROM read_csv_auto('./input/product.csv')").df())