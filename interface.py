from tkinter import *
import Calculadora_de_Sais

class interface:
    def __init__(self):
        #definindo configurações da janela principal
        self.janela_principal = Tk()
        self.janela_principal.title('Zalino')
        self.janela_principal.geometry('350x500')
        self.janela_principal.resizable(False, False)
        self.janela_principal.config(bg='white')

        #Criando frames da janela principal
        self.frame_titulo=Frame(self.janela_principal)
        self.frame_agua=Frame(self.janela_principal)
        self.frame_litros=Frame(self.janela_principal)
        self.frame_lavagem=Frame(self.janela_principal)
        self.frame_mostura=Frame(self.janela_principal)

        #Adicionando Labels da janela principal
        self.label_nome=Label(self.frame_titulo,height=2,width=28,fg='white',bg='gray26',text="Zalino",font=('arial black',18),anchor=CENTER)
        self.label_litros=Label(self.frame_litros,height=2,width=28,fg='white',bg='gray38',text="Quantidade de Litros",anchor=E)
        #Empacotando dados da janela principal
        self.label_nome.pack(side=TOP)

        self.frame_titulo.pack()
        self.frame_litros.pack()
        self.frame_lavagem.pack()
        self.frame_mostura.pack()
        self.janela_principal.mainloop()

    def janela_calculo(self):
        self.janela_calculo=Toplevel()
        self.janela_calculo.title('Zalino')
        self.janela_calculo.geometry('350x500')
        self.janela_calculo.resizable(False, False)
        self.janela_calculo.config(bg='white')


if __name__ == '__main__':
    obj=interface()

