import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

class Tela_Dados:
    def __init__(self, master, janela_principal):
        self.janela_dados = master
        self.janela_dados.overrideredirect(True)
        self.janela_dados.title('Simulador de combate')
        self.janela_dados.geometry('200x400')
        self.janela_dados['background'] = 'navajowhite3'
        self.janela_dados.grab_set()
        self.janela_principal = janela_principal
        self.frm_botoes = tk.Frame(self.janela_dados, background='navajowhite3')
        self.frm_botoes.pack(side=tk.BOTTOM)

        #imagem
        self.d20= ImageTk.PhotoImage(Image.open("Imagens/d20.png"))
        self.d6 = ImageTk.PhotoImage(Image.open("Imagens/d6.png"))
        self.d8 = ImageTk.PhotoImage(Image.open("Imagens/d8.png"))
        self.d12 = ImageTk.PhotoImage(Image.open("Imagens/d12.png"))

        #botões
        self.btn_dado_6 = tk.Button(self.frm_botoes, text='', bg='navajowhite3', command=self.dados_6,image=self.d6,borderwidth=0)
        self.btn_dado_6.pack()
        self.btn_dado_8 = tk.Button(self.frm_botoes, text='', bg='navajowhite3', command=self.dados_8,image=self.d8,borderwidth=0)
        self.btn_dado_8.pack()
        self.btn_dado_12 = tk.Button(self.frm_botoes, text='', bg='navajowhite3', command=self.dados_12,image=self.d12,borderwidth=0)
        self.btn_dado_12.pack()
        self.btn_dado_20 = tk.Button(self.frm_botoes, text='', bg='navajowhite3', command=self.dados_20,image=self.d20,borderwidth=0)
        self.btn_dado_20.pack()
        self.spac2 = tk.Label(self.frm_botoes, text='', bg='navajowhite3')
        self.spac2.pack()
        self.btn_voltar = tk.Button(self.frm_botoes, text='Voltar', bg='navajowhite3', fg='black',font=' Constantia 15 bold ', command=self.voltar, relief="solid")
        self.btn_voltar.pack()
        self.spac1 = tk.Label(self.frm_botoes, text='',background='navajowhite3')
        self.spac1.pack()

    def voltar(self):
        self.janela_dados.destroy()
        self.janela_principal.deiconify()

    def dados_6(self):
        eve = random.randrange(1, 6)
        if eve == 1:
            messagebox.showinfo('Resultado', '1')
        elif eve == 2:
            messagebox.showinfo('Resultado', '2')
        elif eve == 3:
            messagebox.showinfo('Resultado', '3')
        elif eve == 4:
            messagebox.showinfo('Resultado', '4')
        elif eve == 5:
            messagebox.showinfo('Resultado', '5')
        else:
            messagebox.showinfo('Resultado', '6')

    def dados_8(self):
        eve = random.randrange(1, 8)
        if eve == 1:
            messagebox.showinfo('Resultado', '1')
        elif eve == 2:
            messagebox.showinfo('Resultado', '2')
        elif eve == 3:
            messagebox.showinfo('Resultado', '3')
        elif eve == 4:
            messagebox.showinfo('Resultado', '4')
        elif eve == 5:
            messagebox.showinfo('Resultado', '5')
        elif eve == 6:
            messagebox.showinfo('Resultado', '6')
        elif eve == 7:
            messagebox.showinfo('Resultado', '7')
        else:
            messagebox.showinfo('Resultado', '8')

    def dados_12(self):
        eve = random.randrange(1, 12)
        if eve == 1:
            messagebox.showinfo('Resultado', '1')
        elif eve == 2:
            messagebox.showinfo('Resultado', '2')
        elif eve == 3:
            messagebox.showinfo('Resultado', '3')
        elif eve == 4:
            messagebox.showinfo('Resultado', '4')
        elif eve == 5:
            messagebox.showinfo('Resultado', '5')
        elif eve == 6:
            messagebox.showinfo('Resultado', '6')
        elif eve == 7:
            messagebox.showinfo('Resultado', '7')
        elif eve == 8:
            messagebox.showinfo('Resultado', '8')
        elif eve == 9:
            messagebox.showinfo('Resultado', '9')
        elif eve == 10:
            messagebox.showinfo('Resultado', '10')
        elif eve == 11:
            messagebox.showinfo('Resultado', '11')
        else:
            messagebox.showinfo('Resultado', '12')

    def dados_20(self):
        eve = random.randrange(1, 20)
        if eve == 1:
            messagebox.showinfo('Resultado', '1')
        elif eve == 2:
            messagebox.showinfo('Resultado', '2')
        elif eve == 3:
            messagebox.showinfo('Resultado', '3')
        elif eve == 4:
            messagebox.showinfo('Resultado', '4')
        elif eve == 5:
            messagebox.showinfo('Resultado', '5')
        elif eve == 6:
            messagebox.showinfo('Resultado', '6')
        elif eve == 7:
            messagebox.showinfo('Resultado', '7')
        elif eve == 8:
            messagebox.showinfo('Resultado', '8')
        elif eve == 9:
            messagebox.showinfo('Resultado', '9')
        elif eve == 10:
            messagebox.showinfo('Resultado', '10')
        elif eve == 11:
            messagebox.showinfo('Resultado', '11')
        elif eve == 12:
            messagebox.showinfo('Resultado', '12')
        elif eve == 13:
            messagebox.showinfo('Resultado', '13')
        elif eve == 14:
            messagebox.showinfo('Resultado', '14')
        elif eve == 15:
            messagebox.showinfo('Resultado', '15')
        elif eve == 16:
            messagebox.showinfo('Resultado', '16')
        elif eve == 17:
            messagebox.showinfo('Resultado', '17')
        elif eve == 18:
            messagebox.showinfo('Resultado', '18')
        elif eve == 19:
            messagebox.showinfo('Resultado', '19')
        else:
            messagebox.showinfo('Resultado', '20')