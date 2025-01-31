import openpyxl # biblioteca para manipular arquivos xlsx (Excel)
#from time import sleep  //Biblioteca usada para testes

planilha = "InfoJogo.xlsx" # Variavel do caminho da planilha

def pesquisar(Arquivo):
    #Abre o Arquivo
    wb = openpyxl.load_workbook(Arquivo)
    sheet = wb.active

    nome_jogo = input("Nome do Jogo: ").lower()

    ctd = 0 # contador
    for linha in sheet.iter_rows(min_row=2, min_col=2, max_col=7): #Para cada Linha Da Planilha...
        ctd = ctd+1

        if linha[0].value.lower() == nome_jogo.lower(): #Se o Valor da linha for igual o nome do jogo do usuario...
            print("\n          !!! JOGO ENCONTRADO !!!")
            print(f'\nNome ------------: {linha[0].value}')
            print(f'Desenvolvedor ---: {linha[5].value}')
            print(f'Plataforma: -----: {linha[1].value}')
            print(f'Lançamento ------: {linha[2].value}')
            break

        if ctd == sheet.max_row -1: # Se contador for igual a ultima linha (com conteudo) da planilha...
            print(f"         !!!O Jogo {nome_jogo.title()} Não Foi Encontrado !!!")

pesquisar(planilha)
