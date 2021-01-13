import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# La librería pprint es usada para hacer las impresiones/salidas más lindas
from pprint import pprint

URL = 'https://www.who.int/feeds/entity/mediacentre/news/es/rss.xml'
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# Buscar por ID
# results = soup.find(id='ResultsContainer')
rss = soup.rss
channel = rss.channel

noticias = soup.rss.channel.find_all('item')
# print(items)

for noticia in noticias:
	print("Noticia: " + noticia.title.getText() + " - " + noticia.pubdate.getText())





# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=client.noticiero_vivo
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

collection = db.noticias
noticia = { 'titulo': "Titulo", 'fecha_publicacion': "13/13/2013", 'fuente': "WHO" }
collection.insert_one(noticia)

# Otra utilización es generar un HTML o un CSV e importarlo en excel!