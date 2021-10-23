clientes_nomes = []
clientes_telefones = []

def cadastro():
    print("== Cadastro de clientes ==")
    resposta = "s"

    while resposta.upper() == "S":
        nome = input("Informe o nome do cliente: ")
        telefone = input("Informe o telefone do cliente: ")
        ficha(nome, telefone)
        clientes_nomes.append(nome)
        clientes_telefones.append(telefone)
        resposta = input("Deseja cadastrar outro cliente? [S]im ou [N]ão: ")
    print("==Fim do cadastro==")


    print("==Início do relatório==")
    total_clientes = len(clientes_nomes)
    contador = 0

    print("Nome\t Telefone")
    while contador < total_clientes:
        print(clientes_nomes[contador] , "\t" ,clientes_telefones[contador])
        contador += 1

    print("==Fim do relatório==")


def ficha(nome, telefone):
    print("Ficha do cliente")
    print("Nome: ", nome)
    print("Telefone: ", telefone)