nome = ''
while len(nome) <= 3:
    nome = input("Informe o nome: ")
    if len(nome) <= 3:
        print("O nome precisa ter mais que 3 caracteres.")
