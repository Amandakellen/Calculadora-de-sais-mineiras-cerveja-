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
        self.botao_lavagem=Button(self.frame_lavagem,text='Selecionar',command=self.janela_lavagem)


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
               return False
               #messagebox.showerror("ERRO!","Valor digitado não é válido!")

           elif self.litros.get().isspace():
               return False
               #messagebox.showerror("ERRO!", "Valor digitado não é válido!")
           else:
               try:
                   float(self.litros.get())
                   if float(self.litros.get())<0:
                       return False
                   else:
                       return True
               except:
                   return False
                   #messagebox.showerror("ERRO!", "Valor digitado não é válido!")
    def janela_lavagem(self):
         self.validacao=self.validar_dado()
         self.agua='1'
         if self.validacao:
             self.janela_lavagem_=Toplevel()
             self.janela_lavagem_.geometry('350x500')
             self.janela_lavagem_.config(bg='white')
             self.calculando=Calculadora_de_Sais.calculo_sais(self.agua,float(self.litros.get()))

             #Calculo Sulfato de cálcio
             self.cev_lupulada_sc=self.calculando.cerveja_lupulada_sulfato_de_Calcio()
             self.cev_maltada_sc=self.calculando.cerveja_maltada_sulfato_de_Calcio()
             self.cev_equilibrada_sc=self.calculando.cerveja_equilibrada_sulfato_de_Calcio()

             #Cálculo Sulfato de magnésio
             self.cev_lupulada_sm = self.calculando.cerveja_lupulada_sulfato_de_magnesio()
             self.cev_maltada_sm = self.calculando.cerveja_maltada_sulfato_de_magnesio()
             self.cev_equilibrada_sm = self.calculando.cerveja_equilibrada_sulfato_de_magnesio()

             #Cálculo Cloreto de Cálcio
             self.cev_lupulada_cc = self.calculando.cerveja_lupulada_cloreto_De_calcio()
             self.cev_maltada_cc = self.calculando.cerveja_maltada_cloreto_De_calcio()
             self.cev_equilibrada_cc = self.calculando.cerveja_equilibrada_cloreto_de_calcio()

             #Frames
             self.frame_agua_l=Frame(self.janela_lavagem_)
             self.frame_espaco_l=Frame(self.janela_lavagem_)

             #Cerveja Lupulada
             self.frame_nome_cerveja_lupulada=Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_lupulada_sc=Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_lupulada_sm = Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_lupulada_cc = Frame(self.janela_lavagem_)

             #Cerveja Maltada
             self.frame_nome_cerveja_maltada= Frame(self.janela_lavagem_, bg='white')
             self.frame_cerveja_maltada_sc = Frame(self.janela_lavagem_)
             self.frame_cerveja_maltada_sm = Frame(self.janela_lavagem_)
             self.frame_cerveja_maltada_cc = Frame(self.janela_lavagem_)

             #Cerveja Equilibrada
             self.frame_nome_cerveja_equilibrada = Frame(self.janela_lavagem_, bg='white')
             self.frame_cerveja_equilibrada_sc = Frame(self.janela_lavagem_)
             self.frame_cerveja_equilibrada_sm = Frame(self.janela_lavagem_)
             self.frame_cerveja_equilibrada_cc = Frame(self.janela_lavagem_)

             #Labels
             self.label_agua_l=Label(self.frame_agua_l,height=2,width=28,bg='gray26',fg='white',text='Água de Lavagem',font=('arial black',18),anchor=CENTER)
             #self.label_espaco_l=Label(self.frame_espaco_l,height=1,width=7,bg='white')

             # Cerveja Lupulada
             self.label_nome_cl=Label(self.frame_nome_cerveja_lupulada,text='Cerveja Lupulada',height=2,width=20,bg='white',font=('arial black',11),anchor=CENTER)
             #Sulfato de Cálcio
             self.label_cl_sc=Label(self.frame_cerveja_lupulada_sc,text='Sulfato de Cálcio(em g)',height=2,width=20,bg='gray46',anchor=W)
             self.labelcl_sc_resultado=Label(self.frame_cerveja_lupulada_sc,text='%.2f'%self.cev_lupulada_sc,bg='white',font=('arial black',12),anchor=E)
             #Sulfato de Magnésio
             self.label_cl_sm = Label(self.frame_cerveja_lupulada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelcl_sm_resultado = Label(self.frame_cerveja_lupulada_sm, text='%.2f' % self.cev_lupulada_sm,bg='white', font=('arial black', 12), anchor=E)



             #Empacotando dados da janela lavagem
             # Labels
             self.label_agua_l.pack()
             #self.label_espaco_l.pack(side=TOP)


             #Cerveja Lupulada
             self.label_nome_cl.pack()
             #Sulfato de cálcio
             self.label_cl_sc.pack(side=LEFT)
             self.labelcl_sc_resultado.pack(side=RIGHT)
             #sulfato de magnésio
             self.label_cl_sm.pack(side=LEFT)
             self.labelcl_sm_resultado.pack(side=RIGHT)
             #Cloreto de Cálcio

             #Frames
             self.frame_agua_l.pack()
             #self.frame_espaco_l.pack()

             #cerveja Lupulada
             self.frame_nome_cerveja_lupulada.pack(side=TOP)
             self.frame_cerveja_lupulada_sc.pack(side=TOP,fill="both",after=self.frame_nome_cerveja_lupulada)
             self.frame_cerveja_lupulada_sm.packpack(side=TOP,fill="both",after=self.frame_cerveja_lupulada_sc)
             self.frame_cerveja_lupulada_cc.pack()

             #Cerveja Maltada
             self.frame_nome_cerveja_maltada.pack()
             self.frame_cerveja_maltada_sc.pack()
             self.frame_cerveja_maltada_sm.pack()
             self.frame_cerveja_maltada_cc.pack()

             #Cerveja Equilibrada
             self.frame_nome_cerveja_equilibrada.pack()
             self.frame_cerveja_equilibrada_sc.pack()
             self.frame_cerveja_equilibrada_sm.pack()
             self.frame_cerveja_equilibrada_cc.pack()

             self.janela_lavagem_.mainloop()

         elif self.litros.get()=="":
             messagebox.showerror("ERRO!", "Digite a quantidade de Litros!")
         else:
             self.entry_litros.delete(0, len(self.litros.get()))
             self.litros.set("")
             messagebox.showerror("ERRO!", "Valor digitado não é válido!")

    def janela_mostura(self):
        self.validacao = self.validar_dado()
        self.agua = '2'
        if self.validacao:
            self.janela_mostura_ = Toplevel()
            self.janela_mostura_.geometry('350x500')
            self.janela_mostura_.config(bg='white')
            self.calculando = Calculadora_de_Sais.calculo_sais(self.agua, float(self.litros.get()))

            # Calculo Sulfato de cálcio
            self.cev_lupulada_sc = self.calculando.cerveja_lupulada_sulfato_de_Calcio()
            self.cev_maltada_sc = self.calculando.cerveja_maltada_sulfato_de_Calcio()
            self.cev_equilibrada_sc = self.calculando.cerveja_equilibrada_sulfato_de_Calcio()

            # Cálculo Sulfato de magnésio
            self.cev_lupulada_sm = self.calculando.cerveja_lupulada_sulfato_de_magnesio()
            self.cev_maltada_sm = self.calculando.cerveja_maltada_sulfato_de_magnesio()
            self.cev_equilibrada_sm = self.calculando.cerveja_equilibrada_sulfato_de_magnesio()

            # Cálculo Cloreto de Cálcio
            self.cev_lupulada_cc = self.calculando.cerveja_lupulada_cloreto_De_calcio()
            self.cev_maltada_cc = self.calculando.cerveja_maltada_cloreto_De_calcio()
            self.cev_equilibrada_cc = self.calculando.cerveja_equilibrada_cloreto_de_calcio()

            self.janela_mostura_.mainloop()

        elif self.litros.get() == "":
            messagebox.showerror("ERRO!", "Digite a quantidade de Litros!")
        else:
            self.entry_litros.delete(0, len(self.litros.get()))
            self.litros.set("")
            messagebox.showerror("ERRO!", "Valor digitado não é válido!")


if __name__ == '__main__':
    obj=interface()
    print('fim')
