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

    
def Desenvolvedor():
    try:
        with open("data.json", "r") as f:
            dados = json.load(f)
            planilha = dados["Planilha"]
        
        wb = openpyxl.load_workbook(planilha)
        sheet = wb.active

        devs = []

        for linha in sheet.iter_rows(min_col=8, min_row=2, max_row=sheet.max_row):
            dois_dv = str(linha[0].value).split('/')
            if dois_dv:
                for dv in dois_dv:
                    if dv not in devs:
                        devs.append(dv)


        if (linha[0] not in devs) and ("/" not in linha[0].value):
            devs.append(linha[0].value)
            print(linha[0].value)

        return devs
    
    except FileNotFoundError:
        print('Arquivo "data.json" não encontrado ...')


def plataforma():
    try:
        with open("data.json", "r") as f:
            dados = json.load(f)
            planilha = dados["Planilha"]
        
        wb = openpyxl.load_workbook(planilha)
        sheet = wb.active

        pltf = []

        for linha in sheet.iter_rows(min_col=4, min_row=2, max_row=sheet.max_row):
            dois_dv = str(linha[0].value).split('/')
            if dois_dv:
                for dv in dois_dv:
                    if dv not in pltf:
                        pltf.append(dv)

        if (linha[0] not in pltf) and ("/" not in linha[0].value):
            pltf.append(linha[0].value)
            print(linha[0].value)

        return pltf
    
    except FileNotFoundError:
        print('Arquivo "data.json" não encontrado ...')



if __name__ == "__main__": #Executado apenas se o arquivo for executado diretamente, (Para Testes!)
    #procurar_jogo()
    #Desenvolvedor()
    plataforma()