# webscraping-movies
# Web Scraping Movies Project

This project uses Python to scrape data about the top 50 highly ranked films from a web page. The extracted data is saved into a CSV file and also stored in a SQLite database.

## Project Description

The goal of this project is to practice web scraping, data extraction, data storage, and basic SQL querying.

The program collects movie information including:

- Average Rank
- Film Title
- Year of Release

## Files in This Repository

- `webscraping_movies.py`  
  Scrapes the movie data from the website, creates a DataFrame, saves the data as a CSV file, and stores it in a SQLite database.

- `query_movies.py`  
  Connects to the SQLite database and runs SQL queries on the `Top_50` table.

- `top_50_films.csv`  
  Contains the extracted top 50 movie data.

- `.gitignore`  
  Prevents unnecessary files such as `Movies.db`, cache files, and Mac system files from being uploaded.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite3
- Git and GitHub

## How to Run the Project

First, install the required Python libraries:

```bash
## How to Run the Project

First, install the required Python libraries:

```bash
pip install requests pandas beautifulsoup4
```

Then run the web scraping script:

```bash
python3 webscraping_movies.py
```

To run SQL queries:

```bash
python3 query_movies.py
```

## Example SQL Queries

```sql
SELECT * FROM Top_50;
```

```sql
SELECT * FROM Top_50 LIMIT 10;
```

```sql
SELECT COUNT(*) FROM Top_50;
```

```sql
SELECT Film, Year FROM Top_50 WHERE Year > 2000;
```

## Output

The project creates:

- A CSV file named `top_50_films.csv`
- A SQLite database file named `Movies.db`

The database file is not uploaded to GitHub because it can be recreated by running the Python script.

## Author

Hedieh
