"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = ''
while len(nome) <= 3:
    nome = input("Informe o nome: ")
    if len(nome) <= 3:
        print("O nome precisa ter mais que 3 caracteres.")

idade = -1
while idade < 0 or idade > 150:
    idade = input("Informe a idade: ")
    if idade.isdigit() == False:
        idade = -1
        print("Você digitou um texto. Informe um valor numérico.")
    elif int(idade) < 0 or int(idade) > 150:
        idade = int(idade)
        print("Valor inválido. Informe uma idade entre 0 e 150.")
    else:
        idade = int(idade)

salario = 0
while salario <= 0:
    salario = input("Informe o salário: ")
    if salario.isdigit() == False:
        salario = 0
        print("Você digitou um valor inválido.")
    elif int(salario) <= 0:
        salario = int(salario)
        print("Você digitou um valor inválido.")
    else:
        salario = int(salario)

sexo = ''
while sexo.upper() != 'F' and sexo.upper() != 'M':
    sexo = input("Informe o sexo F ou M: ")
    if sexo.upper() != 'F' and sexo.upper() != 'M':
        print("Valor inválido")

estado_civil = 'a'
while 'SCVD'.find(estado_civil.upper()) < 0:
    estado_civil = input("Informe o estado civil \nC - Casado\nS - Solteiro\nV - Viúvo\nD - Divorciado \nEscolha: ")
    if 'SCVD'.find(estado_civil.upper()) < 0:
        print("Opção inválida.")
