import openpyxl
import json

def procurar_jogo(): #Função para prucurar o Jogo
    try: #Tenta executar o código
        with open("data.json", "r") as f: #Abre o arquivo "data.json"
            dados = json.load(f) #A Variavel dados recebe o dicionario do arquivo "data.json"
            planilha = dados["Planilha"] #Recebe o caminho da planilha
            nome = dados["Jogo"]["Nome"] #Recebe o Nome do Jogo que o usuario informou
            ano = dados["Jogo"]["Ano"] #Recebe o Ano de lançamento que o usuario informou
            desenvolvedor = dados["Jogo"]["Desenvolvedor"] #Recebe o Desenvolvedor que o usuario informou
            plataforma = dados["Jogo"]["Plataforma"] #Recebe a plataforma que o usuario informou

        jogos = [] #Lista para receber a lista dos jogos filtrados

        wb = openpyxl.load_workbook(planilha) #Abre o Arquivo Ecel
        sheet= wb.active #Variavel que representa a planilha

        if nome or desenvolvedor or plataforma or ano: #se a variavel nome ou desenvolvedor ou plataforma ou ano, estiver guardando algo, faça...
            for linha in sheet.iter_rows(min_col=3, min_row=2, max_col=7, max_row=sheet.max_row): #Para cada linha na planilha faça:
#                print(linha[1].value) <- print de teste
                if nome.lower() in str(linha[0].value).lower(): #se o nome fornecido pelo usuario estiver no nome da linha, faça:
                    jogos.append(str(linha[0].value).title()) #lista jogos receber o nome do jogo

        print(jogos) #<- print de teste
    except FileNotFoundError: #caso não achar o Arquivo "data.json" faça os print a segui
        print('Arquivo "data.json" não encontrado ...')
        print('Planilha não encontrada ...')
        print('Criando arquivo "data.json ..."')