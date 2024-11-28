                                              #nested dictionaries of objects
import random as rd
from bs4 import BeautifulSoup
import requests
import time
import os

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

def follower_retriever(url,name):
    folder_name = '/Users/jatin/Documents/python/python projects/valorant2025/twitters'
    file_name = f'{name}.html'
    file_path = os.path.join(folder_name, file_name)
    os.makedirs(folder_name, exist_ok=True)
    response = requests.get(url)
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file,'lxml')
        div_tag = soup.find('div', class_ = 'css-175oi2r r-13awgt0 r-18u37iz r-1w6e6rj')
        a_tag = div_tag.find('a', class_ = 'css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-1loqt21')
        followers = a_tag.find('span', class_ = 'css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3').text.strip()
        return followers

def wait():
    for i in range(2):
        print('.')
        time.sleep(0.4)

def convert_to_int(value: str) -> int:
    suffixes = {'K': 10**3, 'M': 10**6, 'B': 10**9}
    number, suffix = value[:-1], value[-1].upper()
    if suffix in suffixes:
        return int(float(number) * suffixes[suffix])
    else:
        return int(number)

def price_maker(href:str):
    url = 'https://www.vlr.gg' + href
    rqsts = requests.get(url)
    soup = BeautifulSoup(rqsts.content,'lxml')
    name = soup.find('h1', class_ = 'wf-title').text.strip()
    a_tag = soup.find('a', style ='margin-top: 3px; display: block;')
    twitter = a_tag.get('href')
    followers = follower_retriever(twitter,name)
    followers = convert_to_int(followers)
    if followers > 100000:
        price = 100000
    elif 40000 > followers > 5000:
        price = 20000
    elif 100000 > followers > 40000:
        price = 50000
    elif followers < 5000:
        price = 10000
    return price


def role_maker(agents:list):
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
def region_maker(links:str,players:dict,teams:dict):
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
    def __init__(self, acs, kd, ign, prev, role, href,price=0):
        super().__init__(acs, kd, ign, prev, role, href)
        self.price = price

class MyTeam(Team):
    def __init__(self, name, squad={},matches = 0,wallet = 300000):
        super().__init__(name, squad)
        self.matches = matches
        self.wallet = wallet

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
    price = price_maker(href=href)
    players[ign] = MyPlayer(kd=kd,acs=acs,href=href,prev=prev,role=role,ign=ign,price=price) 

#picking up a duelist, and displaying
for key,value in players.items():
    a  = 1
    if value.role == 'duelist':
        print(f'{a}. {value.ign}')
        print('price: $',value.price)
        print('acs: ',value.acs)
        print('kd: ',value.kd)
        print('Previously with ',value.prev)
        print('Role: ',value.role)
        a += 1
        wait()
print('You have ${wallet} in your bank')
#picking up a sentinel, and displaying
#picking up a initiator, and displaying
#picking up a controller, and displaying
#picking up a flex, and displaying


region_maker(links=links,players=players,teams=teams)
for key,value in teams.items():
    for i in range(5):
        random_player_key = rd.choice(list(players.keys()))
        random_player_object = players.pop(random_player_key)
        value.squad[random_player_key] = random_player_object


