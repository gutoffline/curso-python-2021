from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://gutoffline.github.io/programacao.html"
reposta = urlopen(url)
html_site = reposta.read()

soup_site = BeautifulSoup(html_site, 'html.parser')
#print(soup_site.prettify())

#pegar o título da página
titulo_pagina = soup_site.title.get_text()
print(titulo_pagina)

titulo_principal = soup_site.h1.get_text()
print(titulo_principal)

nome = soup_site.body.nav.div.a.get_text()
print(nome)

lista_especialidade = soup_site.find_all('h5')
for especialidade in lista_especialidade:
    print(especialidade.text)