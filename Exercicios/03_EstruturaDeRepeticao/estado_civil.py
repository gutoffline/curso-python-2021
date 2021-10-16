estado_civil = 'a'
while 'SCVD'.find(estado_civil.upper()) < 0:
    estado_civil = input("Informe o estado civil \nC - Casado\nS - Solteiro\nV - Viúvo\nD - Divorciado \nEscolha: ")
    if 'SCVD'.find(estado_civil.upper()) < 0:
        print("Opção inválida.")