#encoding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import re

"""
# TODO:   Implement
# function: get_players_links_by_team(team_name) 
#   :param team_name: Nombre del equipo
#   :return: Lista con los nombre y links de los jugadores del equipo
# function: get_news_links_by_team(team_name) 
#   :param team_name: Nombre del equipo
#   :return: Lista con los nombre y links de las ultimas noticias
# function: get_latest_news()
#   :return: Lista de las ultimas noticias
# funcion: get_latest_news_by_team(team_name)
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

""" TESTS
if __name__ == "__main__":
    [names, links]=get_teams_links_and_names()
    for t,l in zip(names, links):
        print(t+"\n")
        print(l+"\n")

END TESTS """