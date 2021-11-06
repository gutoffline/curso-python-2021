from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://gutoffline.github.io/cinema/"
reposta = urlopen(url)
html_site = reposta.read()

soup_site = BeautifulSoup(html_site, 'html.parser')

#1) Extrair o título da página?
titulo_pagina = soup_site.title.get_text()
print(titulo_pagina)

#2) E se eu quiser extrair o título da maior hierarquia(h1) no corpo da página?
titulo_principal = soup_site.h1.get_text()
print(titulo_principal)

#3) Coletar o texto "A maior premiação do cinema aconteceu em Fevereiro. Os destaques deste ano foram:"
texto = soup_site.p.get_text()
print(texto)


#4) Coletar a lista de destaques
lista_destaques = soup_site.find_all("ul",{"class":"destaques"})
for item in soup_site.find_all("ul",{"class":"destaques"}):
    print(item.get_text())

#5) Colete todos os filmes que tenham vencido suas categorias.
lista_vencedores = soup_site.select(".vencedor")
for vencedor in lista_vencedores:
    print(vencedor.text)