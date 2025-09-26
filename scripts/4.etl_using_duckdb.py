import duckdb

with duckdb.connect() as conn:
    conn.execute("COPY (FROM read_csv('./input/Consumo_horario_2024_05.csv')) TO './output/output.parquet';")