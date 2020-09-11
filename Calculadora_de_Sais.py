
class calculo_sais():
    def __init__(self,agua,litro):
        self.tipo_de_Agua=agua
        self.litros=litro
    def calculo_sulfato_de_calcio(self):
        if self.tipo_de_Agua == '1':
            if self.tipo_de_cerveja=='1':
                self.calculo_sc=(self.litros*3.7)/10
            elif self.tipo_de_cerveja=='2':
                self.calculo_sc = (self.litros * 0.1) / 10
            elif self.tipo_de_cerveja=='3':
                self.calculo_sc = (self.litros * 2) / 10
        else:
            if self.tipo_de_cerveja=='1':
                self.calculo_sc=(self.litros*3.7)/10
            elif self.tipo_de_cerveja=='2':
                self.calculo_sc = (self.litros * 0.1) / 10
            elif self.tipo_de_cerveja=='3':
                self.calculo_sc = (self.litros * 2) / 10
        return self.calculo_sc
    def calculo_sulfato_de_magnesio(self):
        if self.tipo_de_Agua == '1':
            if self.tipo_de_cerveja=='1':
                self.calculo_sm=(self.litros*3.7)/10
            elif self.tipo_de_cerveja=='2':
                self.calculo_sm = (self.litros * 0.9) / 10
            elif self.tipo_de_cerveja=='3':
                self.calculo_sm = (self.litros * 0.8) / 10
        else:
            if self.tipo_de_cerveja=='1':
                self.calculo_sm=(self.litros*0.9)/10
            elif self.tipo_de_cerveja=='2':
                self.calculo_sm = (self.litros * 0.9) / 10
            elif self.tipo_de_cerveja=='3':
                self.calculo_sm = (self.litros * 0.8) / 10
        return self.calculo_sm
    def calculo_cloreto_de_calcio(self):
        if self.tipo_de_Agua == '1':
            if self.tipo_de_cerveja == '1':
                self.calculo_cc = (self.litros * 0.8)/10
            elif self.tipo_de_cerveja == '2':
                self.calculo_cc = (self.litros * 3.9) / 10
            elif self.tipo_de_cerveja == '3':
                self.calculo_cc = (self.litros * 2.3) / 10
        else:
            if self.tipo_de_cerveja == '1':
                self.calculo_cc = (self.litros * 0.8) / 10
            elif self.tipo_de_cerveja == '2':
                self.calculo_cc = (self.litros * 3.9) / 10
            elif self.tipo_de_cerveja == '3':
                self.calculo_cc = (self.litros * 2.3) / 10
        return self.calculo_cc
    def resultado(self):
        self.calculo_cloreto_de_calcio()
        self.calculo_sulfato_de_calcio()
        self.calculo_sulfato_de_magnesio()
        print(self.tipoa,'\n',self.tipoc,'\nSulfato de Cálcio: ',self.calculo_sc,' g \nSulfato de Magnésio: ',self.calculo_sm,' g \n Cloreto de Cálcio: ',self.calculo_cc,' g')

if __name__ == '__main__':
    resposta='1'
    obj=calculo_sais()
    while resposta=='1':
        obj.menu()
        obj.resultado()
        resposta=input('Deseja executar novamente?\n(1)Sim\n(2)Não\n')

