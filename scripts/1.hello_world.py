import duckdb

with duckdb.connect(database=':memory:') as conn:
    result = conn.execute("SELECT 'Hello World'").fetchall()
    print(result)