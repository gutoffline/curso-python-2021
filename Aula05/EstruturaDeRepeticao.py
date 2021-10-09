"""
numero = 0
while numero <= 10:
    print(numero)
    numero += 1

print("programa terminado")
"""

"""
1) Usuário escolher qual tabuada será feita
2) Usuário escolher o início
3) Usuário escolher o fim
4) Caso o usuário escolha um início maior que o fim, colocar 1 para inicio e 10 para fim
"""
print("TABUADA")
tabuada = int(input("Qual tabuada deve ser feita? "))
inicio = int(input("Escolha o início: "))
fim = int(input("Escolha o fim: "))

if inicio > fim:
    inicio = 1
    fim = 10

while inicio <= fim:
    print( tabuada , " x ", inicio, " =", tabuada*inicio)
    inicio += 1

