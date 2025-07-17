'''
O que é polimorfismo?

A palavra polimorfismo significa ter muitas formas. Na porgramação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.

Exemplo:
len('Python') #conta números de caracteres
len([10, 20, 30]) #conta elementos de uma lista

Polimorfismo como herança

Na herança, a classe filha herda os métodos da classe pai. No entanto, é poossível modificar um método em uma classe filha herdada da classe pai. Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

Exemplo:

'''

class Passaro:
    def voar(self): 
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa')

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())