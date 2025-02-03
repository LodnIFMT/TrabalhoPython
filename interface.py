import customtkinter as ctk
from CTkListbox import *
import main
import json
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jogo") #Titulo da Janela
        self.geometry("1080x720") #Tamanho da Janela

        # Verifica se o arquivo data.json existe
        if not os.path.exists("data.json"):

            self.info = { #Dicionario para salvar alguns dados
                "Planilha": None, #Caminho da planilha
                "Jogo": { #Dados do Jogo
                    "Nome": None, #Nome
                    "Ano": None, #Ano de Lançamento
                    "Desenvolvedor": None, #Desenvolvedor
                    "Plataforma": None #Plataforma
                },
                "Lista_Jogo": [] #Lista dos Jogos filtrados
            }

            while True:
                self.caminho = ctk.CTkInputDialog(text='Diretório da Planilha:') #Cria a janela de dialogo para o usuario digitar o caminho da planilha
                self.caminho_input = self.caminho.get_input().replace('"', '') #Retira as aspas do caminho
                if self.caminho_input != '' and os.path.exists(self.caminho_input): #Verifica se o caminho é valido
                    self.info["Planilha"] = self.caminho_input

                    with open("data.json", "w") as f: #Cria o arquivo data.json
                        json.dump(self.info, f, indent=2) #Escreve o caminho da planilha no arquivo

                    break #Sai do loop

        else:
            with open("data.json", "r") as f:
                planilha = json.load(f)

            self.info = { #Dicionario para salvar alguns dados
            "Planilha": planilha["Planilha"], #Caminho da planilha
            "Jogo": { #Dados do Jogo
                "Nome": None, #Nome
                "Ano": None, #Ano de Lançamento
                "Desenvolvedor": None, #Desenvolvedor
                "Plataforma": None #Plataforma
            },
            "Lista_Jogo": [] #Lista dos Jogos filtrados
        }

        #Area de Pesquisar o Jogo pelo Nome
        self.label = ctk.CTkLabel(self, text="Nome do Jogo",) #Label escrito, Nome do jogo
        self.nome_jogo = ctk.CTkEntry(self, placeholder_text="ex: Dragon Ball Z", width=550) #Campo para pesquisar o jogo
        self.label.grid(row=0, column=0, sticky="w", padx=12) #Insere a Label na janela
        self.nome_jogo.grid(row=1, column=0, padx=10, pady=5, sticky="w") #Insere O Campo Para Digitar o nome do Jogo, na Janela
        self.grid_columnconfigure(0, weight=2)

        #Area de Filtrar pelo Desenvolvedor
        self.label_Dev = ctk.CTkLabel(self, text="Desenvolvedor") #Label escrito, Desenvolvedor
        self.opcao_devs = ctk.CTkOptionMenu(self, values=["Desenvolvedor1", "Desenvolvedor2", "Desenvolvedor3"], width=250) #Menu de opções, que lista todos os Desenvolvedores
        self.label_Dev.grid(row=0, column=1) #Insere a Label na janela
        self.opcao_devs.set("-----") #quando o usuario não seleciona a opção
        self.opcao_devs.grid(row=1, column=1, padx=5, pady=5) #Adiciona o Menu na Janela
        self.grid_columnconfigure(1, weight=1)

        #Area de filtrar por plataforma
        self.label_plataforma = ctk.CTkLabel(self, text="Plataforma") #Label escrito, Plataforma
        self.opcao_plataforma = ctk.CTkOptionMenu(self, values=["PC", "X360", "PS", "PS2"], width=250) #Menu de opçôes que lista todas as plataforma
        self.label_plataforma.grid(row=0, column=2) #Insere a Label na janela
        self.opcao_plataforma.set("-----") #quando o usuario não seleciona a opção
        self.opcao_plataforma.grid(row=1, column=2, padx=5, pady=5)#Adiciona o Menu a janeeal
        self.grid_columnconfigure(2, weight=1)

        #Area de filtrar por Ano
        self.label_ano = ctk.CTkLabel(self, text="Ano") #Label escrito, Ano
        self.opcao_ano = ctk.CTkOptionMenu(self, values=["2000", "2001", "2002", "2003", "2004"], width=250,) #Menu de opções que lista todos os anos que tem na planilha
        self.label_ano.grid(row=0, column=3) #Insere a Label na janela
        self.opcao_ano.set("-----") #Fica Escrito, Ano, quando o usuario não seleciona a opção
        self.opcao_ano.grid(row=1, column=3, padx=5, pady=5) #Adiciona o Menu a janeeal
        self.grid_columnconfigure(3, weight=1)

        #Botão Buscar
        self.botao = ctk.CTkButton(self, text="BUSCAR", width=150, command=self.procurar_jogo) #Cria o botao
        self.botao.grid(row=1, column=4, padx=5, pady=5) #Adiciona o botão
        self.grid_columnconfigure(4, weight=1)

        # Campo para exibir as informações dos jogos
        # self.campo_texto = ctk.CTkTextbox(self, width=580, height=635)
        # self.campo_texto.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
        # self.grid_rowconfigure(2, weight=1)

        self.lista_jogo = CTkListbox(self, width=400, height=635)
        self.lista_jogo.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.grid_rowconfigure(2, weight=1)

    def procurar_jogo(self):
#        print(self.info["Jogo"]["Nome"]) <-Print de teste
#        print(self.nome_jogo.get()) <-Print de teste
        self.info["Jogo"]["Nome"] = self.nome_jogo.get().lower() #O Nome do Jogo é guardado no dicionario
        
        with open("data.json", "w") as f: #Cria o arquivo data.json
            json.dump(self.info, f, indent=2) #Salva o Nome no arquivo data.json
        
        main.procurar_jogo() #Executa a função procurar_jogo do Arquivo main.py


app = App()
app.mainloop()