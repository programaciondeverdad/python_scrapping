import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
# La librería pprint es usada para hacer las impresiones/salidas más lindas
from pprint import pprint

URL = 'https://www.who.int/feeds/entity/mediacentre/news/es/rss.xml'
# URL = 'https://www.clarin.com/rss/lo-ultimo/'
# URL = 'https://www.pagina12.com.ar/rss/portada'

page = requests.get(URL)
# print(page)
# pprint(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# Buscar por ID
# results = soup.find(id='ResultsContainer')
rss = soup.rss
channel = rss.channel

noticias = channel.find_all('item')
# print(noticias)

# print(noticias[0].title)


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = client.noticiero_vivo
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

collection = db.noticias

# Otra utilización es generar un HTML o un CSV e importarlo en excel!




for noticia in noticias:
	# print("Noticia: " + noticia.title.getText() + " - " + noticia.pubdate.getText())

	noticia_dict = { 'titulo': noticia.title.getText(), 'fecha_publicacion': noticia.pubdate.getText(), 'fuente': URL }

	result = collection.find({'titulo': noticia.title.getText(), 'fecha_publicacion': noticia.pubdate.getText()}).count()
	# pprint(result)
	if result == 0:
		collection.insert_one(noticia_dict)
		print("Insertamos en la base de datos a: " + noticia.title.getText())
	else:
		print("Ya estaba la noticia en la base de datos. Se salta. Noticia: " + noticia.title.getText())
