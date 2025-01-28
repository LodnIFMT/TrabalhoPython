import tkinter as tk 

janela = tk.Tk()

janela.title("Pesquisar Jogos")
janela.geometry("650x650")

tk.Label(janela, text="Nome do jogo:").grid(row=0, column=0, pady=2)
nome = tk.Entry(janela, width=50)
nome.grid(row=1,column=0, padx=5, pady=5)

dev-menu = tk.OptionMenu(janela, )

janela.mainloop()