import duckdb

with duckdb.connect(database='./storage/base.db') as conn:
    query_result = conn.execute("FROM product;").fetchall()
    print("Resgatando os dados do banco persistente")
    print(query_result)

    print("Convertendo a tabela em um DataFrame do Pandas")
    df = conn.execute("SELECT * FROM product;").df()
    print(df)

    print("Convertendo a tabela em um DataFrame do Polars")
    df = conn.execute("SELECT * FROM product;").pl()
    print(df)

    print("Convertendo a tabela em um DataFrame do Arrow")
    df = conn.execute("SELECT * FROM product;").arrow()
    print(df)