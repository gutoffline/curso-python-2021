import os


def Cadastro():
    print("Cadastro de Matérias")
    print("Preencha as informações abaixo:")
    nome = input("Nome da matéria:")

    if os.path.isfile("materias.txt"):
        arquivo = open("materias.txt","r+")
    else:
        arquivo = open("materias.txt","w+")

    lista_materias = arquivo.readlines()
    nome = nome + "\n"
    arquivo.writelines(nome)
    arquivo.close()

def Relatorio():
    arquivo = open("materias.txt" , "r+")
    lista_materias = arquivo.readlines()
    arquivo.close()
    print("Relatório de Matérias")
    print("Nome")
    for materia in lista_materias:
        print(materia)

