import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

class Tela_Regras:
    def __init__(self, master, janela_principal):
        self.janela_regras = master
        self.janela_regras.overrideredirect(True)
        self.janela_regras.grab_set()
        self.janela_principal = janela_principal
        self.janela_regras.title("© 𝓛𝓾𝓕𝓮𝓵 𝓢𝓸𝓯𝓽𝔀𝓪𝓻𝓮")
        self.frm_botoes = tk.Frame(self.janela_regras, background='darkslategray')
        self.janela_regras['background'] = 'darkslategray'
        self.janela_regras.resizable(False, False)

        #CENTRALIZAR
        window_height = 280
        window_width = 160
        screen_width = self.janela_regras.winfo_screenwidth()
        screen_height = self.janela_regras.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.janela_regras.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.frm_botoes.pack(side=tk.TOP)

        #Imagem
        self.Flag = ImageTk.PhotoImage(Image.open("Imagens/info.png"))
        self.imagem = tk.Label(self.frm_botoes, text='', bg='darkslategray', image=self.Flag)
        self.imagem.pack()

        #Botões
        self.btn_classe = tk.Button(self.frm_botoes, text='Classes',
                                    command=lambda: webbrowser.open_new
                                    ('https://drive.google.com/file/d/1ayI22KjXSZPS2E-zZLk2mfuUmt_B5Fpi/view?usp=sharing'),
                                    bg='darkslategray', fg='black', font=' Constantia 12 bold italic', relief='flat')

        self.btn_bes = tk.Button(self.frm_botoes, text="Bestiário/NPC's",
                                 command=lambda: webbrowser.open_new
                                 ('https://drive.google.com/file/d/1c35dtKHFCyQpQ1ELESz-B5Ivr3YeHH1o/view?usp=sharing'),
                                 bg='darkslategray', fg='black',font=' Constantia 12 bold italic', relief="flat")

        self.btn_volt = tk.Button(self.frm_botoes, text='Voltar', bg='darkslategray', fg='black',
                                  command=self.voltar_Role, font=' Constantia 12 bold italic', relief="flat")

        self.btn_classe.pack()
        self.btn_bes.pack()
        self.btn_volt.pack()

    def voltar_Role(self):
        self.janela_regras.destroy()
        self.janela_principal.deiconify()



