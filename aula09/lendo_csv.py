arquivo = open("HIST_PAINEL_COVIDBR_2021_Parte1_04nov2021.csv", "r+",encoding='utf-8')
dados_arquivo = arquivo.readlines()
for linha in dados_arquivo:
    colunas = linha.split(";")

    linha_nova = ''
    for coluna in colunas:
        linha_nova += coluna + "\t"

    print(linha_nova)