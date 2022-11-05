import tkinter as tk
from tkinter import messagebox
import PROJETO_BD_CLI as bd
import sqlite3
from PIL import ImageTk, Image

class TelaCliente():
    def __init__(self, master, janela_principal):
        self.janela_cliente = master
        self.janela_cliente.overrideredirect(True)
        self.janela_cliente.title("‍©𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮")
        self.janela_cliente['background'] = '#ffdead'
        self.janela_principal = janela_principal
        self.frm_text = tk.Frame(self.janela_cliente, background='#ffdead' )
        self.frm_text.pack()
        self.frm_senha = tk.Frame(self.janela_cliente, background='#ffdead')
        self.frm_senha.pack(side=tk.BOTTOM)
        self.frm_btn = tk.Frame(self.janela_cliente, background='#ffdead')
        self.frm_btn.pack(side=tk.BOTTOM)

        self.janela_cliente.resizable(False, False)

        window_height = 450
        window_width = 280

        screen_width = self.janela_cliente.winfo_screenwidth()
        screen_height = self.janela_cliente.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.janela_cliente.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # imagem
        self.logo = ImageTk.PhotoImage(Image.open("Imagens/inicial.jpg"))

        self.spac4 = tk.Label(self.frm_btn, text='', bg='#ffdead')
        self.spac4.pack()

        self.logox = tk.Label(self.frm_btn, text='', bg='#ffdead',image=self.logo)
        self.logox.pack()

        self.spac3 = tk.Label(self.frm_btn, text='', bg='#ffdead')
        self.spac3.pack()

        self.lbl_usuario = tk.Label(self.frm_btn, text ="Usuário", font=' Constantia 15 bold italic', bg='#ffdead', fg='black')
        self.lbl_usuario.pack()

        self.ent_usuario = tk.Entry(self.frm_btn, width= 20, background='#ffdead')
        self.ent_usuario.pack()

        self.lbl_senha = tk.Label(self.frm_btn, text='Senha', font=' Constantia 15 bold italic', bg='#ffdead', fg='black')
        self.lbl_senha.pack()

        self.ent_senha = tk.Entry(self.frm_btn, width= 20, show='*', background='#ffdead')
        self.ent_senha.pack()

        self.spac1 = tk.Label(self.frm_btn, text='', bg='#ffdead')
        self.spac1.pack()

        self.btn_inserir = tk.Button(self.frm_btn,text='Entrar', bg ='#ffdead',fg='black',
                                     command=self.entrar,relief="flat", font=' Times 15 bold')
        self.btn_inserir.pack()

        self.btn_logar = tk.Button(self.frm_btn,text='Novo usuário', command=self.inserir, bg ='#ffdead',
                                   fg='black',relief="flat", font=' Times 15 bold')
        self.btn_logar.pack()

        self.spac = tk.Label(self.frm_btn, text='', bg='#ffdead')
        self.spac.pack()

    def entrar(self):
        User = self.ent_usuario.get()
        password = self.ent_senha.get()
        banco = sqlite3.connect('Bancos/Banco.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT Senha FROM cliente WHERE Usuário = '{}'".format(User))
            senha_bd = cursor.fetchall()
            banco.close()
            if password == senha_bd[0][0]:
                messagebox.showinfo("Saudações!", ""f'{User}'" vamos continuar a nossa aventura! ")
                self.janela_cliente.destroy()
                self.janela_principal.deiconify()
            else:
                messagebox.showinfo('Aviso', 'Erro ao validar o login')
        except:
            messagebox.showinfo('Aviso','Erro ao validar o login')

    def inserir(self):
        User = self.ent_usuario.get()
        password = self.ent_senha.get()
        cont_IDs = []
        for i in bd.consultar('SELECT * FROM cliente;'):
            cont_IDs.append(i[0])
        sql_inserir = f'INSERT INTO cliente VALUES( "{len(cont_IDs)}" ,"{User}","{password}");'
        rar = messagebox.askyesno('Confirmação', 'tem certeza que deseja criar um novo usuáro?')
        if rar == True:
            bd.inserir(sql_inserir)
            messagebox.showinfo("Saudações!", "Agora "f'{User}'" é o mestre dessa partida e esperamos que você respeite as regras, por favor")
            self.janela_cliente.destroy()
            self.janela_principal.deiconify()

