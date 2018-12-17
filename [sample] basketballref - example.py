import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import string
import datetime
import time

def player_info():

    players = []
    base_url = 'http://www.basketball-reference.com/players/'

    for letter in string.ascii_lowercase:
        page_request = requests.get(base_url + letter)
        soup = BeautifulSoup(page_request.text, 'html.parser')

        table = soup.find('table')

        # Testing if data is coming through..
        # print(table)

        if table:
            table_body = table.find('tbody')

            for row in table_body.findAll('tr'):

                # print(row)
                player_url = row.find('a')
                player_names = player_url.text
                player_pages = player_url['href']

                print(player_url)
                print(player_names)
                print(player_pages)

#                 cells = row.findAll('td')
#                 active_from = int(cells[0].text)
#                 active_to = int(cells[1].text)
#                 position = cells[2].text
#                 height = cells[3].text
#                 weight = cells[4].text
#                 birth_date = cells[5].text
#                 college = cells[6].text
#
#                 player_entry = {'url': player_pages,
#                                 'name': player_names,
#                                 'active_from': active_from,
#                                 'active_to': active_to,
#                                 'position': position,
#                                 'college': college,
#                                 'height': height,
#                                 'weight': weight,
#                                 'birth_date': birth_date}
#
#                 players.append(player_entry)
#
#     return pd.DataFrame(players)
#
# players_general_info = player_info()
print(player_info())
# print(players_general_info.head())
