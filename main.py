import openpyxl
import json

def procurar_jogo(): #Função para prucurar o Jogo
    try: #Tenta executar o código
        with open("data.json", "r") as f: #Abre o arquivo "data.json"
            dados = json.load(f) #A Variavel dados recebe o dicionario do arquivo "data.json"
            planilha = dados["Planilha"] #Recebe o caminho da planilha
            jogo = dados["Jogo"] #Recebe informações do jogo

        jogos = [] #Lista para receber a lista dos jogos filtrados

        wb = openpyxl.load_workbook(planilha) #Abre o Arquivo Excel
        sheet= wb.active #Variavel que representa a planilha

        for linha in sheet.iter_rows(min_col=3, min_row=2, max_col=8, max_row=sheet.max_row): #Para cada linha na planilha faça:
            if (jogo["Nome"] in str(linha[0].value).lower() if jogo["Nome"] else True) and (jogo["Desenvolvedor"].lower() in str(linha[5].value).lower() if jogo["Desenvolvedor"] else True) and (jogo["Plataforma"] in str(linha[1].value) if jogo["Plataforma"] else True) and (jogo["Ano"] == linha[2].value if jogo["Ano"] != 0 else True):
                jogos.append(linha[0].value)

                jogos.append(linha[0].value) #Adiciona o nome do jogo na lista jogos

        return jogos

    except FileNotFoundError: #caso não achar o Arquivo "data.json" faça os print a segui
        print('Arquivo "data.json" não encontrado ...')
        print('Planilha não encontrada ...')
        print('Criando arquivo "data.json ..."')

#procurar_jogo()