
class calculo_sais():
    def __init__(self,agua,litro):
        self.tipo_de_Agua=agua
        self.litros=litro

    #Calculos para cerveja Lupulada
    def cerveja_lupulada_sulfato_de_Calcio(self):#1
        if self.tipo_de_Agua == '1':
            self.c_lup_calculo_sc = (self.litros * 3.7) / 10
        else:
            self.c_lup_calculo_sc = (self.litros * 3.7) / 10
        return self.c_lup_calculo_sc
    def cerveja_lupulada_sulfato_de_magnesio(self):#1
        if self.tipo_de_Agua == '1':
            self.c_lup_calculo_sm = (self.litros * 3.7) / 10
        else:
            self.c_lup_calculo_sm=(self.litros*0.9)/10
        return self.c_lup_calculo_sm
    def cerveja_lupulada_cloreto_De_calcio(self):#1
        if self.tipo_de_Agua == '1':
            self.c_lup_calculo_cc = (self.litros * 0.8) / 10
        else:
            self.c_lup_calculo_cc=(self.litros*0.8)/10
        return self.c_lup_calculo_cc

    #cerveja maltada
    def cerveja_maltada_sulfato_de_Calcio(self):
        if self.tipo_de_Agua == '1':
            self.c_malt_calculo_sc = (self.litros * 0.1) / 10
        else:
            self.c_malt_calculo_sc = (self.litros * 0.1) / 10
        return self.c_malt_calculo_sc
    def cerveja_maltada_sulfato_de_magnesio(self):
        if self.tipo_de_Agua == '1':
            self.c_malt_calculo_sm = (self.litros * 0.9) / 10
        else:
            self.c_malt_calculo_sm = (self.litros * 0.9) / 10
        return self.c_malt_calculo_sm
    def cerveja_maltada_cloreto_De_calcio(self):
        if self.tipo_de_Agua == '1':
            self.c_malt_calculo_cc = (self.litros * 3.9) / 10
        else:
            self.c_malt_calculo_cc = (self.litros * 3.9) / 10
        return self.c_malt_calculo_cc

    #Cerveja Equilibrada
    def cerveja_equilibrada_sulfato_de_Calcio(self):
        if self.tipo_de_Agua == '1':
            self.c_equi_calculo_sc = (self.litros * 2) / 10
        else:
            self.c_equi_calculo_sc = (self.litros * 2) / 10
        return self.c_equi_calculo_sc
    def cerveja_equilibrada_sulfato_de_magnesio(self):
        if self.tipo_de_Agua == '1':
            self.c_equi_calculo_sm = (self.litros * 0.8) / 10
        else:
            self.c_equi_calculo_sm = (self.litros * 0.8) / 10
        return self.c_equi_calculo_sm
    def cerveja_equilibrada_cloreto_de_calcio(self):
        if self.tipo_de_Agua == '1':
            self.c_equi_calculo_cc = (self.litros * 2.3) / 10
        else:
            self.c_equi_calculo_cc = (self.litros * 2.3) / 10
        return self.c_equi_calculo_cc

    def resultado(self):
        self.calculo_cloreto_de_calcio()
        self.calculo_sulfato_de_calcio()
        self.calculo_sulfato_de_magnesio()
        print(self.tipoa,'\n',self.tipoc,'\nSulfato de Cálcio: ',self.calculo_sc,' g \nSulfato de Magnésio: ',self.calculo_sm,' g \n Cloreto de Cálcio: ',self.calculo_cc,' g')


