# -*- coding: utf-8 -*-
"""
@author: corinamccullough
"""

import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt


url1 = "https://www.chiefs.com/team/players-roster/"
url2 = "https://www.philadelphiaeagles.com/team/players-roster/"


# Use BeautifulSpup to get the data from the web.
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'html.parser')

response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')


KC = pd.read_html(url1,match="Player")
PHI = pd.read_html(url2,match="Player")


# Turn the data retrieved from the websites into data frames.
KC = pd.DataFrame(KC[0])
PHI = pd.DataFrame(PHI[0])


# Create a 'Team' column so you can decifer which players are on each team when
# we merge the data frames
KC['Team'] = "Kansas City Chiefs"
PHI['Team'] = "Philadelphia Eagles"


print(KC.head())
print(PHI.head())

# Merge the data frames.
nfl = pd.concat([KC, PHI], axis=0)

# Save to excel
nfl.to_excel("nfl_web_scrape.xlsx")



# Let's make a quick graph
# Years od Experience
nfl_players_exp = nfl.groupby(["Exp","Team"], as_index = False).count()

# Height
nfl_players_ht = nfl.groupby(["HT","Team"], as_index = False).count()

# Years of Experience
import pandas as pd
import seaborn as sns

colors = ["#8B0000", "#388E8E"]
sns.set_palette(sns.color_palette(colors))

plt.figure(figsize=(12, 8))

# Plot
years = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']

sb23 = sns.barplot(data=nfl_players_exp, x="Exp", y="Player", hue="Team",
                   order = years)
sb23.set_title("Super Bowl LVII Players' Years of Experience")
sb23.legend(loc='upper right', title='Team')
sb23.set_xlabel("Years of Experience")
sb23.set_ylabel("Number of Players")

# Height

plt.figure(figsize=(12, 8))

sb_ht = sns.barplot(data = nfl_players_ht, x = "HT", y = "Player",
                    order = heights, color = "#8B0000", errwidth = 0)
sb_ht.set_title("Height of Players in Super Bowl LVII")
sb_ht.legend(loc='upper right', title='Team')
sb_ht.set_xlabel("Height (Ft-in)")
sb_ht.set_ylabel("Number of Players")











