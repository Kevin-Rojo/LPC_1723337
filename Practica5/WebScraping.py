import requests
from bs4 import BeautifulSoup as bs

def stats_lol(reg: str, sumonner_name: str) -> list:
    sumonner_name = sumonner_name.replace(" ","+")
    url = "https://"+reg+".op.gg/summoner/userName="+ sumonner_name
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    name = soup.find("span",class_="Name")
    rank = soup.find("div",class_="TierRank")
    ratio = soup.find("span",class_="winratio")
    champs = soup.find_all("div",class_="ChampionBox Ranked")
    #champions_stats = [name, kda, win_rate]
    champions_stats = []
    print("Invocador: " + name.string)
    print("Division: " + rank.string)
    print("Procentaje de Victoria: " + ratio.string)
    print("Campeones resientes:")
    for i in range(5):
        champion_name = champs[i].find("div", class_="Face")
        champion_kda = champs[i].find("span", class_="KDA")
        print(champion_name['title'])
        print(champion_kda.string)
        print()



stats_lol("lan","Pan Espacial")