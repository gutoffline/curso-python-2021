import os
import socket
import platform

nome_computador = socket.gethostname()
sistema_operacional = platform.system()
ip_computador = socket.gethostbyname(nome_computador)

#print(nome_computador, sistema_operacional, ip_computador)

nome = ""
while nome == "":
    nome = input("Informe o seu nome: ")

departamento = ""
while departamento == "":
    departamento = input("Informe o departamento: ")

#ESCREVENDO UM ARQUIVO DE TEXTO - INÍCIO
if os.path.isfile("identificacao.csv"):
    arquivo = open("identificacao.csv","r+")
else:
    arquivo = open("identificacao.csv","w+")

lista_id = arquivo.readlines()

arquivo.writelines(nome + ";" + departamento + ";" + nome_computador + ";" + sistema_operacional + ";" + ip_computador + "\n")

arquivo.close()
#ESCREVENDO UM ARQUIVO DE TEXTO - FIM

#LER UM ARQUIVO DE TEXTO - INÍCIO
arquivo = open("identificacao.csv","r+")
conteudo = arquivo.readlines()
for linha in conteudo:
    print(linha)
arquivo.close()
#LER UM ARQUIVO DE TEXTO - FIM
