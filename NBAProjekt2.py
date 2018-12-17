import pygsheets
import pandas as pd

gc = pygsheets.authorize(service_account_file='\PythonProjects\venv\NBA Project 1-a1b8594c93d2.json')

df = pd.DataFrame()

df['name'] = ['Kyle', 'Mel', 'Moochie']

sh = gc.open('NBAPython')

wks = sh[0]

wks.set_dataframe(df(1,1))

