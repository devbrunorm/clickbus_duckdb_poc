import duckdb

with duckdb.connect(database='./storage/base.db') as conn:
    query_result = conn.execute("FROM read_csv_auto('./input/product.csv') AS product;").fetchall()
    print(query_result)
    conn.execute("CREATE TABLE IF NOT EXISTS product AS FROM read_csv_auto('./input/product.csv')")