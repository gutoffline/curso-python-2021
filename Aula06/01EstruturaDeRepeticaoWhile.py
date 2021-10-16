"""
contador = 1
while contador <= 5:
    print("Aula", contador)
    if contador == 1:
        print("Introdução ao Python")
    if contador == 2:
        print("Operadores, entrada e saída")
    if contador == 3:
        break
    contador += 1 # contador = contador + 1


imposto = int(input("Informe o valor do imposto entre 0 e 100: "))

while imposto > 100:
    imposto = int(input("Valor inválido. \nInforme o valor do imposto corretamente entre 0 e 100: "))


if imposto < 10:
    print("Baixo")
elif imposto >= 10 and imposto <= 27:
    print("Médio")
elif imposto > 27 and imposto <= 100:
    print("Alto")
else:
    print("imposto inválido")



salario = int(input("Informe o salário: "))
imposto = 27
while imposto > 0:
    imposto = input("Informe o imposto ou S para sair: ")
    if not imposto:
        imposto = 27
    elif imposto.isdigit():
        imposto = int(imposto)
    elif imposto.upper() == 'S':
        break
    else:
        imposto = 0

    print("Imposto: ", imposto)
    print("Salário: ", salario - (salario * (imposto * 0.01)))

"""

"""
Construa uma estrutura que permita inserir nome e telefone de um cliente, exiba na tela tela essas informações com um código sequencial (1 ,2 ,3 ...) e pergunte se deseja cadastrar um novo cliente.
"""

novo  = 's'
codigo = 0

while novo.upper() == 'S':
    codigo += 1
    nome = input("Informe o nome do cliente: ")
    telefone = input("Informe o telefone do cliente: ")
    print("Ficha Cadastral de Cliente")
    print("Código:", codigo)
    print("Nome:", nome)
    print("Telefone:", telefone)
    novo = input("Deseja cadastrar mais um cliente? [S]im [N]ão: ")

print("Programa finalizado")





