from tkinter import *
import Calculadora_de_Sais
from tkinter import messagebox

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
        self.frame_lavagem=Frame(self.janela_principal,bg='gray46')
        self.frame_mostura=Frame(self.janela_principal)

        #Adicionando Labels da janela principal
        self.label_nome=Label(self.frame_titulo,height=2,width=28,fg='white',bg='gray26',text="Zalino",font=('arial black',18),anchor=CENTER)
        self.label_litros=Label(self.frame_litros,height=2,width=18,fg='white',bg='gray38',text="Quantidade de Litros",anchor=W)
        self.label_lavagem=Label(self.frame_lavagem,height=3,width=18,fg='white',bg='gray46',relief=FLAT,text="Água de Lavagem",anchor=CENTER)
        self.label_espaco=Label(self.frame_espaco,height=4,width=18,bg='white')

        #Adicionando Entry na janela principal
        self.entry_litros=Entry(self.frame_litros,bd=0.5,width=28,font='Calibri',textvariable=self.litros)


        #Adicionando Botão
        self.botao_lavagem=Button(self.frame_lavagem,text='Selecionar',command=self.validar_dado)


        #Empacotando dados da janela principal
        #label
        self.label_nome.pack(side=TOP)
        self.label_litros.pack(side=LEFT)
        self.label_espaco.pack(side=TOP)
        self.label_lavagem.pack(side=TOP)

        #Entry
        self.entry_litros.pack(side=RIGHT)

        #Botão
        self.botao_lavagem.pack()
        #Frame
        self.frame_titulo.pack(side=TOP)
        self.frame_litros.pack(side=TOP,expand=False,fill =X)
        self.frame_espaco.pack()
        self.frame_lavagem.pack()
        self.frame_mostura.pack()
        self.janela_principal.mainloop()

    def validar_dado(self):

        if self.litros.get() !="":
           if self.litros.get().isalpha():
               self.entry_litros.delete(0,len(self.litros.get()))
               self.litros.set("")
               messagebox.showerror("ERRO!","Valor digitado não é válido!")

           elif self.litros.get().isspace():
               self.entry_litros.delete(0, len(self.litros.get()))
               self.litros.set("")
               messagebox.showerror("ERRO!", "Valor digitado não é válido!")
           else:
               try:
                   float(self.litros.get())
               except:
                   self.entry_litros.delete(0, len(self.litros.get()))
                   self.litros.set("")
                   messagebox.showerror("ERRO!", "Valor digitado não é válido!")
    #def janela_lavagem(self):



if __name__ == '__main__':
    obj=interface()
    print('fim')


