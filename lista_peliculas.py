import requests
from lxml import html
import json

"""
Tutorial educativo para aprender a analizar y extraer información de páginas web.

La principal tarea es analizar cómo está estructurada la información en la página web.
Para ello usa el inspector de las herramientas de desarrolladores de tu navegador.

Tutoriales:
* https://www.geeksforgeeks.org/scrape-imdb-movie-rating-and-details-using-python/

"""
url = 'https://www.imdb.com/chart/top/'
res = requests.get(url)
peliculas = html.fromstring(res.text)

# Extraer las url de las imágenes.
# Vemos que las imágenes están en un td de clase "posterColumn" dentro de un "a"
# que tiene un "img" que contiene la url de la película.
imagenes = peliculas.xpath('//td[contains(@class, "posterColumn")]/a/img/@src')

json.dump(imagenes, open('imagenes.json', 'w'))

# Si queremos analizar todas las películas
listapelis = peliculas.xpath('//tbody[contains(@class, "lister-list")]/tr')

