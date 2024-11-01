import random as rd
from bs4 import BeautifulSoup
import requests

class Player:
    
    def __init__(self,region,acs,kd,ign,country,prev,role,price,twitter_fllwrs):
        self.region = region
        self.acs = acs
        self.kd = kd
        self.ign = ign
        self.name = name
        self.country = country
        self.prev = prev
        self.role = role
        self.price = price
        self.twitter_fllwrs = twitter_fllwrs

class Team:
    
    def __init__(self,region,name,cash,matches):
        self.region = region
        self.cash = cash
        self.name = name
        self.matches = matches

# roles
duelists = ['jett','phoenix','iso','reyna','raze','yoru','neon']
sentinels = ['sage','killjoy','cypher','deadlock','vyse','chamber']
controllers = ['viper','omen','brimstone','harbor','clove','astra']
initiators = ['sova','breach','fade','skye','gekko','kayo']

def role_finder(main1,main2):
    if main1 and main2 in duelists:
        role = 'duelist'
    elif main1 and main2 in sentinels:
        role = 'sentinel'
    elif main1 and main2 in controllers:
        role = 'controller'
    elif main1 and main2 in initiators:
        role = 'initiator'
    else:
        role = 'flex'
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
players = soup.find_all('a', href=lambda href: href and '/player/' in href)
for i in range(len(players)):
    links_emea.append(players[i]['href'])

links_apac = []
url = 'https://www.vlr.gg/event/stats/2005/champions-tour-2024-pacific-stage-2'
apac = requests.get(url).text
soup = BeautifulSoup(apac, 'lxml')
players = soup.find_all('a', href=lambda href: href and '/player/' in href)    #Here, lambda href: creates a function that takes one argument, href, representing the value of the href attribute of each <a> tag that soup.find examines.
for i in range(len(players)):
    links_apac.append(players[i]['href'])


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
    
# player pool
for i in range(len(links_apac)):
    url = 'https://www.vlr.gg/' + links_apac[i] + '?timespan=all'
    apac_players = requests.get(url).text
    soup = BeautifulSoup(apac_players,'lxml')
    #attributes
    country = soup.find('div', class_ = 'ge-text-light').text.strip()
    ign = soup.find('h1', class_ = 'wf-title').text
    img_tag = soup.find('img')
    main = img_tag['alt']
    acs = soup.find_all('td', class_ = 'mod-right')[1].text
    kd = soup.find_all('td', class_ = 'mod-right')[2].text
    name = soup.find('h2',class_ = 'player-real-name ge-text-light').text.strip()
    prev = soup.find('div',style = 'font-weight: 500;').text.strip()
    link = soup.find('a',href= True)            # twitter followers proportionate to price/interest of orgs
    if link and 'x.com' in link['href']:
        xlink = link['href']
    twitter_get = requests.get(xlink)
    souperino = BeautifulSoup(twitter_get,'lxml')
    followers = souperino.find('span',class_ = 'css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3').text.split()
    k = 1000
    m = 1000000
    if int(followers) > m:
        pass
    elif m > int(followers) > 500000:
        pass
    elif 10000 > int(followers) > 0:
        pass
    elif 500000 > int(followers) > 10000:
        pass
    pacific = Player(region = 'APAC',role=,acs=,kd=,country=country,ign = ign,prev=prev,)

# systems that need to be in place:
# role finder: this basically looks at the most agents played by a player and assigns them with a role
# real tournament with a format and all the objects should be created and assigned to interact with each other
# twitter follower count which identifies the demand for the player
# player picker: a for loop will run for