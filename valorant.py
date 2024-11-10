# systems that need to be in place:
# role finder: this basically looks at the most agents played by a player and assigns them with a role
# real tournament with a format and all the objects should be created and assigned to interact with each other
# twitter follower count which identifies the demand for the player
# player picker: a for loop will run 5 times for you to pick your player according to role and price

# you might be able to scrape the twitter followers using replace('M','00000000)

import random as rd
from bs4 import BeautifulSoup
import requests
import time

def wait():
    for i in range(3):
        print('.')
        time.sleep(0.5)


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
        self.region = region

        
class Team:
    
    def __init__(self,name,region,matches= 0,purse = 300000):
        self.metches = matches
        self.name = name
        self.region = region
        self.purse = purse

# roles
duelists = ['jett','phoenix','iso','reyna','raze','yoru','neon','chamber']
sentinels = ['sage','killjoy','cypher','deadlock','vyse','chamber','viper']
controllers = ['viper','omen','brimstone','harbor','clove','astra']
initiators = ['sova','breach','fade','skye','gekko','kayo']

def teams_shower(region):
    if region.lower() == 'americas':
        for i in range(len(teams_na.keys())):
            print(teams_na.keys()[i])
    if region.lower() == 'apac':
        for i in range(len(teams_apac.keys())):
            print(teams_na.keys()[i])
    elif region.lower() == 'emea':
        for i in range(len(teams_emea.keys())):
            print(teams_emea.keys()[i])

def teams_picker(region,team_name):
    if region.lower() == 'americas':
        if team_name in teams_na.keys():
            teams_na['your team'] = teams_na.pop(team_name)
    if region.lower() == 'apac':
        if team_name in teams_apac.keys():
            teams_apac['your team'] = teams_apac.pop(team_name)
    elif region.lower() == 'emea':
        if team_name in teams_emea.keys():
            teams_emea['your team'] = teams_emea.pop(team_name)
      

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

def duelist_printer(region):
    if region.lower() == 'americas':
        for i in range(len(players_na.values())):
            if players_na.values()[i].role == 'duelist':
                print(f'{players_na.values()[i].name}\n{players_na.values()[i].acs}\n{players_na.values()[i].kd}\n{players_na.values()[i].prev}\n{players_na.values()[i].twitter_fllwrs}\n{players_na.values()[i].country}\n{players_na.values()[i].price}')
                time.sleep(2)
    if region.lower() == 'apac':
        for i in range(len(players_na.values())):
            if players_na.values()[i].role == 'duelist':
                print(f'{players_na.values()[i].name}\n{players_na.values()[i].acs}\n{players_na.values()[i].kd}\n{players_na.values()[i].prev}\n{players_na.values()[i].twitter_fllwrs}\n{players_na.values()[i].country}\n{players_na.values()[i].price}')
                time.sleep(2)
            print(teams_na.keys()[i])
    elif region.lower() == 'emea':
        for i in range(len(players_na.values())):
            if players_na.values()[i].role == 'duelist':
                print(f'{players_na.values()[i].name}\n{players_na.values()[i].acs}\n{players_na.values()[i].kd}\n{players_na.values()[i].prev}\n{players_na.values()[i].twitter_fllwrs}\n{players_na.values()[i].country}\n{players_na.values()[i].price}')
                time.sleep(2)
    



# sentinel_printer(region)
# smokes_printer(region)
# initiator_printer(region)
# flex_printer(region)

# making every player an object
regions = ["Americas",'APAC','EMEA']
region_tournaments = ['/2095/champions-tour-2024-americas-stage-2','/2005/champions-tour-2024-pacific-stage-2','/2094/champions-tour-2024-emea-stage-2']
duelist_players = []
sentinel_players = []
initiator_players = []
flex_players = []
smoke_players = []

players_na = {}
players_apac = {}
players_emea = {}

for i in range(len(region_tournaments)):
    url = 'https://www.vlr.gg/event/stats' + region_tournaments[i]
    clickr = requests.get(url)
    soup = BeautifulSoup(clickr.content, 'lxml')
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
        role = role_finder(agent_list[0],agent_list[1])    #returns a role
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
        player = Player(ign=players[j].text,acs = acs,kd=kd,prev = prev,role=role,price=,twitter_fllwrs=,country=country,link=lnk,region=region)
        if i == 0:
            players_na[player.name] = player
        elif i == 1:
            players_apac[player.name] = player
        elif i == 2:
            players_emea[player.name] = player
# twitter follower work to be done here


teams_na = {}                #team.name: object of the team
teams_apac = {}
teams_emea = {}
teams2 = [teams_na.keys(),teams_apac.keys(),teams_emea.keys()]                    #team names

region = input('What region would you like to represent?(Americas/APAC/EMEA) ')
for i in range(len(region_tournaments)):
    url = 'https://www.vlr.gg/event' + region_tournaments[i] + '/regular-season'
    teams = requests.get(url)
    soup = BeautifulSoup(teams.content,'lxml')
    teams_tag = soup.find('div',class_ = 'event-teams-container')
    teams = teams_tag.find_all('a',class_ = 'wf-module-item event-team-name')
    for j in range(len(teams)):
        team = Team(name=teams[j].text.strip(),region=regions[i])
        if team.region == 'Americas':
            teams_na[team.name] = team
        elif team.region == 'APAC':
            teams_apac[team.name] = team
        elif team.region == 'EMEA':
            teams_emea[team.name] = team

your_team = input(f'Which team do you want to play as in the {region} region')
teams_shower(region)
teams_picker(region,your_team)

duelist_printer(region)
duelist_pick = input('Who are you going to pick as your duelist? ')


sentinel_printer(region)
sneintel_pick = input('Who are you going to pick as your duelist? ')

smokes_printer(region)
smokes_pick = input('Who are you going to pick as your duelist? ')

initiator_printer(region)
initiator_pick = input('Who are you going to pick as your duelist? ')

flex_printer(region)
flex_pick = input('Who are you going to pick as your duelist? ')




