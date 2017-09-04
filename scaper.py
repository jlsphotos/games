from lxml import html
import requests as req

page = req.get('http://www.imdb.com/search/title?year=2017,2017&title_type=feature&sort=moviemeter,asc')
tree = html.fromstring(page.content)

#This will create a list of buyers:
id = [x.strip('.') for x in tree.xpath('//*[@id="main"]/div/div/div[3]/div/div[3]/h3/span[1]/text()')]
title = tree.xpath('//*[@id="main"]/div/div/div/div/div/h3/a/text()')
rating = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/div/div[1]/strong/text()')
meta = [x.strip(' ') for x in tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/div/div[3]/span/text()')]
desc = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[2]/text()')
director = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[3]/a[1]/text()')
votes = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[4]/span[2]/text()')
gross = tree.xpath('//*[@id="main"]/div/div/div/div/div[3]/p[4]/span[5]/text()')


print(id)
print(title)
print(rating)
print(meta)
print(desc)
print(director)
print(votes)
print(gross)


