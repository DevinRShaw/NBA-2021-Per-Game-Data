import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# create a list of stat names to use as input into dataframe creation 
header = soup.find("thead")
stats = []

for cell in header.find_all("th"):
  stats.append(cell.text)



# this is creating a list of lists, each inner list contains player stats
table = soup.find("tbody")

data = []
i = 0
for row in table.find_all("tr"): #list of each player row 
  if i % 20 != 0 or i == 0:
    player = []
    for cell in row.find_all(["th", "td"]): #lsit of each attribute 
        player.append(cell.text) 
    data.append(player) #appends list of player attributes
  i += 1



# fastest method to create dataframe is to create list of lists and add the columns as part of the funciton like so 
df = pd.DataFrame(data, columns=stats)
filtered_df = df.drop(["Rk"], axis=1) #remove alphabetical index
display(df)

df = df.drop_duplicates(subset=['Player', 'Rk'])
df = df.drop(26) #removes stray junk row 

# Save the cleaned data to a CSV file
df.to_csv("nba_2021_per_game.csv", index=False)

# Print the first 5 rows of the DataFrame}
print(df.head())
