from bs4 import BeautifulSoup
import pandas as pd
import requests

years = [1930, 1934, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

home, score, away, Year = [], [], [], []

for year in years: 
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    req = requests.get(web)

    soup = BeautifulSoup(req.text, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    
    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())
        Year.append(year)
    
matches_df = pd.DataFrame({'Home':home,
                        'Score':score,
                        'Away':away,
                        'Year':Year})

# print(matches_df)


matches_df.to_excel('football_all_matches.xlsx',index=False)

web = f'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'

req = requests.get(web)

soup = BeautifulSoup(req.text, 'lxml')

matches = soup.find_all('div', class_='footballbox')

home2,score2,away2 = [],[],[]    
for match in matches:
    home2.append(match.find('th', class_='fhome').get_text())
    score2.append(match.find('th', class_='fscore').get_text())
    away2.append(match.find('th', class_='faway').get_text())
    
matches2022_df = pd.DataFrame({'Home':home2,
                        'Score':score2,
                        'Away':away2,})
matches2022_df['Year'] = 2022
matches2022_df.to_excel('WC2022.xlsx',index=False)