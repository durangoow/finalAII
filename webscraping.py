#encoding: utf-8

import random
from bs4 import BeautifulSoup
import urllib.request
import re

"""
#
# TODO: get_players_links_by_team(team_name) 
#   :param team_name: Nombre del equipo
#   :return: Dos listas con los nombres y links de los jugadores del equipo
# TODO: get_news_links_by_team(team_name) 
#   :param team_name: Nombre del equipo
#   :return: Lista con los nombre y links de las ultimas noticias
# TODO: get_latest_news()
#   :return: Lista de las ultimas noticias
# TODO: get_latest_news_by_team(team_name)
#   :param team_name: Nombre del equipo
    :return: Lista de las ultimas noticias del equipo
"""

def get_teams_links_and_names():
    """
    :return: Lista con los nombres de los equipos y su link
    """
    names=[]
    links=[]
    link = "https://www.futbolfantasy.com"
    html = urllib.request.urlopen(link)
    s = BeautifulSoup(html, "lxml")
    teams=s.find("div", class_="teams liga").find_all("a")
    for t in teams:
        names.append(t.get("data-tooltip"))
        links.append(t.get("href"))
    return(names, links)

def get_players_links_by_team(team_name):
    """
    :param team_name: Nombre del equipo / Name of the team
    :return: Dos listas con los nombres y links de los jugadores del equipo / Two list, with players names and players links
    """
    names=[]
    links=[]
    link = "https://www.futbolfantasy.com/laliga/equipos/"+team_name+"/plantilla"
    html = urllib.request.urlopen(link)
    s = BeautifulSoup(html, "lxml")
    players=s.find_all("a", class_="jugador")
    for p in players:
        #FIXME: Combinar las dos expresiones regulares
        name=re.sub(r"\d+\. |\s+$",'',p.text)
        names.append(re.sub(r"^\s+","",name))
    for n in names:
        print(n)


if __name__ == "__main__":

#TESTS
    teams_test=["betis", "sevilla"]
    get_players_links_by_team(teams_test[1])

    """
    [names, links]=get_teams_links_and_names()
    dic=dict(zip(names, links))
    print(dic["Betis"])
    for t,l in zip(names, links):
        print(t+"\n")
        print(l+"\n")
"""
#END TESTS 