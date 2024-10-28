#                                                             ideas/scrapped ideas
#select region
#select org
#have a rostermania, budget based, one import only
#then make a format like lock//in 2023
#game mechanics are a best of 5(duel vs. duel,sentinel vs. sentinel)
#winner wins
#you lose, you go home
#a csv file with all the top vct players will be in this and a for loop will run to make every player into an object
# top 10 players of your region of every role will be shown with their budget
# this project is a personal one to just practice web scraping for the first time and working with objects for the second time
import pandas as pd  
from bs4 import BeautifulSoup
import requests
url = 'https://www.vlr.gg/player/4095/skrossi/'
html_text = requests.get(url +'?timespan=all')
soup = BeautifulSoup(html_text.text, 'lxml')
name = soup.find('h2', class_='player-real-name ge-text-light').text.strip()
ign = soup.find('h1', class_='wf-title').text.strip()
most_played = soup.find('img', alt = 'jett')
img_tag = soup.find('img', alt='jett')
if img_tag:
    img_src = img_tag.get('alt')
    print(f'{img_src}')
else:
    print("Image not found")
country_checker = soup.find('div', class_='ge-text-light')
if country_checker:
    country = country_checker.get_text(strip=True)
else:
    country = "Country not found"
span = soup.find('span', style = 'white-space: nowrap;').text
print(span)

print(f'{name}\'s ign is {ign}')
print(country)


