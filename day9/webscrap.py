# pip install requests
# pip install beautifulsoup4

import requests
import re
from bs4 import BeautifulSoup
url = "https://www.iplt20.com/stats/2019/most-runs"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', class_='table table--scroll-on-tablet top-players')

all_players = []
headers = []
flag = 0
for row in table.find_all('tr'):
    if flag == 0:
        columns = row.find_all('th')
        flag = 1
        for column in columns:
            d = column.get_text().strip()
            headers.append(d)
        all_players.append(headers)
    else:
        columns = row.find_all('td')
        data = []
        for column in columns:
            d = column.get_text().strip()
            d = re.sub(r"\n\s+"," ",d)
            data.append(d)
        all_players.append(data)

import csv
with open("iplScrap.csv","w",newline='') as file:
     writer = csv.writer(file)
     writer.writerows(all_players)
    
