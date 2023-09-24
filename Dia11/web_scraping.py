import bs4
import requests


resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
#resultado.text devuelve una cadena de texto de la web entera. Queremos hacer un parseo de tipo LXML con BS4
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].getText())


parrafo_especial  = sopa.select('div span')
print(parrafo_especial)