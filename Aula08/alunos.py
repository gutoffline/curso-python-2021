import os

def Cadastro():
    print("Cadastro de Alunos")
    print("Preencha as informações abaixo")
    nome = input("Nome: ")
    if os.path.isfile('alunos.txt'):
        arquivo = open("alunos.txt","r+")
    else:
        arquivo = open("alunos.txt","w+")

    lista_alunos = arquivo.readlines()
    nome = nome + "\n"
    arquivo.writelines(nome)
    arquivo.close()


def Relatorio():
    print("Relatório de Alunos")
    print("NOME")

    arquivo = open("alunos.txt","r+")
    lista_alunos = arquivo.readlines()
    arquivo.close()
    for aluno in lista_alunos:
        print(aluno)
