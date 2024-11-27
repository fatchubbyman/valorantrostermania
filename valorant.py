                                              #nested dictionaries of objects

import random as rd
from bs4 import BeautifulSoup
import requests
import time
import selenium

class Player:
    
    def __init__(self,acs,kd,ign,prev,role,href):
        self.acs = acs
        self.kd = kd    
        self.prev = prev
        self.role = role
        self.href = href
        self.ign = ign

class Team:

    def __init__(self,name,squad={}):
        self.name = name
        self.squad = squad

def wait():
    for i in range(3):
        print('.')
        time.sleep(0.4)

def price_maker(href):
    url = 'https://www.vlr.gg' + href
    rqsts = requests.get(url)
    soup = BeautifulSoup(rqsts.content,'lxml')
    a_tag = soup.find('a', style ='margin-top: 3px; display: block;')
    twitter = a_tag.get('href')
    twitter = twitter.replace('https://x.com','')
    social_blade = 'https://socialblade.com/twitter/user' + twitter
    rqsts = requests.get(social_blade)
    soup = BeautifulSoup(rqsts.content,'lxml')
    stats = soup.find('div', id = 'YouTubeUserTopInfoBlockTop')
    followers = stats.find('span', style = 'font-weight: bold;')


def role_maker(agents):
    duelists = ['neon','raze','jett','phoenix','yoru','iso','reyna','chamber']
    controllers = ['brimstone','clove','omen','astra','harbor']
    sentinels = ['killjoy','cypher','chamber','vyse','chamber','sage','deadlock','viper']
    initiators = ['kayo','gekko','sova','fade','breach','skye']
    maker = {'duelists':0,'controllers':0,'sentinels':0,'initiators':0}
    for agent in agents:
        if agent in duelists:
            maker['duelists'] += 1
        elif agent in controllers:
            maker['controllers'] += 1
        elif agent in sentinels:
            maker['sentinels'] += 1
        elif agent in initiators:
            maker['initiators'] += 1
    if maker['duelists'] == 1 or maker['sentinels'] == 1:
        if maker['controllers'] > 0 or maker['initiators'] > 0:
            return 'flex'
    else:
        if maker['duelists'] > len(agents)/2:
            return 'duelist'
        elif maker['controllers'] > len(agents)/2:
            return 'controller'
        elif maker['initiators'] > len(agents)/2:
            return 'initiator'
        elif maker['sentinels'] > len(agents)/2:
            return 'sentinel'

players = {}                                           # (player.name: Player)
teams = {}                                            # (team.name: Team)
#automating teams for the rest of the 2 regions
def region_maker(links,players,teams):
    for link in links:
        rqsts = requests.get(link)
        soup = BeautifulSoup(rqsts.content,'lxml')
        teamsx = soup.find('div', class_ = 'event-teams-container')
        teams_tags = teamsx.find_all('div', class_ = 'wf-card event-team')
        for team in teams_tags:
            a_tag = team.find('a', class_ = 'wf-module-item event-team-name')
            teams[a_tag.text.strip()] = Team(name = a_tag.text.strip(),squad={})
            stats_link = link.replace('/event','/event/stats')
            stats_link = stats_link.replace('/regular-season','')
        rqsts = requests.get(stats_link)
        soup = BeautifulSoup(rqsts.content,'lxml')
        trs = soup.find_all('tr')
        for tr in trs:
            agents = []
            ign = tr.find('div', style = 'font-weight: 700; margin-bottom: 2px; width: 90px;').text.strip()
            data = tr.find_all('td')
            acs = float(data[4].text.strip())
            kd = float(data[5].text.strip())
            # finding roles 
            agents = tr.find('td', class_ = 'mod-agents')
            img_tags = agents.find_all('img')
            for img_tag in img_tags:
                agent_src = img_tag.get('src')
                agent_name = agent_src.replace('/img/vlr/game/agents/','')
                agents.append(agent_name.replace('.png',''))
            role = role_maker(agents)
            prev = tr.find('div', class_ = 'stats-player-country').text.strip()
            #href
            href_tag = tr.find('a')
            if href_tag:
                href = href_tag.get('href')
            players[ign] = Player(kd=kd,acs=acs,href=href,prev=prev,role=role,ign=ign)


links = ['https://www.vlr.gg/event/2094/champions-tour-2024-emea-stage-2/regular-season','https://www.vlr.gg/event/2005/champions-tour-2024-pacific-stage-2/regular-season','https://www.vlr.gg/event/2095/champions-tour-2024-americas-stage-2/regular-season']
wait()
region_select = input('What region would you like to represent? (emea,apac,americas)')
if region_select == 'emea':
    region = links.pop(0)
elif region_select == 'apac':
    region = links.pop(1)
else:
    region = links.pop(2)
# your own region process
class MyPlayer(Player):
    def __init__(self, acs, kd, ign, prev, role, href,price):
        super().__init__(acs, kd, ign, prev, role, href)
        self.price = price

class MyTeam(Team):
    def __init__(self, name, squad={},matches = 0):
        super().__init__(name, squad)
        self.matches = matches

rqsts = requests.get(region)
soup = BeautifulSoup(rqsts.content,'lxml')
# display teams and then select a team and make the others into team objects
team_body = soup.find('div', class_ = 'event-teams-container')
teams_for_display = team_body.find_all('a',class_ = 'wf-module-item event-team-name')
for i in range(len(teams_for_display)):
    print(f'{i+1} {teams_for_display[i].text.strip()}')
    print('.')
team_choice = input('Which team would you like to play as? (enter the team number)')
your_team = MyTeam(name = teams_for_display[team_choice].text.strip())
for team in teams_for_display:
    if team.text.strip() is not your_team.name:
        teams[team.text.strip()] = Team(name= team.text.strip())
stats_link = region.replace('/event','/event/stats')
stats_link = stats_link.replace('/regular-season','')
rqsts = requests.get(stats_link)
soup = BeautifulSoup(rqsts,'lxml')
trs = soup.find_all('tr')
for tr in trs:
    agents = []
    ign = tr.find('div', style = 'font-weight: 700; margin-bottom: 2px; width: 90px;').text.strip()
    data = tr.find_all('td')
    acs = float(data[4].text.strip())
    kd = float(data[5].text.strip())
    # finding roles 
    agents = tr.find('td', class_ = 'mod-agents')
    img_tags = agents.find_all('img')
    for img_tag in img_tags:
        agent_src = img_tag.get('src')
        agent_name = agent_src.replace('/img/vlr/game/agents/','')
        agents.append(agent_name.replace('.png',''))
    role = role_maker(agents)
    prev = tr.find('div', class_ = 'stats-player-country').text.strip()
    #href
    href_tag = tr.find('a')
    if href_tag:
         href = href_tag.get('href')
    price = price_maker(href)
    players[ign] = MyPlayer(kd=kd,acs=acs,href=href,prev=prev,role=role,ign=ign,price=price) 

#picking up a duelist, and displaying
for key,value in players.items():
    a  = 1
    if value.role == 'duelist':
        print(f'{a}. {value.ign}')
        print(value.price)
        print(value.acs)
        print(value.kd)
        print(value.prev)
        print(value.role)
        a += 1
        wait()

duelist_pick = input('Select the player no. ')
your_team.squad['duelist'] = 









for key,value in teams.items():
    for i in range(5):
        random_player_key = rd.choice(list(players.keys()))
        random_player_object = players.pop(random_player_key)
        value.squad[random_player_key] = random_player_object


