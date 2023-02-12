# NBA 2021 Per Game Data

This script takes user input on year and stat type then retrieves NBA data from the website [basketball-reference.com](https://www.basketball-reference.com/leagues/NBA_{year}_{stat_type}.html) and saves it as a cleaned csv file. The data includes player statistics such as player name, rank, games played, points per game, etc. Meant to allow for faster workflow of analyzing NBA datasets.

## Dependencies
The following libraries are used in this script:
- `requests`
- `bs4 (BeautifulSoup)`
- `pandas`

## Retrieving Data
The data is retrieved from the URL `https://www.basketball-reference.com/leagues/NBA_2021_per_game.html` using the `requests` library. The `BeautifulSoup` library is then used to parse the HTML data and extract the required information.

## Data Cleaning
A list of stat names is created from the header of the HTML table and used as columns for the Pandas dataframe. The player data is then extracted from the HTML table and added as rows to the dataframe. Duplicate rows are removed using the `drop_duplicates` method, which keeps only the first occurrence of each row.

## Saving Data
The cleaned data is saved to a CSV file named `nba_2021_per_game.csv` using the `to_csv` method of the Pandas dataframe.


