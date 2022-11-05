import tkinter as tk
from tkinter import ttk
import  PROJETO_BD_GERAL as bd
from tkinter import messagebox
from PIL import ImageTk, Image

class Tela_cadastrar():
    def __init__(self, master, janela_principal, tvw):
        self.janela_cadastro = master
        self.janela_cadastro.overrideredirect(True)
        self.tvw_menu = tvw
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro['background'] = '#696969'
        self.janela_cadastro.grab_set()
        self.janela_principal = janela_principal
        self.janela_cadastro.resizable(False, False)

        #CENTRALIZAR
        window_height = 420
        window_width = 210
        screen_width = self.janela_cadastro.winfo_screenwidth()
        screen_height = self.janela_cadastro.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_cadastro.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Imagem
        self.cadastrar = ImageTk.PhotoImage(Image.open("Imagens/RPG.png"))
        self.info = tk.Label(self.janela_cadastro, text='',bg='#696969', image=self.cadastrar)
        self.info.pack()

        #Layout
        self.lbl_nome = tk.Label(self.janela_cadastro, text='Nome:', background='#696969')
        self.ent_nome = tk.Entry(self.janela_cadastro, width=23, background='DarkGray')

        self.lbl_classe = tk.Label(self.janela_cadastro, text='Classe:', background='#696969')
        v = tk.StringVar
        self.cbx_classe = ttk.Combobox(self.janela_cadastro, textvariable=v, background='#696969', state='readonly')
        self.cbx_classe['values'] = ('Espadachim', 'Atirador', 'Inventor', 'Assassino', 'Xamã', 'Lutador', 'Bardo')

        self.lbl_especie = tk.Label(self.janela_cadastro, text='Espécie:', background='#696969')
        v = tk.StringVar
        self.cbx_especie = ttk.Combobox(self.janela_cadastro, textvariable=v, background='navajowhite2', state='readonly')
        self.cbx_especie['values'] = ('Humano', 'Elfo', 'Anão', 'Minotauro', 'Gnomo', 'Fada', 'Dragonborn ')

        self.lbl_sexo = tk.Label(self.janela_cadastro, text='Sexo:', background='#696969')
        v = tk.StringVar
        self.cbx_sexo = ttk.Combobox(self.janela_cadastro, textvariable=v, background='navajowhite2', state='readonly')
        self.cbx_sexo['values'] = ('Masculino', 'Feminino', 'Indefinido')

        self.lbl_nome.pack()
        self.ent_nome.pack()
        self.lbl_classe.pack()
        self.cbx_classe.pack()
        self.lbl_especie.pack()
        self.cbx_especie.pack()
        self.lbl_sexo.pack()
        self.cbx_sexo.pack()

        # botões
        self.lbl_x = tk.Label(self.janela_cadastro, text='', background='#696969')
        self.btn_confirmar = tk.Button(self.janela_cadastro, text='Confirmar', command=self.confirmar_cadastro, bg='DarkGray',fg='black', font=' Constantia 12 bold italic', relief="groove")
        self.btn_cancelar = tk.Button(self.janela_cadastro, text='Cancelar', command=self.cancelar,bg='DarkGray',fg='black', font=' Constantia 12 bold italic', relief="groove")

        self.lbl_x.pack()
        self.btn_confirmar.pack()
        self.btn_cancelar.pack()

    def confirmar_cadastro(self):
        nome    = self.ent_nome.get()
        classe  = self.cbx_classe.get()
        especie = self.cbx_especie.get()
        sexo    = self.cbx_sexo.get()

        if nome == '' or classe == '' or especie == '' or sexo == '':
            messagebox.showwarning('Aviso', 'Todos os dados são obrigatórios!')
        elif len(nome) > 13:
            messagebox.showwarning('Aviso', 'Só é permitido somente 13 caracteres!')
        else:
            # Classes
            if classe == "Espadachim":
                ATK_c = 50
                DEF_c = 100
                HP_c  = 150
            elif classe == "Atirador":
                ATK_c = 100
                DEF_c = 100
                HP_c  = 100
            elif classe == "Inventor":
                ATK_c = 20
                DEF_c = 180
                HP_c  = 200
            elif classe == "Assassino":
                ATK_c = 90
                DEF_c = 100
                HP_c  = 110
            elif classe == "Xamã":
                ATK_c = 50
                DEF_c = 50
                HP_c  = 200
            elif classe == "Lutador":
                ATK_c = 50
                DEF_c = 150
                HP_c  = 150
            else:
                ATK_c = 20
                DEF_c = 100
                HP_c  = 180

            # especie
            if especie == "Humano":
                ATK_e = 50
                DEF_e = 100
                HP_e  = 150
            elif especie == "Elfo":
                ATK_e = 50
                DEF_e = 70
                HP_e  = 180
            elif especie == "Anão":
                ATK_e = 50
                DEF_e = 125
                HP_e  = 125
            elif especie == "Minotauro":
                ATK_e = 90
                DEF_e = 100
                HP_e  = 110
            elif especie == "Gnomo":
                ATK_e = 50
                DEF_e = 50
                HP_e  = 200
            elif especie == "Fada":
                ATK_e = 60
                DEF_e = 20
                HP_e  = 220
            else:
                ATK_e = 40
                DEF_e = 140
                HP_e  = 120

            ATK_total = ATK_c + ATK_e
            DEF_total = DEF_c + DEF_e
            HP_total  = HP_c + HP_e

            bd.inserir("Bancos/Banco.db", "saude", ["HP"],[""f'{HP_total}'""])
            bd.inserir("Bancos/Banco.db", "guilda", ["XP","Nome","Moradia","Roupas","Armas","Itens","Money"],["0",""f'{nome}'"","Moradia:","Roupas:","Armas:","Itens:","500"])
            bd.inserir("Bancos/Banco.db", "personagens", ["LVL","Nome", "Classe", "Espécie", "Sexo", "ATK", "DEF", "HP"],
                       ["1", ""f'{nome}'"", ""f'{classe}'"", ""f'{especie}'"", ""f'{sexo}'"",
                        ""f'{ATK_total}'"",""f'{DEF_total}'"", ""f'{HP_total}'""])
            self.atualizar_tvw()
            messagebox.showinfo('Aviso', f'O/A {nome} foi criado/a com sucesso!')
            self.janela_cadastro.destroy()
            self.janela_principal.deiconify()

    def cancelar(self):
        self.janela_cadastro.destroy()
        self.janela_principal.deiconify()

    def atualizar_tvw(self):
        for i in self.tvw_menu.get_children():
            self.tvw_menu.delete(i)
        query = 'SELECT * FROM personagens;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_menu.insert('', tk.END, values=tupla)