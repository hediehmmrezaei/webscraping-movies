# Web Scraping Movies Project

This project uses Python to scrape data about the top 50 highly ranked films from a webpage. The extracted data is saved into a CSV file and also stored in a SQLite database.

## Project Description

The goal of this project is to practice:

- Web scraping
- HTML parsing
- Data extraction
- Data storage
- Basic SQL querying
- Uploading a project to GitHub

The program collects the following movie information:

- Average Rank
- Film Title
- Year of Release

## Web Scraping Process

The script first imports the required Python libraries:

```python
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path
```

The `requests` library is used to download the webpage, and `BeautifulSoup` is used to parse the HTML content.

The webpage URL is stored in the variable `url`:

```python
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
```

The script sends a GET request to the webpage and stores the HTML content:

```python
html_page = requests.get(url).text
```

Then, BeautifulSoup parses the HTML page:

```python
data = BeautifulSoup(html_page, 'html.parser')
```

BeautifulSoup converts the HTML into a structured format so Python can search through the page.

The movie data is stored inside an HTML table. The script finds the table body and table rows:

```python
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')
```

The program loops through the rows and extracts the table cells:

```python
col = row.find_all('td')
```

Each row contains movie information. The extracted data is stored in a dictionary:

```python
data_dict = {
    "Average Rank": col[0].get_text(strip=True),
    "Film": col[1].get_text(strip=True),
    "Year": col[2].get_text(strip=True)
}
```

The dictionary is converted into a pandas DataFrame row and added to the main DataFrame.

The loop stops after collecting the first 50 movies:

```python
if count < 50:
```

## Saving the Data

After scraping the data, the script saves it into a CSV file:

```python
df.to_csv(csv_path, index=False)
```

The file created is:

```text
top_50_films.csv
```

The script also saves the same data into a SQLite database:

```python
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
```

The database file created is:

```text
Movies.db
```

Inside the database, the table name is:

```text
Top_50
```

## SQL Query Example

The script can run SQL queries on the database.

For example, this query counts how many records are in the table:

```python
query = f"SELECT COUNT(*) FROM {table_name}"
result = pd.read_sql(query, conn)
```

The SQL query is:

```sql
SELECT COUNT(*) FROM Top_50;
```

This confirms that the movie data was successfully saved into the SQLite database.

## Files in This Repository

- `webscraping_movies.py`  
  Main Python script. It scrapes movie data, saves it as a CSV file, and stores it in a SQLite database.

- `query_movies.py`  
  Python file used to practice SQL queries on the SQLite database.

- `top_50_films.csv`  
  CSV file containing the extracted top 50 movie data.

- `.gitignore`  
  Prevents unnecessary files from being uploaded to GitHub.

## Files Not Uploaded

The file `Movies.db` is not uploaded to GitHub because it is a generated database file. It can be recreated by running the Python script.

The `.gitignore` file prevents it from being uploaded.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite3
- Git
- GitHub

## How to Run the Project

Install the required Python libraries:

```bash
pip install requests pandas beautifulsoup4
```

Run the main script:

```bash
python3 webscraping_movies.py
```

Run the SQL query file:

```bash
python3 query_movies.py
```

## Example SQL Queries

Show all records:

```sql
SELECT * FROM Top_50;
```

Show the first 10 records:

```sql
SELECT * FROM Top_50 LIMIT 10;
```

Count all records:

```sql
SELECT COUNT(*) FROM Top_50;
```

Show films released after 2000:

```sql
SELECT Film, Year FROM Top_50 WHERE Year > 2000;
```

Sort films from newest to oldest:

```sql
SELECT * FROM Top_50 ORDER BY Year DESC;
```

Sort films by average rank:

```sql
SELECT * FROM Top_50 ORDER BY "Average Rank" ASC;
```

## Output

When the script runs successfully, it creates:

- `top_50_films.csv`
- `Movies.db`

It also prints the scraped movie data and the saved file locations in the terminal.

## What I Learned

Through this project, I learned how to:

- Send HTTP requests using Python
- Parse HTML using BeautifulSoup
- Extract table data from a webpage
- Store data in a pandas DataFrame
- Save data into a CSV file
- Create a SQLite database
- Save a DataFrame into a SQL table
- Run SQL queries using Python
- Use Git and GitHub to upload a project

## Author

Hedieh
