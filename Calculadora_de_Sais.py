
class calculo_sais():
    def menu(self):
        self.tipo_de_Agua=input('Selecione o tipo de água a ser utilizada:\n (1)Água de Lavagem\n(2)Água de Mostura\n')
        if self.tipo_de_Agua == '1' or self.tipo_de_Agua == '2':
            if self.tipo_de_Agua=='1':
                print('Água de Lavagem selecionada!')
                self.tipoa='Água de Lavagem'
            if self.tipo_de_Agua=='2':
                print('Água de Mostura  selecionada!')
                self.tipoa='Água de Mostura'
        else:
            print('ERRO!OPÇÃO DIGITADA NÃO É UMA OPÇÃO VÁLIDA!')
            self.tipo_de_Agua = input('Selecione novamente o tipo de água a ser utilizada:\n(1)Água de Lavagem \n(2)Água de Mostura\n')
            while self.tipo_de_Agua != '1' and self.tipo_de_Agua != '2':
                print('ERRO!OPÇÃO DIGITADA NÃO É UMA OPÇÃO VÁLIDA!')
                self.tipo_de_Agua = input('Selecione novamente o tipo de água a ser utilizada:\n(1)Água de Lavagem \n(2)Água de Mostura\n')
            if self.tipo_de_Agua=='1':
                print('Água de Lavagem selecionada!')
                self.tipoa = 'Água de Lavagem'
            if self.tipo_de_Agua=='2':
                print('Água de Mostura  selecionada!')
                self.tipoa = 'Água de Mostura'
        self.tipo_de_cerveja=input('Selecione o tipo de cerveja: \n (1)Cerveja Lupulada \n (2)Cerveja Maltada \n (3)Cerveja Equilibrada\n')
        if self.tipo_de_cerveja=='1' or self.tipo_de_cerveja=='2'or self.tipo_de_cerveja=='3':
            if self.tipo_de_cerveja=='1':
                print('Cerveja Lupulada selecionada!')
                self.tipoc='Cerveja Lupulada'
            if self.tipo_de_cerveja=='2':
                print('Cerveja Maltada selecionada!')
                self.tipoc ='Cerveja Maltada'
            if self.tipo_de_cerveja=='3':
                print('Cerveja Equilibrada selecionada!')
                self.tipoc ='Cerveja Equilibrada'
        else:
            print('ERRO!OPÇÃO DIGITADA NÃO É UMA OPÇÃO VÁLIDA!')
            self.tipo_de_cerveja=input('Selecione novamente o tipo de cerveja: \n (1)Cerveja Lupulada \n (2)Cerveja Maltada \n (3)Cerveja Equilibrada\n')
            while self.tipo_de_cerveja!='1' and self.tipo_de_cerveja!='2'and self.tipo_de_cerveja!='3':
                print('ERRO!OPÇÃO DIGITADA NÃO É UMA OPÇÃO VÁLIDA!')
                self.tipo_de_cerveja=input('Selecione novamente o tipo de cerveja: \n (1)Cerveja Lupulada \n (2)Cerveja Maltada \n (3)Cerveja Equilibrada \n')
            if self.tipo_de_cerveja == '1':
                print('Cerveja Lupulada selecionada!')
                self.tipoc = 'Cerveja Lupulada'
            if self.tipo_de_cerveja == '2':
                print('Cerveja Maltada selecionada!')
                self.tipoc = 'Cerveja Maltada'
            if self.tipo_de_cerveja == '3':
                print('Cerveja Equilibrada selecionada!')
                self.tipoc = 'Cerveja Equilibrada'
        self.litros=input('Informe a quantidade(em litros):\n')
        if self.litros.isdecimal()==False:
            print('ERRO!OPÇÃO DIGITADA NÃO É UMA OPÇÃO VÁLIDA!')
            self.litros = input('Informe novamente a quantidade(em litros):\n')
            while self.litros.isdecimal()==False:
                print('ERRO!OPÇÃO DIGITADA NÃO É UMA OPÇÃO VÁLIDA!')
                self.litros = input('Informe novamente a quantidade(em litros):\n')
            self.litros=int(self.litros)
        else:
            self.litros = int(self.litros)


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

