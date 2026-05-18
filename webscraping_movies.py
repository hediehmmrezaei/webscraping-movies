import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# Save files in the same folder as this Python script
base_dir = Path(__file__).parent
db_name = base_dir / 'Movies.db'
table_name = 'Top_50'
csv_path = base_dir / 'top_50_films.csv'

df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count < 50:
        col = row.find_all('td')
        if len(col) != 0:
            data_dict = {
                "Average Rank": col[0].get_text(strip=True),
                "Film": col[1].get_text(strip=True),
                "Year": col[2].get_text(strip=True)
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

print(df)

df.to_csv(csv_path, index=False)

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

print("CSV file saved at:", csv_path)
print("Database file saved at:", db_name)


import sqlite3
sql_connection = sqlite3.connect(db_name)

df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

sql_connection = sqlite3.connect(db_name)

import sqlite3
import pandas as pd

conn = sqlite3.connect("/Users/hedieh/Desktop/Web scraping/Movies.db")

query = "SELECT * FROM Top_50 LIMIT 10"

df = pd.read_sql(query, conn)

print(df)

conn.close()