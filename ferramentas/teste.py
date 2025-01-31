import openpyxl  # biblioteca para manipular arquivos xlsx (Excel)
import os  # para checar se o arquivo existe

planilha = "Lista_Jogos.xlsx"  # Variável do caminho da planilha

def validar_entrada():
    """Função para garantir que o usuário insira um nome válido de jogo."""
    while True:
        nome_jogo = input("Nome do Jogo: ").strip()
        if nome_jogo:
            return nome_jogo.lower()
        else:
            print("Por favor, insira um nome de jogo válido (não vazio).")

def obter_sugestoes(nome_jogo, jogos):
    """Função que retorna jogos com nomes que contêm a palavra-chave fornecida."""
    sugestoes = []
    for jogo in jogos:
        if nome_jogo in jogo[0].value.lower():  # Verifica se o nome contém o texto pesquisado
            sugestoes.append(jogo)
    return sugestoes

def mostrar_jogo(jogo):
    """Exibe as informações de um jogo."""
    print(f'\nNome ------------: {jogo[0].value}')
    print(f'Desenvolvedor ---: {jogo[5].value}')
    print(f'Plataforma: -----: {jogo[1].value}')
    print(f'Lançamento ------: {jogo[2].value}')

def pesquisar(Arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(Arquivo):
        print(f"Erro: O arquivo '{Arquivo}' não foi encontrado.")
        return

    try:
        # Abre o Arquivo
        wb = openpyxl.load_workbook(Arquivo)
        sheet = wb.active

        nome_jogo = validar_entrada()  # Garantir que o nome do jogo seja válido
        jogos_encontrados = set()  # Usar um set para evitar jogos repetidos
        todos_jogos = list(sheet.iter_rows(min_row=2, min_col=2, max_col=7))  # Carrega todos os jogos

        for linha in todos_jogos:
#            if linha[0].value and linha[0].value.lower() == nome_jogo:  # Se o valor da linha for igual ao nome do jogo
            if linha[0].value.lower() == nome_jogo:
                jogos_encontrados.add(tuple(linha))  # Adiciona a linha no set

        if jogos_encontrados:  # Se algum jogo foi encontrado
            print(f"\n          !!! JOGO(S) ENCONTRADO(S) !!!")
            for jogo in jogos_encontrados:  # Imprimir todos os jogos encontrados
                mostrar_jogo(jogo)
        else:
            # Caso não tenha encontrado um jogo exato, sugerir jogos parecidos
            print(f"         !!! O Jogo '{nome_jogo.title()}' Não Foi Encontrado !!!")
            sugestoes = obter_sugestoes(nome_jogo, todos_jogos)

            if sugestoes:
                print("\nTalvez você esteja procurando por um desses jogos?")
                for i, jogo in enumerate(sugestoes, 1):
                    print(f"{i}. {jogo[0].value}")
                try:
                    escolha = int(input("\nEscolha o número do jogo para ver mais detalhes (ou 0 para sair): "))
                    if 1 <= escolha <= len(sugestoes):
                        mostrar_jogo(sugestoes[escolha - 1])
                    else:
                        print("Nenhuma opção válida selecionada.")
                except ValueError:
                    print("Entrada inválida. Nenhuma ação tomada.")
            else:
                print("Não encontramos nenhum jogo semelhante.")

    except Exception as e:
        print(f"Erro ao tentar abrir ou ler o arquivo: {e}")

def continuar_busca():
    """Função que pergunta ao usuário se deseja realizar outra pesquisa."""
    while True:
        resposta = input("\nDeseja pesquisar outro jogo? (s/n): ").strip().lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("Por favor, responda com 's' para sim ou 'n' para não.")

def main():
    while True:
        pesquisar(planilha)  # Chama a função de pesquisa
        if not continuar_busca():  # Pergunta se deseja continuar
            print("Obrigado por usar a busca de jogos!")
            break

if __name__ == "__main__":
    main()
