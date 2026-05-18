# Web Scraping Movies Project

This project uses Python to scrape data about the top 50 highly ranked films from a web page. The extracted data is saved into a CSV file and also stored in a SQLite database.

## Project Description

The goal of this project is to practice web scraping, data extraction, data storage, and basic SQL querying.

The program collects movie information including:

- Average Rank
- Film Title
- Year of Release

## Web Scraping Process

This project uses web scraping to automatically collect movie data from a webpage instead of copying it manually.

The script first sends a request to the webpage using the `requests` library:

```python
html_page = requests.get(url).text
```

This downloads the HTML content of the webpage.

Then, the HTML page is parsed using `BeautifulSoup`:

```python
data = BeautifulSoup(html_page, 'html.parser')
```

BeautifulSoup converts the HTML into a structured format so Python can search through the page.

The movie data is stored inside HTML table rows. The script finds the table body using:

```python
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')
```

After that, the script loops through the rows and extracts the columns:

```python
col = row.find_all('td')
```

Each row contains movie information such as:

- Average Rank
- Film Title
- Year

The extracted values are placed into a dictionary:

```python
data_dict = {
    "Average Rank": col[0].get_text(strip=True),
    "Film": col[1].get_text(strip=True),
    "Year": col[2].get_text(strip=True)
}
```

Then each dictionary is converted into a pandas DataFrame row and added to the main DataFrame.

The loop stops after collecting the first 50 movies:

```python
if count < 50:
```

Finally, the collected data is saved into:

- a CSV file: `top_50_films.csv`
- a SQLite database table: `Top_50`

This makes the scraped data easier to store, view, and query using SQL.

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

Show all records from the table:

```sql
SELECT * FROM Top_50;
```

Show only the first 10 records:

```sql
SELECT * FROM Top_50 LIMIT 10;
```

Count the total number of records:

```sql
SELECT COUNT(*) FROM Top_50;
```

Show films released after the year 2000:

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

The project creates:

- A CSV file named `top_50_films.csv`
- A SQLite database file named `Movies.db`

The database file is not uploaded to GitHub because it can be recreated by running the Python script.

## What I Learned

Through this project, I practiced:

- Sending HTTP requests using Python
- Parsing HTML using BeautifulSoup
- Extracting table data from a webpage
- Storing scraped data in a pandas DataFrame
- Saving data into a CSV file
- Creating a SQLite database
- Running SQL queries on the extracted data
- Uploading a project to GitHub

## Author

Hedieh
