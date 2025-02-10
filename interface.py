import customtkinter as ctk
from CTkListbox import *
import main
import json
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lista = []
        self.indice = 0

        self.title("Jogo") #Titulo da Janela
        self.geometry("1080x800") #Tamanho da Janela

        self.info = { #Dicionario para salvar alguns dados
            "Planilha": None, #Caminho da planilha
            "Jogo": { #Dados do Jogo
                "Nome": None, #Nome
                "Ano": None, #Ano de Lançamento
                "Desenvolvedor": None, #Desenvolvedor
                "Plataforma": None #Plataforma
            }
        }

        # Verifica se o arquivo data.json existe
        if not os.path.exists("data.json"):
            while True:
                self.caminho = ctk.CTkInputDialog(text='Diretório da Planilha:') #Cria a janela de dialogo para o usuario digitar o caminho da planilha
                self.caminho_input = self.caminho.get_input().replace('"', '') #Retira as aspas do caminho
                if self.caminho_input != '' and os.path.exists(self.caminho_input): #Verifica se o caminho é valido
                    self.info["Planilha"] = self.caminho_input

                    with open("data.json", "w") as f: #Cria o arquivo data.json
                        json.dump(self.info, f, indent=2) #Escreve o caminho da planilha no arquivo

                    break #Sai do loop

        else: #Caso Exista...
            with open("data.json", "r") as f: #Abre o arquivo "data.json"
                arquivo = json.load(f) #Recebe os dados do arquivo "data.json"

            self.info["Planilha"] = arquivo["Planilha"] #O Dicionario "info" recebe o caminho da planilha na varivel "Planilha" 

        #Area de Pesquisar o Jogo pelo Nome
        self.label = ctk.CTkLabel(self, text="Nome do Jogo",) #Label escrito, Nome do jogo
        self.nome_jogo = ctk.CTkEntry(self, placeholder_text="ex: Dragon Ball Z", width=550) #Campo para pesquisar o jogo
        self.label.grid(row=0, column=0, sticky="w", padx=12) #Insere a Label na janela
        self.nome_jogo.grid(row=1, column=0, padx=10, pady=5, sticky="ew") #Insere O Campo Para Digitar o nome do Jogo, na Janela
        self.grid_columnconfigure(0, weight=2) #Faz a coluna 0 ficar responsiva

        #Area de Filtrar pelo Desenvolvedor
        devs = main.Desenvolvedor()
        self.label_Dev = ctk.CTkLabel(self, text="Desenvolvedor") #Label escrito, Desenvolvedor
        self.opcao_devs = ctk.CTkOptionMenu(self, values=devs, width=250) #Menu de opções, que lista todos os Desenvolvedores
        self.label_Dev.grid(row=0, column=1) #Insere a Label na janela
        self.opcao_devs.set("-----") #quando o usuario não seleciona a opção
        self.opcao_devs.grid(row=1, column=1, padx=5, pady=5) #Adiciona o Menu na Janela
        self.grid_columnconfigure(1, weight=1) #Faz a coluna 1 ficar responsiva

        #Area de filtrar por plataforma
        plataformas = main.plataforma()
        self.label_plataforma = ctk.CTkLabel(self, text="Plataforma") #Label escrito, Plataforma
        self.opcao_plataforma = ctk.CTkOptionMenu(self, values=plataformas, width=250) #Menu de opçôes que lista todas as plataforma
        self.label_plataforma.grid(row=0, column=2) #Insere a Label na janela
        self.opcao_plataforma.set("-----") #quando o usuario não seleciona a opção
        self.opcao_plataforma.grid(row=1, column=2, padx=5, pady=5)#Adiciona o Menu a janeeal
        self.grid_columnconfigure(2, weight=1) #Faz a coluna 2 ficar responsiva

        #Area de filtrar por Ano
        anos = main.ano()
        self.label_ano = ctk.CTkLabel(self, text="Ano") #Label escrito, Ano
        self.opcao_ano = ctk.CTkOptionMenu(self, values=anos, width=250,) #Menu de opções que lista todos os anos que tem na planilha
        self.label_ano.grid(row=0, column=3) #Insere a Label na janela
        self.opcao_ano.set("-----") #Fica Escrito, Ano, quando o usuario não seleciona a opção
        self.opcao_ano.grid(row=1, column=3, padx=5, pady=5) #Adiciona o Menu a janeeal
        self.grid_columnconfigure(3, weight=1) #Faz a coluna 3 ficar responsiva

        #Botão Buscar
        self.botao = ctk.CTkButton(self, text="BUSCAR", width=150, command=self.procurar_jogo) #Cria o botao
        self.botao.grid(row=1, column=4, padx=5, pady=5) #Adiciona o botão
        self.grid_columnconfigure(4, weight=1) #Faz a coluna 4 ficar responsiva

        #Área que mostra a lista de jogos
        self.lista_jogo = CTkListbox(self, width=400, height=650) #Area da Lista de Jogos
        self.lista_jogo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="new") #Insere a Lista na Janela
        self.lista_jogo.bind("<<ListboxSelect>>", self.teste) #Comando a executar quando o usuario seleciona um item da lista
        self.grid_rowconfigure(2, weight=1) #Deixa a linha 2 responsiva

    #Função para procura de jogos
    def procurar_jogo(self):
        self.lista.clear()
        self.info["Jogo"]["Nome"] = self.nome_jogo.get().lower() #O Nome do Jogo é guardado no dicionario
        
        #Área para verificar se o usuario escolheu algum filtro
        if self.opcao_devs.get() != "-----":
            self.info["Jogo"]["Desenvolvedor"] = self.opcao_devs.get() #O Desenvolvedor é guardado no dicionario

        if self.opcao_plataforma.get() != "-----":
            self.info["Jogo"]["Plataforma"] = self.opcao_plataforma.get() #A Plataforma é guardado no dicionario

        if self.opcao_ano.get() != "-----":
            self.info["Jogo"]["Ano"] = (self.opcao_ano.get()) #O Ano é guardado no dicionario
        
        with open("data.json", "w") as f: #Cria o arquivo data.json
            json.dump(self.info, f, indent=2) #Salva o Nome no arquivo data.json
        
        self.lista.extend(main.procurar_jogo()) #Executa a função procurar_jogo do Arquivo main.py

        self.lista_jogo.delete(0, ctk.END)

        for jg in self.lista:
            itens = self.lista_jogo.size()
            
            if itens < 20:
                self.lista_jogo.insert(ctk.END, jg)
            else:
                break

        if len(self.lista) > 19:
            self.botao_proximo = ctk.CTkButton(self, text="PRÓXIMO",width=150, command=self.proximo)
            self.botao_proximo.grid(row=3, column=1, padx=5, pady=5, sticky="ne")
            self.grid_rowconfigure(3, weight=100)

            self.botao_proximo = ctk.CTkButton(self, text="VOLTAR",width=150, command=self.voltar)
            self.botao_proximo.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
            self.grid_rowconfigure(3, weight=100)


    def proximo(self):
        self.lista_jogo.delete(0, ctk.END)
        self.indice = self.indice +20
        
        for i in range(self.indice, self.indice + 20):
            if i < len(self.lista)-1:
                self.lista_jogo.insert(ctk.END, self.lista[i])
            else:
                if self.indice < len(self.lista):
                    self.lista_jogo.insert(ctk.END, self.lista[i])
                self.indice = 0
    

    def voltar(self):
        self.lista_jogo.delete(0, ctk.END)
        self.indice = self.indice -20
        
        if self.indice < 0:
            self.indice = 0

        for i in range(self.indice, self.indice + 20):
            self.lista_jogo.insert(ctk.END, self.lista[i])


    def teste(self):
        print("Deu Certo... Eu Acho")


app = App()
app.mainloop()