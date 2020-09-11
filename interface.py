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

        #Variáveis do Entry
        self.litros=StringVar()

        #Criando frames da janela principal
        self.frame_titulo=Frame(self.janela_principal)
        self.frame_agua=Frame(self.janela_principal)
        self.frame_litros=Frame(self.janela_principal,bg='white')
        self.frame_espaco=Frame(self.janela_principal)
        self.frame_lavagem=Frame(self.janela_principal)
        self.frame_mostura=Frame(self.janela_principal)

        #Adicionando Labels da janela principal
        self.label_nome=Label(self.frame_titulo,height=2,width=28,fg='white',bg='gray26',text="Zalino",font=('arial black',18),anchor=CENTER)
        self.label_litros=Label(self.frame_litros,height=2,width=18,fg='white',bg='gray38',text="Quantidade de Litros",anchor=W)
        self.label_lavagem=Label(self.frame_lavagem,height=2,width=18,fg='white',bg='gray46',text="Água de Lavagem",anchor=CENTER)
        self.label_espaco=Label(self.frame_espaco,height=2,width=18,bg='white')
        #Adicionando Entry na janela principal
        self.retorna = self.frame_litros.register(self.validar_dado)
        self.entry_litros=Entry(self.frame_litros,bd=0.5,width=28,font='Calibri',textvariable=self.litros)
        self.entry_litros.bind(self.litros, (lambda _: self.validar_dado()))

        #Adicionando Botão



        #Empacotando dados da janela principal
        #label
        self.label_nome.pack(side=TOP)
        self.label_litros.pack(side=LEFT)
        self.label_espaco.pack(side=TOP)
        self.label_lavagem.pack(side=TOP)


        #Entry
        self.entry_litros.pack(side=RIGHT)
        #Frame
        self.frame_titulo.pack(side=TOP)
        self.frame_litros.pack(side=TOP,expand=False,fill =X)
        self.frame_espaco.pack()
        self.frame_lavagem.pack()
        self.frame_mostura.pack()
        self.janela_principal.mainloop()

    def validar_dado(self):
            try:
                float(self.litros.get())
                print('oi')

            except ValueError:
                print('5')
if __name__ == '__main__':
    obj=interface()
    obj.validar_dado()
    print('fim')


