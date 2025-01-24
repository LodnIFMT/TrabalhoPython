import openpyxl
from time import sleep

planilha = "Lista_Jogos.xlsx"

def pesquisar(Arquivo):
    wb = openpyxl.load_workbook(Arquivo)
    sheet = wb.active

    nome_jogo = input("Nome do Jogo: ").lower()

    ctd = 0
    for linha in sheet.iter_rows(min_row=2, min_col=2, max_col=7):
        ctd = ctd+1

        if linha[0].value.lower() == nome_jogo.lower():
            print("\n          !!! JOGO ENCONTRADO !!!")
            print(f'\nNome ------------: {linha[0].value}')
            print(f'Desenvolvedor ---: {linha[5].value}')
            print(f'Plataforma: -----: {linha[1].value}')
            print(f'Lançamento ------: {linha[2].value}')
            break

        if ctd == sheet.max_row -1:
            print(f"         !!!O Jogo {nome_jogo.title()} Não Foi Encontrado !!!")

pesquisar(planilha)