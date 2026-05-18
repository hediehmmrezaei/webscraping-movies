import sqlite3
import pandas as pd

db_path = "/Users/hedieh/Desktop/Web scraping/Movies.db"

conn = sqlite3.connect(db_path)

query = "SELECT * FROM Top_50 LIMIT 10"

df = pd.read_sql(query, conn)

print(df)

conn.close()