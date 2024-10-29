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
        self.matches = matches

links_na = []
url = 'https://www.vlr.gg/event/stats/2095/champions-tour-2024-americas-stage-2'
na = requests.get(url).text
soup = BeautifulSoup(na,'lxml')
players = soup.find_all('a', href=lambda href: href and '/player/' in href)
for i in range(len(players)):
    links_na.append(players[i]['href'])

links_emea = []
url = 'https://www.vlr.gg/event/stats/2094/champions-tour-2024-emea-stage-2'
emea = requests.get(url).text
soup = BeautifulSoup(emea, 'lxml')
players = soup.find_all('a', href=lambda href: href and '/player/' in href)    #Here, lambda href: creates a function that takes one argument, href, representing the value of the href attribute of each <a> tag that soup.find examines.
for i in range(len(players)):
    links_emea.append(players[i]['href'])

links_apac = []
url = 'https://www.vlr.gg/event/stats/2005/champions-tour-2024-pacific-stage-2'
apac = requests.get(url).text
soup = BeautifulSoup(apac, 'lxml')
players = soup.find_all('a', href=lambda href: href and '/player/' in href)    #Here, lambda href: creates a function that takes one argument, href, representing the value of the href attribute of each <a> tag that soup.find examines.
for i in range(len(players)):
    links_apac.append(players[i]['href'])

links_china = []
url = 'https://www.vlr.gg/event/stats/2096/champions-tour-2024-china-stage-2'
china = requests.get(url).text
soup = BeautifulSoup(china, 'lxml')
players = soup.find_all('a',href = lambda href: href and '/player/'in href)
for i in range(len(players)):
    links_china.append(players[i]['href'])

#teams

url = 'https://www.vlr.gg/event/1188/champions-tour-2023-lock-in-s-o-paulo/bracket-stage'
teams_list = []
teams = requests.get(url).text
soup = BeautifulSoup(teams,'lxml')
team = soup.find_all('a', class_ = 'wf-module-item event-team-name')
for i in range(len(team)):
    print(team[i].text.strip())
    teams_list.append(team[i].text.strip())

# team pool

url = 'https://www.vlr.gg/event/2095/champions-tour-2024-americas-stage-2/regular-season'
na_teams = requests.get(url).text
soup = BeautifulSoup(na_teams,'lxml')
na_team = soup.find_all('a',class_ = 'wf-module-item event-team-name')
for i in range(len(na_team)):
    na_team = Team(name = na_team[i].text.strip(),cash=250000,luck=0,matches=0)
    na_team[i].text.strip() = na_team
url = 'https://www.vlr.gg/event/2005/champions-tour-2024-pacific-stage-2/regular-season'
apac_teams = requests.get(url).text
soup = BeautifulSoup(apac_teams,'lxml')
apac_team = soup.find_all('a',class_ = 'wf-module-item event-team-name')
for i in range(len(apac_team)):
    apac_team = Team(name = apac_team[i].text.strip(),cash=250000,luck=0,matches=0)
    apac_team[i].text.strip() = apac_team
url = 'https://www.vlr.gg/event/2094/champions-tour-2024-emea-stage-2/regular-season'
emea_teams = requests.get(url).text
soup = BeautifulSoup(emea_teams,'lxml')
emea_team = soup.find_all('a',class_ = 'wf-module-item event-team-name')
for i in range(len(emea_team)):
    emea_team = Team(name = emea_team[i].text.strip(),cash=250000,luck=0,matches=0)
    emea_team[i].text.strip() = emea_team
url = 'https://www.vlr.gg/event/2094/champions-tour-2024-emea-stage-2/regular-season'
emea_teams = requests.get(url).text
soup = BeautifulSoup(emea_teams,'lxml')
emea_team = soup.find_all('a',class_ = 'wf-module-item event-team-name')
for i in range(len(emea_team)):
    emea_team = Team(name = emea_team[i].text.strip(),cash=250000,luck=0,matches=0)
    emea_team[i].text.strip() = emea_team
    
# player pool
for i in range(len(links_apac)):
    url = 'https://www.vlr.gg/' + links_apac[i] + '?timespan=all'
    apac_players = requests.get(url).text
    soup = BeautifulSoup(apac_players,'lxml')
    ign = soup.find('h1', class_ = 'wf-title').text
    img_tag = soup.find('img')
    main = img_tag['alt']
    acs = soup.find_all('td', class_ = 'mod-right')[1]
    kd = soup.find_all('td', class_ = 'mod-right')[2]
    name = soup.find()
    prev = soup.find()
    role = soup.find()
    price = 0                           # twitter followers proportionate to price/interest of orgs
    

    
