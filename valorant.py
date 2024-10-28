#                                                             ideas/scrapped ideas
#select region
#select org
#have a rostermania, budget based, one import only
#then make a format like lock//in 2023
#game mechanics are a best of 5(duel vs. duel,sentinel vs. sentinel)
#winner wins
#you lose, you go home
#a csv file with all the top vct players with their vlr profiles will be in this and a for loop will run to make every player into an object
# top 10 players of your region of every role will be shown with their budget
# this project is a personal one to just practice web scraping for the first time and working with objects for the second time
# americas: https://www.vlr.gg/event/stats/2095/champions-tour-2024-americas-stage-2
# EMEA: https://www.vlr.gg/event/stats/2094/champions-tour-2024-emea-stage-2
# APAC: https://www.vlr.gg/event/stats/2005/champions-tour-2024-pacific-stage-2
# CHINA: https://www.vlr.gg/event/stats/2096/champions-tour-2024-china-stage-2
# pick 5 players according to budget and then make a LOCK//IN format and every team will get players randomly depending upon their role
# every role gets a 1v1 and then the winner out of the best of 5 is chosen, the others are automatically done and your games will be watched slowly
import random as rd
import pandas as pd  
from bs4 import BeautifulSoup
import requests
# url = 'https://www.vlr.gg/player/4095/skrossi/'
# html_text = requests.get(url +'?timespan=all')
# soup = BeautifulSoup(html_text.text, 'lxml')
# name = soup.find('h2', class_='player-real-name ge-text-light').text.strip()
# ign = soup.find('h1', class_='wf-title').text.strip()
# most_played = soup.find('img', alt = 'jett')
# img_tag = soup.find('img', alt='jett')
# if img_tag:
#     img_src = img_tag.get('alt')
#     print(f'{img_src}')
# else:
#     print("Image not found")
# country_checker = soup.find('div', class_='ge-text-light')
# if country_checker:
#     country = country_checker.get_text(strip=True).title()
# else:
#     country = "Country not found"
# span = soup.find('span', style = 'white-space: nowrap;').text
# print(span)

# print(f'{name}\'s ign is {ign}')
# print(country)
# make a matches system
class Player:
    
    def __init__(self,region,main,acs,kd,ign,name,country,prev,role,price):
        self.region = region
        self.main = main
        self.acs = acs
        self.kd = kd
        self.ign = ign
        self.name = name
        self.country = country
        self.prev = prev
        self.role = role
        self.price = price

class Team:
    
    def __init__(self,region,name,cash,luck,matches):
        self.region = region
        self.cash = cash
        self.name = name
        self.luck = luck
        self.matches = matches

links_na = []
url = 'https://www.vlr.gg/event/stats/2095/champions-tour-2024-americas-stage-2'
na = requests.get(url).text
soup = BeautifulSoup(na,'lxml')
player = soup.find_all('a', href=lambda href: href and '/player/' in href)
for i in range(58):
    print(player[i]['href'])
    links_na.append(player[i]['href'])

links_emea = []
url = 'https://www.vlr.gg/event/stats/2094/champions-tour-2024-emea-stage-2'
emea = requests.get(url).text
soup = BeautifulSoup(emea, 'lxml')
player = soup.find_all('a', href=lambda href: href and '/player/' in href)    #Here, lambda href: creates a function that takes one argument, href, representing the value of the href attribute of each <a> tag that soup.find examines.
for i in range(56):
    print(player[i]['href'])
    links_emea.append(player[i]['href'])

links_apac = []
url = 'https://www.vlr.gg/event/stats/2005/champions-tour-2024-pacific-stage-2'
apac = requests.get(url).text
soup = BeautifulSoup(apac, 'lxml')
player = soup.find_all('a', href=lambda href: href and '/player/' in href)    #Here, lambda href: creates a function that takes one argument, href, representing the value of the href attribute of each <a> tag that soup.find examines.
for i in range(55):
    print(player[i]['href'])
    links_apac.append(player[i]['href'])


        


