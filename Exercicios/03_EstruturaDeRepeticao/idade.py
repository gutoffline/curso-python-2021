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