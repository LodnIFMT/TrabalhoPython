import openpyxl
import os
import tkinter as tk
from tkinter import messagebox

planilha = "Lista_Jogos.xlsx"

# Função para validar a entrada (nome do jogo, desenvolvedor ou ano)
def validar_entrada(nome_jogo, desenvolvedor, ano):
    return nome_jogo.strip().lower(), desenvolvedor.strip().lower(), ano.strip().lower()

# Função para obter sugestões de jogos semelhantes
def obter_sugestoes(nome_jogo, desenvolvedor, ano, jogos):
    return [
        jogo for jogo in jogos
        if (nome_jogo in jogo[0].value.lower() if nome_jogo else True) and
           (desenvolvedor in jogo[5].value.lower() if desenvolvedor else True) and
           (ano in str(jogo[2].value) if ano else True)
    ]

# Função para exibir as informações de um jogo
def mostrar_jogo(jogo, resultado_texto):
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, f'\nNome ------------: {jogo[0].value}')
    resultado_texto.insert(tk.END, f'\nDesenvolvedor ---: {jogo[5].value}')
    resultado_texto.insert(tk.END, f'\nPlataforma: -----: {jogo[1].value}')
    resultado_texto.insert(tk.END, f'\nLançamento ------: {jogo[2].value}')

# Função para realizar a busca de jogos
def pesquisar(arquivo, nome_jogo, desenvolvedor, ano, resultado_texto, lista_jogos):
    if not os.path.exists(arquivo):
        messagebox.showerror("Erro", f"Arquivo '{arquivo}' não encontrado.")
        return

    try:
        wb = openpyxl.load_workbook(arquivo)
        sheet = wb.active

        nome_jogo, desenvolvedor, ano = validar_entrada(nome_jogo, desenvolvedor, ano)
        todos_jogos = list(sheet.iter_rows(min_row=2, min_col=2, max_col=7))
        lista_jogos.delete(0, tk.END)
        resultado_texto.delete(1.0, tk.END)

        jogos_encontrados = set([
            tuple(linha) for linha in todos_jogos
            if (nome_jogo in linha[0].value.lower() if nome_jogo else True) and
               (desenvolvedor in linha[5].value.lower() if desenvolvedor else True) and
               (ano in str(linha[2].value) if ano else True)
        ])

        if jogos_encontrados:
            for jogo in jogos_encontrados:
                lista_jogos.insert(tk.END, jogo[0].value)
            lista_jogos.bind("<Double-1>", lambda event, jogo=jogo: mostrar_jogo(jogo, resultado_texto))
        else:
            sugestoes = obter_sugestoes(nome_jogo, desenvolvedor, ano, todos_jogos)
            if sugestoes:
                for jogo in sugestoes:
                    lista_jogos.insert(tk.END, jogo[0].value)
                lista_jogos.bind("<Double-1>", lambda event, jogo=sugestoes[0]: mostrar_jogo(jogo, resultado_texto))
            else:
                messagebox.showinfo("Sem resultados", f"Nenhum jogo encontrado para '{nome_jogo}', '{desenvolvedor}' ou '{ano}'.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao tentar abrir ou ler o arquivo: {e}")

# Função para inicializar a interface gráfica
def criar_interface():
    def iniciar_pesquisa():
        nome_jogo = campo_nome_jogo.get()
        desenvolvedor = campo_desenvolvedor.get()
        ano = campo_ano.get()
        if nome_jogo or desenvolvedor or ano:
            pesquisar(planilha, nome_jogo, desenvolvedor, ano, resultado_texto, lista_jogos)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira ao menos um critério de pesquisa.")

    # Criando a janela principal
    janela = tk.Tk()
    janela.title("Busca de Jogos")

    # Label e campos de entrada para os critérios de pesquisa
    tk.Label(janela, text="Digite o nome do jogo:").grid(row=0, column=0, padx=10, pady=10)
    campo_nome_jogo = tk.Entry(janela, width=40)
    campo_nome_jogo.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Digite o nome do desenvolvedor:").grid(row=1, column=0, padx=10, pady=10)
    campo_desenvolvedor = tk.Entry(janela, width=40)
    campo_desenvolvedor.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(janela, text="Digite o ano de lançamento:").grid(row=2, column=0, padx=10, pady=10)
    campo_ano = tk.Entry(janela, width=40)
    campo_ano.grid(row=2, column=1, padx=10, pady=10)

    # Botão de pesquisa
    botao_pesquisar = tk.Button(janela, text="Pesquisar", command=iniciar_pesquisa)
    botao_pesquisar.grid(row=3, column=2, padx=10, pady=10)

    # Lista de resultados encontrados
    tk.Label(janela, text="Jogos encontrados:").grid(row=4, column=0, padx=10, pady=10)
    lista_jogos = tk.Listbox(janela, width=50, height=10)
    lista_jogos.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    # Área de texto para exibir detalhes do jogo selecionado
    tk.Label(janela, text="Detalhes do jogo:").grid(row=6, column=0, padx=10, pady=10)
    resultado_texto = tk.Text(janela, width=50, height=10)
    resultado_texto.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    # Iniciar a interface
    janela.mainloop()

# Função principal para rodar o programa
if __name__ == "__main__":
    criar_interface()
