from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.superpaguemenos.com.br/"
reposta = urlopen(url)
html_site = reposta.read()

soup_site = BeautifulSoup(html_site, 'html.parser')

titulos = soup_site.select(".title")
precos = soup_site.select(".price")
print(titulos)
print(precos)

lista_produtos = []
i = 0
while i < len(titulos):
    lista_produtos.append(
        [
            titulos[i].text,
            precos[i].text
        ])
    i+=1

for produto in lista_produtos:
    print(produto[0], produto[1])