import customtkinter as ctk
from CTkListbox import *
import main
from json import load, dump
from os import path

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lista = []
        self.indice = 0

        self.title("Jogo") #Titulo da Janela
        self.geometry("1080x720") #Tamanho da Janela
        self.resizable(False, False) #Impede que a janela seja redimensionada

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
        if not path.exists("data.json"):
            while True:
                self.caminho = ctk.CTkInputDialog(text='Diretório da Planilha:') #Cria a janela de dialogo para o usuario digitar o caminho da planilha
                self.caminho_input = self.caminho.get_input().replace('"', '') #Retira as aspas do caminho
                if self.caminho_input != '' and path.exists(self.caminho_input): #Verifica se o caminho é valido
                    self.info["Planilha"] = self.caminho_input

                    with open("data.json", "w") as f: #Cria o arquivo data.json
                        dump(self.info, f, indent=2) #Escreve o caminho da planilha no arquivo

                    break #Sai do loop

        else: #Caso Exista...
            with open("data.json", "r") as f: #Abre o arquivo "data.json"
                arquivo = load(f) #Recebe os dados do arquivo "data.json"

            self.info["Planilha"] = arquivo["Planilha"] #O Dicionario "info" recebe o caminho da planilha na varivel "Planilha" 

        #Area de Pesquisar o Jogo pelo Nome
        self.label = ctk.CTkLabel(self, text="Nome do Jogo",) #Label escrito, Nome do jogo
        self.nome_jogo = ctk.CTkEntry(self, placeholder_text="ex: Dragon Ball Z", width=395) #Campo para pesquisar o jogo
        self.label.grid(row=0, column=0, sticky="w", padx=12) #Insere a Label na janela
        self.nome_jogo.grid(row=1, column=0, padx=10, pady=5, sticky="we") #Insere O Campo Para Digitar o nome do Jogo, na Janela

        #Area de Filtrar pelo Desenvolvedor
        devs = main.Desenvolvedor()
        self.label_Dev = ctk.CTkLabel(self, text="Desenvolvedor") #Label escrito, Desenvolvedor
        self.opcao_devs = ctk.CTkOptionMenu(self, values=devs, width=195) #Menu de opções, que lista todos os Desenvolvedores
        self.opcao_devs.set("-----") #quando o usuario não seleciona a opção
        self.label_Dev.grid(row=0, column=1) #Insere a Label na janela
        self.opcao_devs.grid(row=1, column=1, padx=5, pady=5) #Adiciona o Menu na Janela

        #Area de filtrar por plataforma
        plataformas = main.plataforma()
        self.label_plataforma = ctk.CTkLabel(self, text="Plataforma") #Label escrito, Plataforma
        self.opcao_plataforma = ctk.CTkOptionMenu(self, values=plataformas, width=195) #Menu de opçôes que lista todas as plataforma
        self.opcao_plataforma.set("-----") #quando o usuario não seleciona a opção
        self.label_plataforma.grid(row=0, column=2) #Insere a Label na janela
        self.opcao_plataforma.grid(row=1, column=2, padx=5, pady=5)#Adiciona o Menu a janeeal

        #Area de filtrar por Ano
        anos = main.ano()
        self.label_ano = ctk.CTkLabel(self, text="Ano") #Label escrito, Ano
        self.opcao_ano = ctk.CTkOptionMenu(self, values=anos, width=100,) #Menu de opções que lista todos os anos que tem na planilha
        self.opcao_ano.set("-----") #Fica Escrito, Ano, quando o usuario não seleciona a opção
        self.label_ano.grid(row=0, column=3) #Insere a Label na janela
        self.opcao_ano.grid(row=1, column=3, padx=5, pady=5) #Adiciona o Menu a janeeal

        #Botão Buscar
        self.botao = ctk.CTkButton(self, text="BUSCAR", width=90, command=self.procurar_jogo) #Cria o botao
        self.botao.grid(row=1, column=4, padx=5, pady=5) #Adiciona o botão

        #Área que mostra a lista de jogos
        self.lista_jogo = CTkListbox(self, width=425, height=580) #Area da Lista de Jogos
        self.lista_jogo.grid(row=2, column=0, padx=5, pady=5, sticky="new") #Insere a Lista na Janela
        self.lista_jogo.bind("<<ListboxSelect>>", func=self.info_jg) #Comando a executar quando o usuario seleciona um item da lista

        #Area de Mostrar o resultado
        label_nome = ctk.CTkLabel(self, text="NOME:", width=10, font=("Arial", 15)).place(x=470, y=70) #Label escrito, NOME
        
        label_desenvolvedor = ctk.CTkLabel(self, text="DESENVOLVEDOR:", width=50, font=("Arial", 15)).place(x=470, y=150) #Label escrito, NOME

        label_ano = ctk.CTkLabel(self, text="ANO DE LANÇAMENTO:", width=100, font=("Arial", 15)).place(x=470, y=260) #Label escrito, NOME #Label escrito, NOME

        label_plataforma = ctk.CTkLabel(self, text="PLATAFORMAS:", width=50, font=("Arial", 15)).place(x=950, y=150) #Label escrito, NOME


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
            dump(self.info, f, indent=2) #Salva o Nome no arquivo data.json
        
        self.lista.extend(main.procurar_jogo(self)) #Executa a função procurar_jogo do Arquivo main.py

        self.botao_proximo = ctk.CTkButton(self, text="LIMPAR",width=100, command=self.limpar).place(x=10, y=680)

        if len(self.lista) > 19:
            self.botao_proximo = ctk.CTkButton(self, text="PROXIMO",width=100, command=self.proximo).place(x=360, y=680)

            self.botao_proximo = ctk.CTkButton(self, text="VOLTAR",width=100, command=self.voltar).place(x=250, y=680)

    def proximo(self):
        main.fun_proximo(self)

    def voltar(self):
        main.fun_voltar(self)

    def limpar(self):
        main.fun_limpar(self)

    def info_jg(self, event):
        jogo = self.lista_jogo.get(self.lista_jogo.curselection())
        main.informacoes(jogo)

        with open("data.json", "r") as f:
            arquivo= load(f)
            info = arquivo["jg_info"]

        nome_jogo = ctk.CTkLabel(self, text=info["Nome"], width=50, font=("Arial", 20, "bold")).place(x=470, y=100)

        Desevolvedor_jg = ctk.CTkOptionMenu(self, values=info["Desenvolvedor"], width=70).place(x=470, y=185)

        plataforma_lista = ctk.CTkOptionMenu(self, values=info["Plataforma"], width=70).place(x=950, y=185)

        ano_jogo = ctk.CTkLabel(self, text=info["Ano"], width=50, font=("Arial", 20, "bold")).place(x=470, y=285)

app = App()
app.mainloop()
    