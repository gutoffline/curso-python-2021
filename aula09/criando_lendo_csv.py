import os
import socket
import platform
from datetime import datetime

def Cadastrar():
    nome_computador = socket.gethostname()
    sistema_operacional = platform.system()
    ip_computador = socket.gethostbyname(nome_computador)
    agora = datetime.now()

    nome = input("Informe seu nome: ")

    if os.path.isfile("lista_comp.csv"):
        arquivo = open("lista_comp.csv","r+")
    else:
        arquivo = open("lista_comp.csv","w+")

    dados_arquivo = arquivo.readlines()

    linha_nova = str(agora) + ";" + nome + ";" + nome_computador + sistema_operacional + ";" + ip_computador + ";\n"

    arquivo.writelines(linha_nova)



def Relatorio():
    try:
        arquivo = open("lista_comp.csv","r+")
        dados_arquivo = arquivo.readlines()
        for linha in dados_arquivo:
            colunas = linha.split(";")

            linha_nova = ''
            for coluna in colunas:
                linha_nova += coluna + "\t"

            print(linha_nova)

    except:
        print("Ocorreu algum erro")
    finally:
        print("Relatório finalizado")


opcao = input("1 - cadastrar \n2 - relatório \n")
if opcao == "1":
    Cadastrar()
elif opcao == "2":
    Relatorio()