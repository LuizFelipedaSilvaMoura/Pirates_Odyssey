import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import webbrowser
import PROJETO_BD_GERAL as bd
from PROJETO_Informações import  Tela_Regras
from PROJETO_Combate import TelaCombate
from PROJETO_Ajuda import Tela_Ajuda
from PROJETO_Entrar import TelaCliente
from PROJETO_Cadastro import Tela_cadastrar
from PROJETO_Atualizar import Tela_atualizar
from PROJETO_Dados import Tela_Dados
from PROJETO_Guilda import Tela_Guilda

class Tela_Principal:
    def __init__(self, master):
        self.janela_principal = master
        self.janela_principal.overrideredirect(True)
        self.janela_principal.title("© 𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮")
        self.janela_principal['background'] = 'navajowhite3'
        self.banco_de_dados = "Bancos/Banco.db"
        self.janela_principal.resizable(False, False)

        #CENTRALIZAR
        window_height = 300
        window_width = 580
        screen_width = self.janela_principal.winfo_screenwidth()
        screen_height = self.janela_principal.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_principal.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Janela de LOGIN
        self.tela_entrar()
        self.janela_principal.withdraw()

        #Frame
        self.frm_botoes = tk.Frame(self.janela_principal)
        self.frm_botoes.pack(side=tk.BOTTOM)
        self.barra = tk.Menu(self.janela_principal)

        #Menu_RPG
        self.menu1 = tk.Menu(self.barra, tearoff=False, background='lightcyan')
        self.barra.add_cascade(label='⚙ RPG', menu=self.menu1)
        self.menu1.add_command(label='_História', command=lambda:webbrowser.open_new('https://drive.google.com/file/d/1T_KybeO97RQ_3Fa5FRcgTJ7a78V5Xonc/view?usp=sharing'))
        self.menu1.add_command(label='_Informações', command=self.Tela_Regras)
        self.menu1.add_command(label='_Combate', command=self.simule)
        self.menu1.add_command(label='_Mapa', command=self.tela_mapa)
        self.menu1.add_command(label='_Dados', command=self.dados)
        self.menu1.add_command(label='_Guildas', command=self.Tela_Guilda)

        self.janela_principal.config(menu=self.barra)
        #Menu_Opções
        self.menu2 = tk.Menu(self.barra, tearoff=False, background='lightcyan')
        self.barra.add_cascade(label='⚙ OPÇÕES', menu=self.menu2)
        self.menu2.add_command(label='_Legenda', command=self.legenda)
        self.menu2.add_command(label='_Ajuda',command=self.tela_ajuda)
        self.menu2.add_command(label='_Sair', command=self.sair)
        self.janela_principal.config(menu=self.barra)

        #Cabeçalho
        colunas = ['id','lvl', 'nome', 'classe', 'especie', 'sexo','atk', 'def', 'hp']
        self.tvw_menu = ttk.Treeview(self.janela_principal, show='headings', columns=colunas, height=5)
        self.tvw_menu.pack(side=tk.LEFT, fill=tk.BOTH)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', background="navajowhite2", foreground="black", font=('Constantia 10 bold italic'))
        self.tvw_menu.heading('id', text='ID')
        self.tvw_menu.heading('lvl', text='LVL')
        self.tvw_menu.heading('nome', text='Nome')
        self.tvw_menu.heading('classe', text="Classe")
        self.tvw_menu.heading('especie', text="Espécie")
        self.tvw_menu.heading('sexo', text="Sexo")
        self.tvw_menu.heading('atk', text='ATK')
        self.tvw_menu.heading('def', text='DEF')
        self.tvw_menu.heading('hp', text='HP')

        self.tvw_menu.column('id', minwidth=0, width=30)
        self.tvw_menu.column('lvl', minwidth=0, width=30)
        self.tvw_menu.column('nome', minwidth=0, width=100)
        self.tvw_menu.column('classe', minwidth=0, width=100)
        self.tvw_menu.column('especie', minwidth=0, width=100)
        self.tvw_menu.column('sexo', minwidth=0, width=100)
        self.tvw_menu.column('atk', minwidth=0, width=35)
        self.tvw_menu.column('def', minwidth=0, width=35)
        self.tvw_menu.column('hp', minwidth=0, width=35)

        self.scr = tk.Scrollbar(self.janela_principal, command=self.tvw_menu.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_menu.configure(yscroll=self.scr.set)

        for i in bd.consultar(bd.sql_consultar):
            self.tvw_menu.insert('', 'end', values=(i))

        #imagem
        self.img_cadastrar = ImageTk.PhotoImage(Image.open("Imagens/cadastro.png"))
        self.img_deletar = ImageTk.PhotoImage(Image.open("Imagens/botao-de-deletar.png"))
        self.img_atualizar = ImageTk.PhotoImage(Image.open("Imagens/atualizar.png"))
        self.img_fechar_mapa= ImageTk.PhotoImage(Image.open("Imagens/fechar_mapa.png"))
        self.img_descansar= ImageTk.PhotoImage(Image.open("Imagens/house.png"))
        self.img_mapa = tk.PhotoImage(file="Imagens/Mapa.png")


        # botoes
        self.btn_cadastrar = tk.Button(self.frm_botoes, text='Cadastrar', command=self.tela_cadastrar, bg ='navajowhite3', image=self.img_cadastrar, borderwidth=0)
        self.btn_deletar = tk.Button(self.frm_botoes, text='Deletar', command=self.deletar_selecionado, bg ='navajowhite3', image=self.img_deletar, borderwidth=0)
        self.btn_atualizar = tk.Button(self.frm_botoes, text='Atualizar', bg ='navajowhite3', image=self.img_atualizar, borderwidth=0, command=self.tela_atualizar)
        self.btn_descansar = tk.Button(self.frm_botoes, text='Descansar', bg ='navajowhite3', image=self.img_descansar, borderwidth=0, command=self.descansar)

        self.btn_cadastrar.pack(side=tk.LEFT)
        self.btn_deletar.pack(side=tk.LEFT)
        self.btn_atualizar.pack(side=tk.LEFT)
        self.btn_descansar.pack(side=tk.LEFT)

    def tela_mapa(self):
        self.janela_principal.withdraw()
        self.janela_mapa = tk.Toplevel()
        self.janela_mapa.overrideredirect(True)
        self.janela_mapa.grab_set()
        self.janela_mapa.title("©𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮")
        self.janela_mapa['background'] = '#d3ccbf'
        self.janela_mapa.resizable(False, False)
        #CENTRALIZAR
        window_height = 555
        window_width = 900
        screen_width = self.janela_mapa.winfo_screenwidth()
        screen_height = self.janela_mapa.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_mapa.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        #Mapa e Botões
        self.lbl_mapa = tk.Label(self.janela_mapa, image=self.img_mapa, relief="solid")
        self.lbl_mapa.image = self.img_mapa
        self.btn_mapa = tk.Button(self.janela_mapa, text='', image=self.img_fechar_mapa, command=self.Voltar_mapa, bg='#d3ccbf', borderwidth=0)

        self.lbl_mapa.pack()
        self.btn_mapa.pack(side=tk.BOTTOM)

    def Voltar_mapa(self):
        self.janela_mapa.destroy()
        self.janela_principal.deiconify()

    #Funções da tela principal
    def deletar_selecionado(self):
        selecionado = self.tvw_menu.selection()
        if len(selecionado) != 1:
            messagebox.showwarning('Aviso', 'Selecione um personagem.')
        else:
            id = self.tvw_menu.item(selecionado, 'values')[0]
            Nome = self.tvw_menu.item(selecionado, 'values')[2]
            if messagebox.askyesno('Aviso', f'Confirma a remoção do/a {Nome}?'):
                bd.deletar_linha("Bancos/Banco.db", "saude", id)
                bd.deletar_linha("Bancos/Banco.db", "personagens", id)
                bd.deletar_linha("Bancos/Banco.db", "guilda", id)
                self.atualizar_tvw()
                messagebox.showinfo('Aviso', f'O/A {Nome} foi removido/a com sucesso!')

    def tela_cadastrar(self):
        self.janela_principal.withdraw()
        topcadastro = tk.Toplevel(self.janela_principal)
        Tela_cadastrar(topcadastro, self.janela_principal, self.tvw_menu)

    def tela_atualizar(self):
        self.selecionado = self.tvw_menu.selection()
        if len(self.selecionado) != 1:
            messagebox.showwarning('Aviso', 'Selecione um personagem.')
        else:
            self.janela_principal.withdraw()
            topatualizar = tk.Toplevel(self.janela_principal)
            Tela_atualizar(topatualizar, self.janela_principal, self.tvw_menu)
    def descansar(self):
        self.selecionado = self.tvw_menu.selection()
        if len(self.selecionado) != 1:
            messagebox.showwarning('Aviso', 'Selecione um personagem.')
        else:
            self.id = self.tvw_menu.item(self.selecionado, 'values')[0]
            self.nome = self.tvw_menu.item(self.selecionado, 'values')[2]
            self.saude = bd.consulta_por_valor(self.banco_de_dados, "saude", "id", ""f'{self.id}'"")
            self.valor_saude = self.saude[0][1]
            bd.atualizar(self.banco_de_dados, "personagens", ""f'{self.id}'"", ['HP'], [""f'{self.valor_saude}'""])
            self.atualizar_tvw()
            messagebox.showwarning('Aviso', f'O/A {self.nome} descansou e curou todos os seus ferimentos')

    #Funções do menu RPG
    def Tela_Guilda(self):
        self.janela_principal.withdraw()
        toploja = tk.Toplevel(self.janela_principal)
        Tela_Guilda(toploja, self.janela_principal, self.tvw_menu)

    def simule(self):
        self.janela_principal.withdraw()
        topcombate = tk.Toplevel(self.janela_principal)
        TelaCombate(topcombate, self.janela_principal, self.tvw_menu)

    def dados(self):
        topdados = tk.Toplevel(self.janela_principal)
        Tela_Dados(topdados, self.janela_principal)

    def tela_entrar(self):
        topentrar = tk.Toplevel(self.janela_principal)
        TelaCliente(topentrar, self.janela_principal)

    def Tela_Regras(self):
        self.janela_principal.withdraw()
        topregras = tk.Toplevel(self.janela_principal)
        Tela_Regras(topregras, self.janela_principal)

    #Funções do menu Opções
    def legenda(self):
        messagebox.showinfo('Legenda','LVL = NIVEL\n\nATK = ATAQUE\n\nDEF = DEFESA\n\nHP = VIDA')

    def tela_ajuda(self):
        self.janela_principal.withdraw()
        toprajuda = tk.Toplevel(self.janela_principal)
        Tela_Ajuda(toprajuda, self.janela_principal)

    def sair(self):
        rar = messagebox.askyesno('EXIT', 'Quer realmente sair da aventura?')
        if rar == True:
            exit()

    def atualizar_tvw(self):
        for i in self.tvw_menu.get_children():
            self.tvw_menu.delete(i)
        query = 'SELECT * FROM personagens;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_menu.insert('', tk.END, values=tupla)

#Janela central
app = tk.Tk()
Tela_Principal(app)
app.mainloop()
