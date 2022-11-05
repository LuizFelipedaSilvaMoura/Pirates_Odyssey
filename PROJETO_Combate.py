import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import PROJETO_BD_GERAL as bd

class TelaCombate:
    def __init__(self, master, janela_principal, tvw):
        self.banco_de_dados = "Bancos/Banco.db"
        self.janela_combate = master
        self.tvw_menu = tvw
        self.janela_combate.overrideredirect(True)
        self.janela_combate.grab_set()
        self.janela_combate.title('Simulador de combate')
        self.janela_combate.geometry('200x420')
        self.janela_combate['background'] = '#8b0000'
        self.janela_principal = janela_principal
        self.janela_combate.resizable(False, False)

        #CENTRALIZAR
        window_height = 350
        window_width  = 220
        screen_width  = self.janela_combate.winfo_screenwidth()
        screen_height = self.janela_combate.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_combate.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #Frame
        self.frm_botoes = tk.Frame(self.janela_combate, background='#8b0000')
        self.frm_botoes.pack(side=tk.BOTTOM)

        # imagem
        self.log = ImageTk.PhotoImage(Image.open("Imagens/combate.png"))
        self.lbl_imagem = tk.Label(self.janela_combate, text='', bg='#8b0000', image=self.log)
        self.lbl_imagem.pack()

        #Layout
        v1 = tk.StringVar
        v2 = tk.StringVar

        self.cbx_nome1 = ttk.Combobox(self.janela_combate, textvariable=v1, background='#FEBD59', state='readonly')
        self.cbx_nome2 = ttk.Combobox(self.janela_combate,  textvariable=v2, background='#FEBD59', state='readonly')
        self.lbl_text1 = tk.Label(self.janela_combate, text='Primeiro combatente', bg='#8b0000', fg='#FEBD59',font=' Constantia 12 bold italic')
        self.lbl_text2 = tk.Label(self.janela_combate, text='Segundo combatente', bg='#8b0000', fg='#FEBD59',font=' Constantia 12 bold italic')

        self.lbl_text1.pack()
        self.cbx_nome1.pack()
        self.lbl_text2.pack()
        self.cbx_nome2.pack()

        #Tupla =========================================================================================================
        self.aux_pers = bd.consultar_coluna(self.banco_de_dados,'personagens','Nome')
        self.aux_NPC  = bd.consultar_coluna(self.banco_de_dados,'NPC','Nome')

        #Lista =========================================================================================================
        self.lista_pers  = []
        self.lista_NPC   = []
        self.lista_todos = []
        for i in self.aux_pers:
            self.lista_pers.append(i[0])
        for i in self.aux_NPC:
            self.lista_NPC.append(i[0])

        self.lista_todos = self.lista_pers+self.lista_NPC

        #Insert no combobox ============================================================================================
        self.cbx_nome1['values'] = self.lista_todos
        self.cbx_nome2['values'] = self.lista_todos

        self.tipo_do_1 = ''
        self.tipo_do_2 = ''

        self.lbl_Val     = tk.Label (self.janela_combate, text='', bg='#8b0000')
        self.btn_simular = tk.Button(self.frm_botoes, text='Avançar', bg='#8b0000', fg='#FEBD59',command=self.simular,font=' Constantia 15 bold ', relief="flat")
        self.btn_voltar  = tk.Button(self.frm_botoes, text='Voltar', bg='#8b0000', fg='#FEBD59',font=' Constantia 15 bold ', command=self.voltar, relief="flat")

        self.lbl_Val.pack()
        self.btn_simular.pack()
        self.btn_voltar.pack()

    def voltar(self):
        self.atualizar_tvw()
        self.janela_combate.destroy()
        self.janela_principal.deiconify()
        bd.atualizar("Bancos/Banco.db", "NPC", "1", ['HP'], ["100"],)
        bd.atualizar("Bancos/Banco.db", "NPC", "2", ['HP'], ["450"],)
        bd.atualizar("Bancos/Banco.db", "NPC", "3", ['HP'], ["80"],)
        bd.atualizar("Bancos/Banco.db", "NPC", "4", ['HP'], ["600"],)
        bd.atualizar("Bancos/Banco.db", "NPC", "5", ['HP'], ["600"],)
        bd.atualizar("Bancos/Banco.db", "NPC", "6", ['HP'], ["800"],)
        bd.atualizar("Bancos/Banco.db", "NPC", "7", ['HP'], ["100"],)

    def simular(self):
        var1 = self.cbx_nome1.get()
        var2 = self.cbx_nome2.get()

        if(var1 in self.lista_pers):
            self.tipo_do_1 = "personagens"
        else:
            self.tipo_do_1 = "NPC"

        if (var2 in self.lista_pers):
            self.tipo_do_2 = "personagens"
        else:
            self.tipo_do_2 = "NPC"

        # print(f'Tipo do {var1} = {self.tipo_do_1}')
        # print(f'Tipo do {var2} = {self.tipo_do_2}')

        if var1 == '' or var2 == '':
            messagebox.showwarning('Aviso', 'Todos os dados são obrigatórios!')
        elif var1 == var2 or var2 == var1:
            messagebox.showwarning('Aviso', 'Não pode lutar contra o mesmo invíduo!')
        else:
            self.nome1   = var1
            self.tupla1  = bd.consulta_por_valor(self.banco_de_dados, self.tipo_do_1, "Nome", var1)
            if(self.tipo_do_1 == "NPC"):
                self.id1     = self.tupla1[0][0]
                self.ataque1 = self.tupla1[0][6]
                self.defesa1 = self.tupla1[0][7]
                self.vida1   = self.tupla1[0][8]
            else:
                self.id1     = self.tupla1[0][0]
                self.ataque1 = self.tupla1[0][6]
                self.defesa1 = self.tupla1[0][7]
                self.vida1   = self.tupla1[0][8]
            self.nome2   = var2
            self.tupla2  = bd.consulta_por_valor(self.banco_de_dados, self.tipo_do_2, "Nome", var2)
            if (self.tipo_do_2 == "NPC"):
                self.id2     = self.tupla2[0][0]
                self.ataque2 = self.tupla2[0][6]
                self.defesa2 = self.tupla2[0][7]
                self.vida2   = self.tupla2[0][8]
            else:
                self.id2     = self.tupla2[0][0]
                self.ataque2 = self.tupla2[0][6]
                self.defesa2 = self.tupla2[0][7]
                self.vida2   = self.tupla2[0][8]

            '''print("Personagem 1")
            print("id: ", self.id1)
            print("Nome: ", self.nome1)
            print("ATK: ", self.ataque1)
            print("DEF: ", self.defesa1)
            print("HP: ", self.vida1)
            print("========================================")
            print("Personagem 2")
            print("id: ", self.id2)
            print("Nome: ", self.nome2)
            print("ATK: ", self.ataque2)
            print("DEF: ", self.defesa2)
            print("HP: ", self.vida2)'''

            if (self.tipo_do_1 == 'personagens' and self.tipo_do_2 == 'personagens'):
                 if self.ataque1 > self.defesa2:
                     self.defesa_dano = self.defesa2 - self.ataque1
                     self.ataque_dano = self.ataque1 - self.defesa2
                     if self.defesa_dano <= 0:
                         self.dano_total = self.vida2 - self.ataque_dano
                         if self.dano_total <= 0:
                             messagebox.showinfo("Resultado"," O "f'{var1}'" matou o "f'{var2}'"")
                             bd.atualizar("Bancos/Banco.db", "personagens", self.id2, ['HP'], ["0"])
                         else:
                             messagebox.showinfo("Resultado", " O "f'{var2}'" sobreviveu ao ataque do "f'{var1}'"")
                             bd.atualizar("Bancos/Banco.db", "personagens", self.id2, ['HP'], [""f'{self.dano_total}'""])
                 else:
                     messagebox.showinfo("Resultado", " O "f'{var2}'" defendeu o ataque do "f'{var1}'"")

            elif (self.tipo_do_1 == 'NPC' and self.tipo_do_2 == 'personagens'):
                 if self.ataque1 > self.defesa2:
                     self.defesa_dano = self.defesa2 - self.ataque1
                     self.ataque_dano = self.ataque1 - self.defesa2
                     if self.defesa_dano <= 0:
                         self.dano_total = self.vida2 - self.ataque_dano
                         if self.dano_total <= 0:
                             messagebox.showinfo("Resultado"," O "f'{var1}'" matou o "f'{var2}'"")
                             bd.atualizar("Bancos/Banco.db", "personagens", self.id2 , ['HP'], [""f'{self.dano_total}'""])
                         else:
                             messagebox.showinfo("Resultado", " O "f'{var2}'" sobreviveu ao ataque do "f'{var1}'"")
                             bd.atualizar("Bancos/Banco.db", "personagens", self.id2 , ['HP'], [""f'{self.dano_total}'""])
                 else:
                     messagebox.showinfo("Resultado", " O "f'{var2}'" defendeu o ataque do "f'{var1}'"")

            elif (self.tipo_do_1 == 'personagens' and self.tipo_do_2 == 'NPC'):
                 if self.ataque1 > self.defesa2:
                     self.defesa_dano = self.defesa2 - self.ataque1
                     self.ataque_dano = self.ataque1 - self.defesa2
                     if self.defesa_dano <= 0:
                         self.dano_total = self.vida2 - self.ataque_dano
                         if self.dano_total <= 0:
                             morte = True
                             messagebox.showinfo("Resultado"," O "f'{var1}'" matou o "f'{var2}'"")
                             if morte == True:
                                 bd.atualizar("Bancos/Banco.db", "NPC", "1", ['HP'], ["100"])
                                 bd.atualizar("Bancos/Banco.db", "NPC", "2", ['HP'], ["450"])
                                 bd.atualizar("Bancos/Banco.db", "NPC", "3", ['HP'], ["80"])
                                 bd.atualizar("Bancos/Banco.db", "NPC", "4", ['HP'], ["600"])
                                 bd.atualizar("Bancos/Banco.db", "NPC", "5", ['HP'], ["600"])
                                 bd.atualizar("Bancos/Banco.db", "NPC", "6", ['HP'], ["800"])
                                 bd.atualizar("Bancos/Banco.db", "NPC", "7", ['HP'], ["100"])
                         else:
                             messagebox.showinfo("Resultado", " O "f'{var2}'" sobreviveu ao ataque do "f'{var1}'"")
                             bd.atualizar("Bancos/Banco.db", "NPC", self.id2, ['HP'], [""f'{self.dano_total}'""])
                 else:
                     messagebox.showinfo("Resultado", " O "f'{var2}'" defendeu o ataque do "f'{var1}'"")

            else:
                 if self.ataque1 > self.defesa2:
                     self.defesa_dano = self.defesa2 - self.ataque1
                     self.ataque_dano = self.ataque1 - self.defesa2
                     if self.defesa_dano <= 0:
                         self.dano_total = self.vida2 - self.ataque_dano
                         if self.dano_total <= 0:
                             messagebox.showinfo("Resultado"," O "f'{var1}'" matou o "f'{var2}'"")
                         else:
                             messagebox.showinfo("Resultado", " O "f'{var2}'" sobreviveu ao ataque do "f'{var1}'"")
                 else:
                     messagebox.showinfo("Resultado", " O "f'{var2}'" defendeu o ataque do "f'{var1}'"")


    def atualizar_tvw(self):
        for i in self.tvw_menu.get_children():
            self.tvw_menu.delete(i)
        query = 'SELECT * FROM personagens;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_menu.insert('', tk.END, values=tupla)