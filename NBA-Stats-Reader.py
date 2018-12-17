import pandas as pd
import csv
import numpy as np

# to find the path of csv files
# import os
# print(os.getcwd())
#  out: ../Users/Docs/etc
# print(os.listdir(os.getcwd())
# out: ['Names of csv files]

# Reading content from the csv

# Reading a csv file
df = pd.read_csv('../PythonProjects/NBA_TeamSchedule.csv')
# print(df.dtypes)
# print(df.columns)
# print(df.describe())


# List of NBA teams

ATL = 'Atlanta Hawks'
BOS = 'Boston Celtics'
BKN = 'Brooklyn Nets'
CHA = 'Charlotte Hornets'
CHI = 'Chicago Bulls'
CLE = 'Cleveland Cavaliers'
DAL = 'Dallas Mavericks'
DEN = 'Denver Nuggets'
DET = 'Detroit Pistons'
GSW = 'Golden State Warriors'
HOU = 'Houston Rockets'
IND = 'Indiana Pacers'
LAC = 'Los Angeles Clippers'
LAL = 'Los Angeles Lakers'
MEM = 'Memphis Grizzlies'
MIA = 'Miami Heat'
MIL = 'Milwaukee Bucks'
MIN = 'Minnesota Timberwolves'
NOR = 'New Orleans Pelicans'
OKC = 'Oklahoma City Thunder'
ORL = 'Orlando Magic'
PHI = 'Philadelphia 76ers'
PHO = 'Phoenix Suns'
POR = 'Portland Trail Blazers'
SAC = 'Sacramento Kings'
SAS = 'San Antonio Spurs'
TOR = 'Toronto Raptors'
UTA = 'Utah Jazz'
WAS = 'Washington Wizards'


# print(df)
x = df['Difference'] = df['Away Pts'] - df['Home Pts']

# print(x)
# Creating a new column 'Difference'
p = df[df['Difference'] > 200][['Home Team', 'Away Team', 'Difference']]

print(p)
# if df['Difference'] > 200:
#     print(['Away Team' + 'vs' + 'Home Team'])

# Things to find:
# - Matchups with the largest differentials
# - Which team wins at home more
# - Which team wins away more

# Writing the contents out of the csv
# with open('../PythonProjects/NBA_TeamSchedule.csv', newline='') as csvfile:
#     b_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in b_reader:
#         print(','.join(row))

# df = pd.read_csv('../PythonProjects/[working] basketballref_teams.py', sep=',', keep_default_na=False)


