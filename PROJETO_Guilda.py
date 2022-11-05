import tkinter as tk
from tkinter import ttk
import PROJETO_BD_GERAL as bd
from PIL import ImageTk, Image
from tkinter import messagebox

class Tela_Guilda():
    def __init__(self, master, janela_principal, tvw):
        self.janela_guilda = master
        self.banco_de_dados = "Bancos/Banco.db"
        self.janela_guilda.overrideredirect(True)
        self.tvw_guilda = tvw
        self.janela_guilda.title('Guildas')
        self.janela_guilda['background'] = '#CCCCCC'
        self.janela_guilda.grab_set()
        self.janela_principal = janela_principal
        self.janela_guilda.resizable(False, False)

        #CENTRALIZAR
        window_height = 670
        window_width = 1050
        screen_width = self.janela_guilda.winfo_screenwidth()
        screen_height = self.janela_guilda.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_guilda.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Frame
        self.frm_total = tk.Frame(self.janela_guilda, background='#CCCCCC')
        self.frm_total.pack(side=tk.TOP)

        # cabeçalho
        colunas = ['id', 'lvl', 'nome', 'moradia', 'roupas', 'armas', 'itens', 'money']
        self.tvw_guilda = ttk.Treeview(self.janela_guilda, show='headings', columns=colunas, height=45)
        G = ttk.Style()
        G.theme_use('clam')
        G.configure('Treeview', background="navajowhite2", foreground="black", font=('Constantia 10 bold italic'))
        self.tvw_guilda.heading('id', text='ID')
        self.tvw_guilda.heading('lvl', text='XP')
        self.tvw_guilda.heading('nome', text='Nome')
        self.tvw_guilda.heading('moradia', text="Moradia")
        self.tvw_guilda.heading('roupas', text="Roupas")
        self.tvw_guilda.heading('armas', text="Armas")
        self.tvw_guilda.heading('itens', text='itens')
        self.tvw_guilda.heading('money', text='Money')

        self.tvw_guilda.column('id', minwidth=0, width=30)
        self.tvw_guilda.column('lvl', minwidth=0, width=100)
        self.tvw_guilda.column('nome', minwidth=0, width=100)
        self.tvw_guilda.column('moradia', minwidth=0, width=100)
        self.tvw_guilda.column('roupas', minwidth=0, width=100)
        self.tvw_guilda.column('armas', minwidth=0, width=100)
        self.tvw_guilda.column('itens', minwidth=0, width=100)
        self.tvw_guilda.column('money', minwidth=0, width=100)

        self.scr = tk.Scrollbar(self.janela_guilda, command=self.tvw_guilda.yview)
        self.tvw_guilda.configure(yscroll=self.scr.set)

        self.scr.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.tvw_guilda.pack(side=tk.RIGHT, fill=tk.BOTH)

        for i in bd.consultar_guilda(bd.sql_consultar_guilda):
            self.tvw_guilda.insert('', 'end', values=(i))

        #Logo
        self.logo = ImageTk.PhotoImage(Image.open("Imagens/guildas.png"))
        self.lbl_logo = tk.Label(self.janela_guilda, text='', background='#CCCCCC', image=self.logo)
        self.lbl_logo.pack()

        #Layout
        self.lbl_cliente = tk.Label(self.janela_guilda, text='Aventureiro', background='#CCCCCC', font=' Constantia 12 bold italic')

        self.lista_personagens = bd.consultar_coluna("Bancos/Banco.db", "Personagens", "Nome", False)
        self.lista_aux = []
        for i in self.lista_personagens:
            self.lista_aux.append(i[0])

        v = tk.StringVar
        self.cbx_personagem = ttk.Combobox(self.janela_guilda, textvariable=v, background='#CCCCCC', state='readonly')
        self.cbx_personagem['values'] = self.lista_aux
        #moradia
        self.lbl_ser = tk.Label(self.janela_guilda, text='Moradia', background='#CCCCCC', font=' Constantia 10')
        v = tk.StringVar
        self.cbx_moradia = ttk.Combobox(self.janela_guilda, textvariable=v, background='#CCCCCC', state='readonly')
        self.cbx_moradia['values'] = ('Alojamento(Pobre)', 'Alojamento(Média)', 'Alojamento(Rica)')
        #roupas
        self.lbl_roupa = tk.Label(self.janela_guilda, text='Guilda de roupas', background='#CCCCCC', font=' Constantia 10')
        v = tk.StringVar
        self.cbx_roupa = ttk.Combobox(self.janela_guilda, textvariable=v, background='#CCCCCC', state='readonly')
        self.cbx_roupa['values'] = ('Casaco de lobo', 'Blusa de algodão', 'Manto de urso')
        #armas
        self.lbl_armas = tk.Label(self.janela_guilda, text='Guilda de armas', background='#CCCCCC', font=' Constantia 10')
        v = tk.StringVar
        self.cbx_armas = ttk.Combobox(self.janela_guilda, textvariable=v, background='#CCCCCC', state='readonly')
        self.cbx_armas['values'] = ('Adaga' , 'Lança' , 'Espada' , 'Arco' , 'Foice' , 'Besta')
        #itens
        self.lbl_itens = tk.Label(self.janela_guilda, text='Guilda de itens', background='#CCCCCC', font=' Constantia 10')
        v = tk.StringVar
        self.cbx_itens = ttk.Combobox(self.janela_guilda, textvariable=v, background='#CCCCCC', state='readonly')
        self.cbx_itens['values'] = ('Mochila' , 'Óleo' , 'Ampulheta' , 'Luneta' , 'Anzol' , 'Baú')
        #evolução
        self.lbl_lvl = tk.Label(self.janela_guilda, text='Salão da evolução', background='#CCCCCC', font=' Constantia 10')
        self.lbl_cliente.pack()
        v = tk.StringVar
        self.cbx_elu = ttk.Combobox(self.janela_guilda, textvariable=v, background='#CCCCCC', state='readonly', width='5')
        self.cbx_elu['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')

        #Imagens
        self.fechar_loja= ImageTk.PhotoImage(Image.open("Imagens/exit_loja.png"))
        self.minha_loja = tk.PhotoImage(file="Imagens/menu_loja.png")
        self.info = ImageTk.PhotoImage(Image.open("Imagens/information.png"))

        #Botões
        self.lbl_x = tk.Label(self.janela_guilda, text='', background='#CCCCCC')
        self.btn_informaçoes = tk.Button(self.janela_guilda, text='informações',image=self.info, bg='#CCCCCC',borderwidth=0, command=self.tela_loja)
        self.lbl_z = tk.Label(self.janela_guilda, text='', background='#CCCCCC')
        self.btn_confirmar = tk.Button(self.janela_guilda, text='Comprar', bg='#CCCCCC',
                                       fg='black', font=' Constantia 12 bold italic', relief="groove", command=self.Comprar)
        self.btn_cancelar = tk.Button(self.janela_guilda, text='Cancelar', command=self.cancelar, bg='#CCCCCC',
                                      fg='black', font=' Constantia 12 bold italic', relief="groove")

        self.cbx_personagem.pack()
        self.lbl_ser.pack()
        self.cbx_moradia.pack()
        self.lbl_roupa.pack()
        self.cbx_roupa.pack()
        self.lbl_armas.pack()
        self.cbx_armas.pack()
        self.lbl_itens.pack()
        self.cbx_itens.pack()
        self.lbl_lvl.pack()
        self.cbx_elu.pack()
        self.lbl_x.pack()
        self.btn_informaçoes.pack()
        self.lbl_z.pack()
        self.btn_confirmar.pack()
        self.btn_cancelar.pack()

    def Comprar(self):
        self.selecione_nome    = self.cbx_personagem.get()
        self.selecione_moradia = self.cbx_moradia.get()
        self.selecione_roupas  = self.cbx_roupa.get()
        self.selecione_armas   = self.cbx_armas.get()
        self.selecione_itens   = self.cbx_itens.get()
        self.selecione_elv     = self.cbx_elu.get()

        self.selecione_valores = bd.consulta_por_valor(self.banco_de_dados, "guilda", "Nome", self.selecione_nome)
        self.selecione_valores_per = bd.consulta_por_valor(self.banco_de_dados, "personagens", "Nome", self.selecione_nome)

        self.id          = self.selecione_valores[0][0]
        self.xp          = self.selecione_valores[0][1]
        self.nome        = self.selecione_valores[0][2]
        self.Moradia     = self.selecione_valores[0][3]
        self.roupas      = self.selecione_valores[0][4]
        self.armas       = self.selecione_valores[0][5]
        self.itens       = self.selecione_valores[0][6]
        self.money       = self.selecione_valores[0][7]
        self.ataque      = self.selecione_valores_per[0][6]
        self.defesa      = self.selecione_valores_per[0][7]


        if self.money <= 0:
            messagebox.showwarning('Aviso', f'O/A {self.nome} não tem money suficiente!')
        else:
            if self.selecione_moradia == "Alojamento(Pobre)":
                self.valor_total_m1 = self.money - 100
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Moradia'],[""f'{self.selecione_moradia}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Money'], [""f'{self.valor_total_m1}'""])
                self.atualizar_tvw_guilda()
            elif self.selecione_moradia == "Alojamento(Média)":
                self.valor_total_m2 = self.money - 250
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Moradia'],[""f'{self.selecione_moradia}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Money'], [""f'{self.valor_total_m2}'""])
                self.atualizar_tvw_guilda()
            else:
                self.valor_total_m3 = self.money - 500
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Moradia'],[""f'{self.selecione_moradia}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Money'], [""f'{self.valor_total_m3}'""])
                self.atualizar_tvw_guilda()
            #Roupa
            if self.selecione_roupas == "Casaco de lobo":
                self.valor_total_r1 = self.money - 25
                self.valor_total_def = self.defesa + 25
                bd.atualizar(self.banco_de_dados, "guilda",""f'{self.id}'"", ['Money'], [""f'{self.valor_total_r1}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Roupas'], [""f'{self.selecione_roupas}'""])
                bd.atualizar(self.banco_de_dados, "personagens", ""f'{self.id}'"", ['DEF'], [""f'{self.valor_total_def}'""])
                self.atualizar_tvw_guilda()
            elif self.selecione_roupas == "Blusa de algodão":
                self.valor_total_r2 = self.money - 50
                self.valor_total_def = self.defesa + 50
                bd.atualizar(self.banco_de_dados, "guilda",""f'{self.id}'"", ['Money'], [""f'{self.valor_total_r2}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Roupas'], [""f'{self.selecione_roupas}'""])
                bd.atualizar(self.banco_de_dados, "personagens", ""f'{self.id}'"", ['DEF'], [""f'{self.valor_total_def}'""])
                self.atualizar_tvw_guilda()
            else:
                self.valor_total_r3 = self.money - 100
                self.valor_total_def = self.defesa + 100
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Money'], [""f'{self.valor_total_r3}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Roupas'], [""f'{self.selecione_roupas}'""])
                bd.atualizar(self.banco_de_dados, "personagens", ""f'{self.id}'"", ['DEF'], [""f'{self.valor_total_def}'""])
                self.atualizar_tvw_guilda()
            #Armas
            if self.selecione_armas == "Adaga" or "Lança" or "Espada" or "Arco" or "Foice" or "Besta":
                self.valor_total_armas = self.money - 100
                self.valor_total_atk = self.ataque + 100
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Money'], [""f'{self.valor_total_armas}'""])
                bd.atualizar(self.banco_de_dados, "guilda",""f'{self.id}'"", ['Armas'], [""f'{self.selecione_armas}'""])
                bd.atualizar(self.banco_de_dados, "personagens", ""f'{self.id}'"", ['ATK'], [""f'{self.valor_total_atk}'""])
                self.atualizar_tvw_guilda()
            #Itens
            if self.selecione_roupas == "Mochila" or "Óleo" or "Ampulheta" or "Luneta" or "Anzol" or "Baú":
                self.valor_total_itens = self.money - 20
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Money'], [""f'{self.valor_total_itens}'""])
                bd.atualizar(self.banco_de_dados, "guilda", ""f'{self.id}'"", ['Itens'], [""f'{self.selecione_itens}'""])
                self.atualizar_tvw_guilda()
            #Level
            if self.selecione_elv == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14" or "15" or"16" or "17" or "18" or "19" or "20" :
                if self.xp <= 0:
                    messagebox.showwarning('Aviso', f'O/A {self.nome} não tem xp suficiente!')
                else:
                    bd.atualizar(self.banco_de_dados, "personagens", ""f'{self.id}'"", ['LVL'], [""f'{self.selecione_elv}'""])

    def tela_loja(self):
        self.janela_guilda.withdraw()
        self.janela_loja = tk.Toplevel()
        self.janela_loja.overrideredirect(True)
        self.janela_loja.grab_set()
        self.janela_loja.title("©𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮")
        self.janela_loja['background'] = '#CCCCCC'
        self.janela_loja.resizable(False, False)
        #CENTRALIZAR
        window_height = 650
        window_width = 800
        screen_width = self.janela_loja.winfo_screenwidth()
        screen_height = self.janela_loja.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_loja.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        #Mapa e Botões
        self.lbl_mapa = tk.Label(self.janela_loja, image=self.minha_loja, relief="solid")
        self.lbl_mapa.image = self.minha_loja
        self.btn_mapa = tk.Button(self.janela_loja, text='', image=self.fechar_loja, command=self.voltar_loja, bg='#CCCCCC', borderwidth=0)

        self.lbl_mapa.pack()
        self.btn_mapa.pack(side=tk.BOTTOM)

    def voltar_loja(self):
        self.janela_loja.destroy()
        self.janela_guilda.deiconify()

    def cancelar(self):
        self.janela_guilda.destroy()
        self.janela_principal.deiconify()

    def atualizar_tvw_menu(self):
        for i in self.tvw_menu.get_children():
            self.tvw_menu.delete(i)
        query1 = 'SELECT * FROM personagens;'
        dados1 = bd.consultar(query1)
        for tupla1 in dados1:
            self.tvw_menu.insert('', tk.END, values=tupla1)

    def atualizar_tvw_guilda(self):
        for i in self.tvw_guilda.get_children():
            self.tvw_guilda.delete(i)
        query = 'SELECT * FROM guilda;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_guilda.insert('', tk.END, values=tupla)