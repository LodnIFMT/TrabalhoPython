import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jogo") #Titulo da Janela
        self.geometry("1080x720") #Tamanho da Janela

        #Area de Pesquisar o Jogo pelo Nome
        self.label = ctk.CTkLabel(self, text="Nome do Jogo",) #Label escrito, Nome do jogo
        self.nome_jogo = ctk.CTkEntry(self, placeholder_text="ex: Dragon Ball Z", width=500) #Campo para pesquisar o jogo
        self.label.grid(row=0, column=0) #Insere a Label na janela
        self.nome_jogo.grid(row=1, column=0, padx=5, pady=5) #Insere O Campo Para Digitar o nome do Jogo, na Janela

        #Area de Filtrar pelo Desenvolvedor
        self.opcao_devs = ctk.CTkOptionMenu(self, values=["Desenvolvedor1", "Desenvolvedor2", "Desenvolvedor3"]) #Menu de opções, que lista todos os Desenvolvedores
        self.opcao_devs.set("Desenvolvedores") #Fica Escrito, Desenvolvedores, quando o usuario não seleciona a opção
        self.opcao_devs.grid(row=1, column=3, padx=5, pady=5) #Adiciona o Menu na Janela

        #Area de filtrar por plataforma
        self.opcao_plataforma = ctk.CTkOptionMenu(self, values=["PC", "X360", "PS", "PS2"]) #Menu de opçôes que lista todas as plataforma
        self.opcao_plataforma.set("Plataforma") #Fica Escrito, Plataforma, quando o usuario não seleciona a opção
        self.opcao_plataforma.grid(row=1, column=4, padx=5, pady=5)#Adiciona o Menu a janeeal

        #Area de filtrar por Ano
        self.opcao_ano = ctk.CTkOptionMenu(self, values=["2000", "2001", "2002", "2003", "2004"]) #Menu de opções que lista todos os anos que tem na planilha
        self.opcao_ano.set("Ano") #Fica Escrito, Ano, quando o usuario não seleciona a opção
        self.opcao_ano.grid(row=1, column=5, padx=5, pady=5) #Adiciona o Menu a janeeal

app = App()
app.mainloop()