import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Tela_Ajuda:
    def __init__(self, master, janela_principal):
        self.janela_ajuda = master
        self.janela_ajuda.overrideredirect(True)
        self.janela_ajuda.title('AJUDA')
        self.janela_ajuda['background'] = 'gainsboro'
        self.janela_ajuda.grab_set()
        self.janela_principal = janela_principal
        self.janela_ajuda.resizable(False, False)

        #CENTRALIZAR
        window_height = 265
        window_width = 250
        screen_width = self.janela_ajuda.winfo_screenwidth()
        screen_height = self.janela_ajuda.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_ajuda.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Imagem
        self.ajuda = ImageTk.PhotoImage(Image.open("Imagens/ajuda.png"))
        self.logox = tk.Label(self.janela_ajuda, text='', bg='gainsboro', image=self.ajuda)
        self.logox.pack()

        #Botões
        self.spac = tk.Label(self.janela_ajuda, text='', bg='gainsboro')
        self.btn1 = tk.Button(self.janela_ajuda, text='Equipe', command=self.info, bg='OrangeRed', relief="ridge", fg= "gainsboro")
        self.btn2 = tk.Button(self.janela_ajuda, text='Como adicionar arquivo?', command=self.pergunta, bg='OrangeRed', relief="ridge", fg= "gainsboro")
        self.btn3 = tk.Button(self.janela_ajuda, text='Erro no sistema', command=self.erro, bg='OrangeRed', relief="ridge", fg= "gainsboro")
        self.btn4 = tk.Button(self.janela_ajuda, text='Voltar', command=self.voltar, bg='OrangeRed', relief="ridge", fg= "gainsboro")
        self.spac1 = tk.Label(self.janela_ajuda, text='', bg='gainsboro')

        self.spac.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
        self.spac1.pack()

    def info(self):
        messagebox.showinfo('© 𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮','\n© 𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮\n\nCEO\nLuiz Felipe da Silva Moura\n\n'
                                               'Equipe de desenvolvedores:\nLuiz Felipe da Silva Moura\n'
                                               'João Vitor Henrique de Melo\n\n'
                                               'Designer:\nLuiz Felipe da Silva Moura\n\n'
                                               'Escritor:\nLuiz Felipe da Silva MOura\n\n')

    def voltar(self):
        self.janela_ajuda.destroy()
        self.janela_principal.deiconify()

    def pergunta(self):
        rar = messagebox.askyesno('Complicado', 'Quer matar o programador?')
        if rar == True:
            messagebox.showinfo('fiquei irritado', 'vai trabalhar!')

    def erro(self):
        messagebox.showinfo('Erro no sistema', 'Entre em contato com © 𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮!')