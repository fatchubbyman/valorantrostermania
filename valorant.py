# systems that need to be in place:
# role finder: this basically looks at the most agents played by a player and assigns them with a role
# real tournament with a format and all the objects should be created and assigned to interact with each other
# twitter follower count which identifies the demand for the player
# player picker: a for loop will run 5 times for you to pick your player according to role and price

# you might be able to scrape the twitter followers using replace('M','00000000)

import random as rd
from bs4 import BeautifulSoup
import requests

class Player:
    
    def __init__(self,region,acs,kd,ign,country,prev,role,price,twitter_fllwrs):
        self.acs = acs
        self.kd = kd
        self.ign = ign
        self.country = country
        self.prev = prev
        self.role = role
        self.price = price
        self.twitter_fllwrs = twitter_fllwrs
        self.link = link

        
class Team:
    
    def __init__(self,name,region,matches= 0):
        self.metches = matches
        self.name = name
        self.region = region

# roles
duelists = ['jett','phoenix','iso','reyna','raze','yoru','neon','chamber']
sentinels = ['sage','killjoy','cypher','deadlock','vyse','chamber','viper']
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
    return role

# making every player an object
regions = ['APAC','EMEA',"Americas"]
region_tournaments = ['','/2005/champions-tour-2024-pacific-stage-2','/2094/champions-tour-2024-emea-stage-2']
for i in range(len(region_tournaments)):
    url = 'https://www.vlr.gg/event/stats' + region_tournaments[i]
    clickr = requests.get(url)
    soup = BeautifulSoup(clickr, 'lxml')
    players = soup.find_all('div', style = 'font-weight: 700; margin-bottom: 2px; width: 90px;' )
    for j in range(len(players)):
        tbody = soup.find('tbody')
        trs = tbody.find_all('tr')[j]   # every player has a tr
        stats = trs.find_all('span')
        acs = stats[1].text
        kd = stats[2].text
        prev = trs.find('div',class_ = 'stats-player-country').text
        agent_list = []
        agents = trs.find_all('img', class_ = 'mod-small')
        for k in range(len(agents)):
            agents[i].replace('<img class="mod-small" src="/img/vlr/game/agents/','')
            agents[i].replace('.png','')
            agent_list.append(agents[k])
        role_finder(agent_list[0],agent_list[1])
        link = trs.find('a')
        lnk = link.get('href')
        url = 'https://www.vlr.gg/' + lnk
        #twitter time
        player_clicked = requests.get(url).text
        soupy = BeautifulSoup(player_clicked,'lxml')
        country = soupy.find('div', class_ = 'ge-text-light').text
        twitter_tag = soupy.find('a')
        twitter_link = twitter_tag.get('href')
        twt_clicked = requests.get(twitter_link,'lxml')
        tsoup = BeautifulSoup(twitter_link,'lxml')
        followers = tsoup.find()
        region = regions[i]
        Player(ign=players[j].text,acs = acs,kd=kd,prev = prev,role=role,price=,twitter_fllwrs=,country=country,link=lnk)
# twitter follower work to be done here


    
        





