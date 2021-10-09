"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

pergunta_1 = int(input("Telefonou para a vítima? (1)Sim ou (0)Não: "))
pergunta_2 = int(input("Esteve no local do crime? (1)Sim ou (0)Não: "))
pergunta_3 = int(input("Mora perto da vítima? (1)Sim ou (0)Não: "))
pergunta_4 = int(input("Devia para a vítima? (1)Sim ou (0)Não: "))
pergunta_5 = int(input("Já trabalhou com a vítima? (1)Sim ou (0)Não: "))
contador = pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5

if contador == 0 or contador == 1:
    print("Inocente")
elif contador == 2:
    print("Suspeita")
elif contador == 3 or contador == 4:
    print("Cúmplice")
else:
    print("Assassina")

