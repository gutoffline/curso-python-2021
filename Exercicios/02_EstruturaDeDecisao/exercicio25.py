"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

pergunta_1 = input("Telefonou para a vítima? [S]im ou [N]ão: ")
pergunta_2 = input("Esteve no local do crime? [S]im ou [N]ão: ")
pergunta_3 = input("Mora perto da vítima? [S]im ou [N]ão: ")
pergunta_4 = input("Devia para a vítima? [S]im ou [N]ão: ")
pergunta_5 = input("Já trabalhou com a vítima? [S]im ou [N]ão: ")
contador = 0

if pergunta_1.upper() == "S":
    contador += 1

if pergunta_2.upper() == "S":
    contador += 1

if pergunta_3.upper() == "S":
    contador += 1

if pergunta_4.upper() == "S":
    contador += 1

if pergunta_5.upper() == "S":
    contador += 1

if contador == 0 or contador == 1:
    print("Inocente")
elif contador == 2:
    print("Suspeita")
elif contador == 3 or contador == 4:
    print("Cúmplice")
else:
    print("Assassina")

