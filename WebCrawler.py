import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://oceanofgames.com/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        sasha = BeautifulSoup(plain_text, 'html.parser')
        for link in sasha.find_all('a', {'rel': 'bookmark'}):
            href = link.get('href')
            item_tile = link.string
            print(href)
            print(item_tile)
            get_single_game_data(href)
        page += 1


# This is to get data from each individual game title
def get_single_game_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    sasha = BeautifulSoup(plain_text, 'html.parser')
    for game_name in sasha.find_all('h1', {'class': 'title'}):
        print(game_name.string)
    '''for links in sasha.find_all('a'):  #This code is to get all the links present in the game
        href = links.get('href')
        print(href)'''
    '''for sash in sasha.find_all('p'):   #For all paragraph headers
        print(sash.string)'''


trade_spider(7)
