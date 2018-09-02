from bs4 import BeautifulSoup as bs
import requests as r
import pandas as pd

# variables
table = pd.read_table('https://www.wunderground.com/history/daily/gb/castleford/IWESTYOR64/date/2018-8-27')

print(table.head())
url = 'https://www.wunderground.com/hourly/gb/'
hist = 'history/daily/gb/castleford/IWESTYOR64/date/2018-8-27'
location = 'castleford'
full_url = url + location

print(full_url)
