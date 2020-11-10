from tkinter import *
import Calculadora_de_Sais
from tkinter import messagebox
import webbrowser


def callback(url):
    webbrowser.open_new(url)
class interface:
    def __init__(self):
        #definindo configurações da janela principal
        self.janela_principal = Tk()
        self.janela_principal.title('Zalino Water')
        self.janela_principal.geometry('450x700')
        self.janela_principal.resizable(False, False)
        self.icone=PhotoImage(file='simbolo.png')
        self.janela_principal.iconphoto(True, self.icone)
        self.imagem=PhotoImage(file='Zalino Water.png')
        self.janela_principal.config(bg='white')

        #Variáveis do Entry
        self.litros=StringVar()

        #Criando frames da janela principal
        self.frame_titulo=Frame(self.janela_principal)
        self.frame_agua=Frame(self.janela_principal)
        self.frame_litros=Frame(self.janela_principal,bg='white')
        self.frame_espaco=Frame(self.janela_principal)
        self.frame_espaco2 = Frame(self.janela_principal)
        self.frame_lavagem=Frame(self.janela_principal,bg='gray46')
        self.frame_mostura=Frame(self.janela_principal,bg='gray46')
        self.frame_rodape=Frame(self.janela_principal,bg='white')

        #Adicionando Labels da janela principal
        self.label_nome=Label(self.frame_titulo,height=250,width=700,fg='white',bg='white',image=self.imagem,anchor=CENTER)
        self.label_litros=Label(self.frame_litros,height=2,width=18,fg='white',bg='gray38',text="Quantidade de Litros",anchor=W)
        self.label_lavagem=Label(self.frame_lavagem,height=3,width=18,fg='white',bg='gray46',relief=FLAT,text="Água de Lavagem",anchor=CENTER)
        self.label_espaco=Label(self.frame_espaco,height=4,width=18,bg='white')
        self.label_espaco2 = Label(self.frame_espaco2, height=4, width=18, bg='white')
        self.label_mostura=Label(self.frame_mostura,height=3,width=18,fg='white',bg='gray46',relief=FLAT,text="Água de Mostura",anchor=CENTER)
        self.label_rodape=Label(self.frame_rodape,text='Refêrencias de  Jamal Awadallak - Beer School',bg='white',fg='black',font=('Calibri',10))
        self.label_rodape.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=iVqjMjcikMc&t=1s"))

        #Adicionando Entry na janela principal
        self.entry_litros=Entry(self.frame_litros,bd=1,width=40,bg='white',font='Calibri',textvariable=self.litros)


        #Adicionando Botão
        self.botao_lavagem=Button(self.frame_lavagem,text='Selecionar',command=self.janela_lavagem,bd=3,fg='black',bg='white')
        self.botao_mostura= Button(self.frame_mostura, text='Selecionar', command=self.janela_mostura,bd=3,fg='black',bg='white')

        #Empacotando dados da janela principal
        #label
        self.label_nome.pack(side=TOP)
        self.label_litros.pack(side=LEFT)
        self.label_espaco.pack(side=TOP)
        self.label_lavagem.pack(side=TOP)
        self.label_espaco2.pack(side=TOP)
        self.label_mostura.pack(side=TOP)
        self.label_rodape.pack(side=BOTTOM)

        #Entry
        self.entry_litros.pack(side=RIGHT)

        #Botão
        self.botao_lavagem.pack()
        self.botao_mostura.pack()
        #Frame
        self.frame_titulo.pack(side=TOP)
        self.frame_litros.pack(side=TOP,expand=False,fill =X)
        self.frame_espaco.pack()
        self.frame_lavagem.pack()
        self.frame_espaco2.pack(side=TOP,after=self.frame_lavagem)
        self.frame_mostura.pack()
        self.frame_rodape.pack(side=BOTTOM)
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
             self.janela_lavagem_.geometry('400x550')
             self.janela_lavagem_.config(bg='white')
             self.janela_lavagem_.resizable(False, False)
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
             self.frame_cerveja_lupulada_cc = Frame(self.janela_lavagem_,bg='white')

             #Cerveja Maltada
             self.frame_nome_cerveja_maltada= Frame(self.janela_lavagem_, bg='white')
             self.frame_cerveja_maltada_sc = Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_maltada_sm = Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_maltada_cc = Frame(self.janela_lavagem_,bg='white')

             #Cerveja Equilibrada
             self.frame_nome_cerveja_equilibrada = Frame(self.janela_lavagem_, bg='white')
             self.frame_cerveja_equilibrada_sc = Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_equilibrada_sm = Frame(self.janela_lavagem_,bg='white')
             self.frame_cerveja_equilibrada_cc = Frame(self.janela_lavagem_,bg='white')

             #Labels
             self.label_agua_l=Label(self.frame_agua_l,height=2,width=28,bg='gray26',fg='white',text='Água de Lavagem',font=('arial black',18),anchor=CENTER)


             # Cerveja Lupulada
             self.label_nome_cl=Label(self.frame_nome_cerveja_lupulada,text='Cerveja Lupulada',height=2,width=20,bg='white',font=('arial black',11),anchor=CENTER)
             #Sulfato de Cálcio
             self.label_cl_sc=Label(self.frame_cerveja_lupulada_sc,text='Sulfato de Cálcio(em g)',height=2,width=20,bg='gray46',anchor=W)
             self.labelcl_sc_resultado=Label(self.frame_cerveja_lupulada_sc,text='%.2f'%self.cev_lupulada_sc,bg='white',font=('arial black',12),anchor=E)
             #Sulfato de Magnésio
             self.label_cl_sm = Label(self.frame_cerveja_lupulada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelcl_sm_resultado = Label(self.frame_cerveja_lupulada_sm, text='%.2f' % self.cev_lupulada_sm,bg='white', font=('arial black', 12), anchor=E)
             #Cloreto de cálcio
             self.label_cl_cc = Label(self.frame_cerveja_lupulada_cc, text='Cloreto de Cálcio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelcl_cc_resultado = Label(self.frame_cerveja_lupulada_cc, text='%.2f' % self.cev_lupulada_cc,bg='white', font=('arial black', 12), anchor=E)

             # Cerveja Maltada
             self.label_nome_cm = Label(self.frame_nome_cerveja_maltada, text='Cerveja Maltada', height=2, width=20,bg='white', font=('arial black', 11), anchor=CENTER)
             # Sulfato de Cálcio
             self.label_cm_sc = Label(self.frame_cerveja_maltada_sc, text='Sulfato de Cálcio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelcm_sc_resultado = Label(self.frame_cerveja_maltada_sc, text='%.2f' % self.cev_maltada_sc,bg='white', font=('arial black', 12), anchor=E)
             # Sulfato de Magnésio
             self.label_cm_sm = Label(self.frame_cerveja_maltada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelcm_sm_resultado = Label(self.frame_cerveja_maltada_sm, text='%.2f' % self.cev_maltada_sm,bg='white', font=('arial black', 12), anchor=E)
             # Cloreto de cálcio
             self.label_cm_cc = Label(self.frame_cerveja_maltada_cc, text='Cloreto de Cálcio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelcm_cc_resultado = Label(self.frame_cerveja_maltada_cc, text='%.2f' % self.cev_maltada_cc,bg='white', font=('arial black', 12), anchor=E)

             # Cerveja Equilibrada
             self.label_nome_ce = Label(self.frame_nome_cerveja_equilibrada, text='Cerveja Equilibrada', height=2, width=20,bg='white', font=('arial black', 11), anchor=CENTER)
             # Sulfato de Cálcio
             self.label_ce_sc = Label(self.frame_cerveja_equilibrada_sc, text='Sulfato de Cálcio(em g)', height=2, width=20,bg='gray46', anchor=W)
             self.labelce_sc_resultado = Label(self.frame_cerveja_equilibrada_sc, text='%.2f' % self.cev_equilibrada_sc,bg='white', font=('arial black', 12), anchor=E)
             # Sulfato de Magnésio
             self.label_ce_sm = Label(self.frame_cerveja_equilibrada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
             self.labelce_sm_resultado = Label(self.frame_cerveja_equilibrada_sm, text='%.2f' % self.cev_equilibrada_sm,bg='white', font=('arial black', 12), anchor=E)
             # Cloreto de cálcio
             self.label_ce_cc = Label(self.frame_cerveja_equilibrada_cc, text='Cloreto de Cálcio(em g)', height=2, width=20,bg='gray46', anchor=W)
             self.labelce_cc_resultado = Label(self.frame_cerveja_equilibrada_cc, text='%.2f' % self.cev_equilibrada_cc,bg='white', font=('arial black', 12), anchor=E)

             #Empacotando dados da janela lavagem
             # Labels
             self.label_agua_l.pack()

             #Cerveja Lupulada
             self.label_nome_cl.pack()
             #Sulfato de cálcio
             self.label_cl_sc.pack(side=LEFT)
             self.labelcl_sc_resultado.pack(side=LEFT)
             #sulfato de magnésio
             self.label_cl_sm.pack(side=LEFT)
             self.labelcl_sm_resultado.pack(side=LEFT)
             #Cloreto de Cálcio
             self.label_cl_cc.pack(side=LEFT)
             self.labelcl_cc_resultado.pack(side=LEFT)

             # Cerveja Maltada
             self.label_nome_cm.pack()
             # Sulfato de cálcio
             self.label_cm_sc.pack(side=LEFT)
             self.labelcm_sc_resultado.pack(side=LEFT)
             # sulfato de magnésio
             self.label_cm_sm.pack(side=LEFT)
             self.labelcm_sm_resultado.pack(side=LEFT)
             # Cloreto de Cálcio
             self.label_cm_cc.pack(side=LEFT)
             self.labelcm_cc_resultado.pack(side=LEFT)

             # Cerveja Equilibrada
             self.label_nome_ce.pack()
             # Sulfato de cálcio
             self.label_ce_sc.pack(side=LEFT)
             self.labelce_sc_resultado.pack(side=LEFT)
             # sulfato de magnésio
             self.label_ce_sm.pack(side=LEFT)
             self.labelce_sm_resultado.pack(side=LEFT)
             # Cloreto de Cálcio
             self.label_ce_cc.pack(side=LEFT)
             self.labelce_cc_resultado.pack(side=LEFT)

             #Frames
             self.frame_agua_l.pack()

             #cerveja Lupulada
             self.frame_nome_cerveja_lupulada.pack(side=TOP)
             self.frame_cerveja_lupulada_sc.pack(side=TOP,fill="both",after=self.frame_nome_cerveja_lupulada)
             self.frame_cerveja_lupulada_sm.pack(side=TOP,fill="both")
             self.frame_cerveja_lupulada_cc.pack(side=TOP,fill="both")

             #Cerveja Maltada
             self.frame_nome_cerveja_maltada.pack(side=TOP)
             self.frame_cerveja_maltada_sc.pack(side=TOP,fill="both",after=self.frame_nome_cerveja_maltada)
             self.frame_cerveja_maltada_sm.pack(side=TOP,fill="both")
             self.frame_cerveja_maltada_cc.pack(side=TOP,fill="both")

             #Cerveja Equilibrada
             self.frame_nome_cerveja_equilibrada.pack(side=TOP)
             self.frame_cerveja_equilibrada_sc.pack(side=TOP,fill="both",after=self.frame_nome_cerveja_equilibrada)
             self.frame_cerveja_equilibrada_sm.pack(side=TOP,fill="both")
             self.frame_cerveja_equilibrada_cc.pack(side=TOP,fill="both")

             self.janela_lavagem_.mainloop()

         elif self.litros.get()=="":
             messagebox.showerror("ERRO!", "Digite a quantidade de Litros!")
         else:
             self.entry_litros.delete(0, len(self.litros.get()))
             self.litros.set("")
             messagebox.showerror("ERRO!", "Valor digitado não é válido!")
    def janela_mostura(self):
        self.validacao = self.validar_dado()
        self.aguam = '2'
        if self.validacao:
            self.janela_mostura_ = Toplevel()
            self.janela_mostura_.geometry('400x550')
            self.janela_mostura_.config(bg='white')
            self.janela_mostura_.resizable(False, False)
            self.calculandom = Calculadora_de_Sais.calculo_sais(self.aguam, float(self.litros.get()))

            # Calculo Sulfato de cálcio
            self.mostura_cev_lupulada_sc = self.calculandom.cerveja_lupulada_sulfato_de_Calcio()
            self.mostura_cev_maltada_sc = self.calculandom.cerveja_maltada_sulfato_de_Calcio()
            self.mostura_cev_equilibrada_sc = self.calculandom.cerveja_equilibrada_sulfato_de_Calcio()

            # Cálculo Sulfato de magnésio
            self.mostura_cev_lupulada_sm = self.calculandom.cerveja_lupulada_sulfato_de_magnesio()
            self.mostura_cev_maltada_sm = self.calculandom.cerveja_maltada_sulfato_de_magnesio()
            self.mostura_cev_equilibrada_sm = self.calculandom.cerveja_equilibrada_sulfato_de_magnesio()

            # Cálculo Cloreto de Cálcio
            self.mostura_cev_lupulada_cc = self.calculandom.cerveja_lupulada_cloreto_De_calcio()
            self.mostura_cev_maltada_cc = self.calculandom.cerveja_maltada_cloreto_De_calcio()
            self.mostura_cev_equilibrada_cc = self.calculandom.cerveja_equilibrada_cloreto_de_calcio()

            # Frames
            self.mostura_frame_agua_m = Frame(self.janela_mostura_)
            self.mostura_frame_espaco_m = Frame(self.janela_mostura_)


            # Cerveja Lupulada
            self.mostura_frame_nome_cerveja_lupulada = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_lupulada_sc = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_lupulada_sm = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_lupulada_cc = Frame(self.janela_mostura_, bg='white')

            # Cerveja Maltada
            self.mostura_frame_nome_cerveja_maltada = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_maltada_sc = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_maltada_sm = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_maltada_cc = Frame(self.janela_mostura_, bg='white')

            # Cerveja Equilibrada
            self.mostura_frame_nome_cerveja_equilibrada = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_equilibrada_sc = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_equilibrada_sm = Frame(self.janela_mostura_, bg='white')
            self.mostura_frame_cerveja_equilibrada_cc = Frame(self.janela_mostura_, bg='white')

            # Labels
            self.mostura_label_agua_l = Label(self.mostura_frame_agua_m, height=2, width=28, bg='gray26', fg='white',text='Água de Mostura', font=('arial black', 18), anchor=CENTER)

            # Cerveja Lupulada
            self.mostura_label_nome_cl = Label(self.mostura_frame_nome_cerveja_lupulada, text='Cerveja Lupulada', height=2, width=20,bg='white', font=('arial black', 11), anchor=CENTER)
            # Sulfato de Cálcio
            self.mostura_label_cl_sc = Label(self.mostura_frame_cerveja_lupulada_sc, text='Sulfato de Cálcio(em g)', height=2, width=20,bg='gray46', anchor=W)
            self.mostura_labelcl_sc_resultado = Label(self.mostura_frame_cerveja_lupulada_sc, text='%.2f' % self.mostura_cev_lupulada_sc,bg='white', font=('arial black', 12), anchor=E)
            # Sulfato de Magnésio
            self.mostura_label_cl_sm = Label(self.mostura_frame_cerveja_lupulada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
            self.mostura_labelcl_sm_resultado = Label(self.mostura_frame_cerveja_lupulada_sm, text='%.2f' % self.mostura_cev_lupulada_sm,bg='white', font=('arial black', 12), anchor=E)
            # Cloreto de cálcio
            self.mostura_label_cl_cc = Label(self.mostura_frame_cerveja_lupulada_cc, text='Cloreto de Cálcio(em g)', height=2, width=20,bg='gray46', anchor=W)
            self.mostura_labelcl_cc_resultado = Label(self.mostura_frame_cerveja_lupulada_cc, text='%.2f' % self.mostura_cev_lupulada_cc,bg='white', font=('arial black', 12), anchor=E)

            # Cerveja Maltada
            self.mostura_label_nome_cm = Label(self.mostura_frame_nome_cerveja_maltada, text='Cerveja Maltada', height=2, width=20,bg='white', font=('arial black', 11), anchor=CENTER)
            # Sulfato de Cálcio
            self.mostura_label_cm_sc = Label(self.mostura_frame_cerveja_maltada_sc, text='Sulfato de Cálcio(em g)', height=2, width=20,bg='gray46', anchor=W)
            self.mostura_labelcm_sc_resultado = Label(self.mostura_frame_cerveja_maltada_sc, text='%.2f' % self.mostura_cev_maltada_sc,bg='white', font=('arial black', 12), anchor=E)
            # Sulfato de Magnésio
            self.mostura_label_cm_sm = Label(self.mostura_frame_cerveja_maltada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
            self.mostura_labelcm_sm_resultado = Label(self.mostura_frame_cerveja_maltada_sm, text='%.2f' % self.mostura_cev_maltada_sm,bg='white', font=('arial black', 12), anchor=E)
            # Cloreto de cálcio
            self.mostura_label_cm_cc = Label(self.mostura_frame_cerveja_maltada_cc, text='Cloreto de Cálcio(em g)', height=2, width=20,bg='gray46', anchor=W)
            self.mostura_labelcm_cc_resultado = Label(self.mostura_frame_cerveja_maltada_cc, text='%.2f' % self.mostura_cev_maltada_cc,bg='white', font=('arial black', 12), anchor=E)

            # Cerveja Equilibrada
            self.mostura_label_nome_ce = Label(self.mostura_frame_nome_cerveja_equilibrada, text='Cerveja Equilibrada', height=2,width=20, bg='white', font=('arial black', 11), anchor=CENTER)
            # Sulfato de Cálcio
            self.mostura_label_ce_sc = Label(self.mostura_frame_cerveja_equilibrada_sc, text='Sulfato de Cálcio(em g)', height=2,width=20, bg='gray46', anchor=W)
            self.mostura_labelce_sc_resultado = Label(self.mostura_frame_cerveja_equilibrada_sc, text='%.2f' % self.mostura_cev_equilibrada_sc,bg='white', font=('arial black', 12), anchor=E)
            # Sulfato de Magnésio
            self.mostura_label_ce_sm = Label(self.mostura_frame_cerveja_equilibrada_sm, text='Sulfato de Magnésio(em g)', height=2,width=20, bg='gray46', anchor=W)
            self.mostura_labelce_sm_resultado = Label(self.mostura_frame_cerveja_equilibrada_sm, text='%.2f' % self.mostura_cev_equilibrada_sm,bg='white', font=('arial black', 12), anchor=E)
            # Cloreto de cálcio
            self.mostura_label_ce_cc = Label(self.mostura_frame_cerveja_equilibrada_cc, text='Cloreto de Cálcio(em g)', height=2,width=20, bg='gray46', anchor=W)
            self.mostura_labelce_cc_resultado = Label(self.mostura_frame_cerveja_equilibrada_cc, text='%.2f' % self.mostura_cev_equilibrada_cc,bg='white', font=('arial black', 12), anchor=E)

            # Empacotando dados da janela lavagem
            # Labels
            self.mostura_label_agua_l.pack()

            # Cerveja Lupulada
            self.mostura_label_nome_cl.pack()
            # Sulfato de cálcio
            self.mostura_label_cl_sc.pack(side=LEFT)
            self.mostura_labelcl_sc_resultado.pack(side=LEFT)
            # sulfato de magnésio
            self.mostura_label_cl_sm.pack(side=LEFT)
            self.mostura_labelcl_sm_resultado.pack(side=LEFT)
            # Cloreto de Cálcio
            self.mostura_label_cl_cc.pack(side=LEFT)
            self.mostura_labelcl_cc_resultado.pack(side=LEFT)

            # Cerveja Maltada
            self.mostura_label_nome_cm.pack()
            # Sulfato de cálcio
            self.mostura_label_cm_sc.pack(side=LEFT)
            self.mostura_labelcm_sc_resultado.pack(side=LEFT)
            # sulfato de magnésio
            self.mostura_label_cm_sm.pack(side=LEFT)
            self.mostura_labelcm_sm_resultado.pack(side=LEFT)
            # Cloreto de Cálcio
            self.mostura_label_cm_cc.pack(side=LEFT)
            self.mostura_labelcm_cc_resultado.pack(side=LEFT)

            # Cerveja Equilibrada
            self.mostura_label_nome_ce.pack()
            # Sulfato de cálcio
            self.mostura_label_ce_sc.pack(side=LEFT)
            self.mostura_labelce_sc_resultado.pack(side=LEFT)
            # sulfato de magnésio
            self.mostura_label_ce_sm.pack(side=LEFT)
            self.mostura_labelce_sm_resultado.pack(side=LEFT)
            # Cloreto de Cálcio
            self.mostura_label_ce_cc.pack(side=LEFT)
            self.mostura_labelce_cc_resultado.pack(side=LEFT)

            # Frames
            self.mostura_frame_agua_m.pack()


            # cerveja Lupulada
            self.mostura_frame_nome_cerveja_lupulada.pack(side=TOP)
            self.mostura_frame_cerveja_lupulada_sc.pack(side=TOP, fill="both", after=self.mostura_frame_nome_cerveja_lupulada)
            self.mostura_frame_cerveja_lupulada_sm.pack(side=TOP, fill="both")
            self.mostura_frame_cerveja_lupulada_cc.pack(side=TOP, fill="both")

            # Cerveja Maltada
            self.mostura_frame_nome_cerveja_maltada.pack(side=TOP)
            self.mostura_frame_cerveja_maltada_sc.pack(side=TOP, fill="both", after=self.mostura_frame_nome_cerveja_maltada)
            self.mostura_frame_cerveja_maltada_sm.pack(side=TOP, fill="both")
            self.mostura_frame_cerveja_maltada_cc.pack(side=TOP, fill="both")

            # Cerveja Equilibrada
            self.mostura_frame_nome_cerveja_equilibrada.pack(side=TOP)
            self.mostura_frame_cerveja_equilibrada_sc.pack(side=TOP, fill="both", after=self.mostura_frame_nome_cerveja_equilibrada)
            self.mostura_frame_cerveja_equilibrada_sm.pack(side=TOP, fill="both")
            self.mostura_frame_cerveja_equilibrada_cc.pack(side=TOP, fill="both")

            self.janela_mostura_.mainloop()
        elif self.litros.get() == "":
            messagebox.showerror("ERRO!", "Digite a quantidade de Litros!")
        else:
            self.entry_litros.delete(0, len(self.litros.get()))
            self.litros.set("")
            messagebox.showerror("ERRO!", "Valor digitado não é válido!")


if __name__ == '__main__':
    obj=interface()

