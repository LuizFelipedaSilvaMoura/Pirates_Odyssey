import tkinter as tk
from tkinter import ttk
import  PROJETO_BD_GERAL as bd
from tkinter import messagebox
from PIL import ImageTk, Image


class Tela_atualizar():

    def __init__(self, master, janela_principal,tvw):
        self.janela_atualizar = master
        self.tvw_menu = tvw
        self.janela_atualizar.overrideredirect(True)
        self.janela_atualizar.title('Atualizar')
        self.janela_atualizar['background'] = 'aqua'
        self.janela_atualizar.grab_set()
        self.janela_principal = janela_principal
        self.janela_atualizar.resizable(False, False)

        #CENTRALIZAR
        window_height = 420
        window_width = 210
        screen_width = self.janela_atualizar.winfo_screenwidth()
        screen_height = self.janela_atualizar.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_atualizar.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Imagem
        self.cadastrar = ImageTk.PhotoImage(Image.open("Imagens/atu.png"))
        self.info = tk.Label(self.janela_atualizar, text='', bg='aqua', image=self.cadastrar)

        #Layout
        self.lbl_nome = tk.Label(self.janela_atualizar, text='Nome:', background='aqua')
        self.ent_nome = tk.Entry(self.janela_atualizar, width=23, background='AliceBlue')

        self.lbl_classe = tk.Label(self.janela_atualizar, text='Classe:', background='aqua')
        v = tk.StringVar
        self.cbx_classe = ttk.Combobox(self.janela_atualizar, textvariable=v, background='aqua', state='readonly')
        self.cbx_classe['values'] = ('Espadachim', 'Atirador', 'Inventor', 'Assassino', 'Xamã', 'Lutador', 'Bardo')

        self.lbl_especie = tk.Label(self.janela_atualizar, text='Espécie:', background='aqua')
        v = tk.StringVar
        self.cbx_especie = ttk.Combobox(self.janela_atualizar, textvariable=v, background='aqua', state='readonly')
        self.cbx_especie['values'] = ('Humano', 'Elfo', 'Anão', 'Minotauro', 'Gnomo', 'Fada', 'Dragonborn ')

        self.lbl_sexo = tk.Label(self.janela_atualizar, text='Sexo:', background='aqua')
        v = tk.StringVar
        self.cbx_sexo = ttk.Combobox(self.janela_atualizar, textvariable=v, background='aqua',state='readonly')
        self.cbx_sexo['values'] = ('Masculino', 'Feminino', 'Indefinido')

        self.info.pack()
        self.lbl_nome.pack()
        self.ent_nome.pack()
        self.lbl_classe.pack()
        self.cbx_classe.pack()
        self.lbl_especie.pack()
        self.cbx_especie.pack()
        self.lbl_sexo.pack()
        self.cbx_sexo.pack()

        self.selecionado = self.tvw_menu.selection()
        self.ent_nome.insert   (0, self.tvw_menu.item(self.selecionado, 'values')[2])

        #Botões
        self.lbl_x = tk.Label(self.janela_atualizar, text='', background='aqua')
        self.btn_confirmar = tk.Button(self.janela_atualizar, text='Confirmar', command=self.atualizar_per,bg='DarkTurquoise',fg='black', font=' Constantia 12 bold italic', relief="groove")
        self.btn_cancelar = tk.Button(self.janela_atualizar, text='Cancelar', command=self.cancelar_atu, bg='DarkTurquoise',fg='black', font=' Constantia 12 bold italic', relief="groove")

        self.lbl_x.pack()
        self.btn_confirmar.pack()
        self.btn_cancelar.pack()

    def cancelar_atu(self):
        self.janela_atualizar.destroy()
        self.janela_principal.deiconify()

    def atualizar_per(self):
        nome    = self.ent_nome.get()
        classe  = self.cbx_classe.get()
        especie = self.cbx_especie.get()
        sexo    = self.cbx_sexo.get()

        #Classes
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

        #Especie
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

        self.selecionado = self.tvw_menu.selection()
        id = self.tvw_menu.item(self.selecionado, 'values')[0]
        bd.atualizar("Bancos/Banco.db", "personagens", ""f'{id}'"", ['Nome','Classe','Espécie','Sexo','ATK','DEF','HP'],
                     [""f'{nome}'"",""f'{classe}'"",""f'{especie}'"",""f'{sexo}'"",""f'{ATK_total}'"",""f'{DEF_total}'"",""f'{HP_total}'""])
        bd.atualizar("Bancos/Banco.db", "saude", ""f'{id}'"",['HP'],[""f'{HP_total}'""])
        self.atualizar_tvw()
        self.janela_atualizar.destroy()
        self.janela_principal.deiconify()
        messagebox.showinfo('Aviso', f'O/A {nome} entrou em nova fase de sua vida!')

    def atualizar_tvw(self):
        for i in self.tvw_menu.get_children():
            self.tvw_menu.delete(i)
        query = 'SELECT * FROM personagens;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_menu.insert('', tk.END, values=tupla)