import random as rd
from bs4 import BeautifulSoup
import requests
import time

class Player:
    
    def __init__(self,acs,kd,ign,prev,role,href):
        self.acs = acs
        self.kd = kd    
        self.prev = prev
        self.role = role
        self.href = href
        self.ign = ign

class Team:

    def __init__(self,name,players={}):
        self.name = name
        self.players = players

def wait():
    for i in range(3):
        print('.')
        time.sleep(0.4)

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

players = {}                                       # (player.name: Player)
teams = {}                                         # (team.name: Team)
#automating teams for the rest of the 2 regions
def region_maker(links,players):
    for link in links:
        rqsts = requests.get(link)
        soup = BeautifulSoup(rqsts.content,'lxml')
        teams = soup.find('div', class_ = 'event-teams-container')
        teams_tags = teams.find_all('div', class_ = 'wf-card event-team')
        for team in teams_tags:
            a_tag = team.find('a', class_ = 'wf-module-item event-team-name')
            teams[a_tag.text.strip()] = Team(name = a_tag.text.strip())
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
stats = {'emea':'https://www.vlr.gg/event/stats/2094/champions-tour-2024-emea-stage-2','apac':'https://www.vlr.gg/event/stats/2005/champions-tour-2024-pacific-stage-2','americas':'https://www.vlr.gg/event/stats/2095/champions-tour-2024-americas-stage-2'}
wait()
region_select = input('What region would you like to represent? (emea,apac,americas)')
if region_select == 'emea':
    region = links.pop(0)
elif region_select == 'apac':
    region = links.pop(1)
else:
    region = links.pop(2)
# your own region process
