from bs4 import BeautifulSoup as bs
import requests as r
import pandas as pd

# variables
dates = '2018-8-27'
location = 'castleford'
table = pd.read_table('https://www.wunderground.com/history/daily/gb/%s/IWESTYOR64/date/%s' % (location, dates))

print(table.head())
url = 'https://www.wunderground.com/hourly/gb/'
hist = 'history/daily/gb/%s/IWESTYOR64/date/%s' % (location, dates)

full_url = url + location

print(full_url)
