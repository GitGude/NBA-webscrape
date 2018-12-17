import requests
from bs4 import BeautifulSoup
import pandas as pd
import string
import month_loop

# # 2018 Stat urls
# list = {'NBA_2018_games-october.html',
#         'NBA_2018_games-november.html',
#         'NBA_2018_games-december.html',
#         'NBA_2018_games-january.html''
#         'NBA_2018_games-february.html',
#         'NBA_2018_games-march.html'
# g = 'NBA_2018_games-april.html'
# h = 'NBA_2018_games-may.html'
# i = 'NBA_2018_games-june.html'
#
# # 2019 Stat urls
# j = 'NBA_2019_games-october.html'
# k = 'NBA_2019_games-november.html'
# l = 'NBA_2019_games-december.html'
# m = 'NBA_2019_games-january.html'
# n = 'NBA_2019_games-february.html'
# o = 'NBA_2019_games-march.html'
# p = 'NBA_2019_games-april.html'


def get_team_info():

    # for letter in list:

    teams = []
    base_url = 'https://www.basketball-reference.com/leagues/'

    for u in month_loop.get_url():

        page_request = requests.get(base_url + u)

        # print(page_request)

        soup = BeautifulSoup(page_request.text, 'html.parser')

        table = soup.find('table')

        # print(soup)

    # Looks at the table element..

        if table:

            table_body = table.find('tbody')

        # Loops on all 'tr' elements on the table (rows)..

            for row in table_body.findAll('tr'):

                pl = row.findAll('th')
               # print(pl)

                data1 = row.findAll('td')

                if not len(data1) <= 0:

                    home_pts = data1[4].text
                    # print(home_pts)
                    if not len(home_pts) <= 0:

                        cells = row.findAll('a')
                        # url = row.findAll['href']

                        date = cells[0].text
                        away_team = cells[1].text
                        home_team = cells[2].text
                        home_pts = int(data1[4].text)
                        away_pts = int(data1[2].text)
                        # boxscore_url = cells[3].text

                        # Testing the data that is pulled through from the above..

                        # print(date)
                        # print(away_team)
                        # print(home_team)
                        # print(home_pts)
                        # print(away_pts)

                        team_entry = {"Away Team": away_team,
                                      "Away Pts": away_pts,
                                      "Home Team": home_team,
                                      "Home Pts": home_pts,
                                      "xDate": date}
                                      # "Boxscore URL": boxscre_url}
                        teams.append(team_entry)

            # return pd.DataFrame(teams)
            # Need to set the Date, Team Names and URL on another loop as it
            # they are all under element 'a'...

            # team_url = row.findAll('a')
            # team_names = team_url.text
            # team_pages = team_url['href']

            # print(team_names)
            # print(team_pages)

        # This code aligns each iteration/index with a column header in a DataFrame..
        # Currently works.. although we need to convert pts to intergesr.. currently all strings

        #         cells = row.findAll('td')
        #         date = cells[0].text
        #         start_time = cells[1].text
        #         away_team = cells[2].text
        #         away_pts = int(cells[3].text)
        #         home_team = cells[4].text
        #         home_pts = int(cells[5].text)
        #         boxscore = cells[6].text
        #         overtime = cells[7].text
        #         # attendance = cells[8].text
        #         # notes = cells[9].text
        #
        #         team_entry = {"Date": date,
        #                       "Start Time": start_time,
        #                       "Away": away_team,
        #                       "Away Pts": away_pts,
        #                       "Home Team": home_team,
        #                       "Home Pts": home_pts,
        #                       "Boxscore url": boxscore,
        #                       "Overtime": overtime}
        #                       # "Attendance": attendance}
        #                       # "Notes": notes}
        #
        #         teams.append(team_entry)
        #
    return pd.DataFrame(teams)


teams_general_info = get_team_info()

# print(get_team_info())
# print(teams_general_info.head())
print(teams_general_info.to_csv("NBA_TeamSchedule.csv", sep=',', encoding='utf-8', index=False))

# Writing to CSV
# def import_to_csv():
#     wks = teams_general_info.to_csv("NBA_TeamSchedule.csv", sep='\t', encoding='utf-8')
#     return wks

