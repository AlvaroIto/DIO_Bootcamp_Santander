'''
Nosso primeiro programa POO

João tem uma bicicleta e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos

'''

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('bip bip!!')
    
    def parar(self):
        print('Bicicleta parada')
    
    def correr(self):
        print('Bicicleta corendo')

#    def __str__(self) -> str:
#        return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

b1 = Bicicleta('branca', 'caloi', 2019, 1200)
b2 = Bicicleta('preta', 'bmw', 2020, 5000)

b1.buzinar()
b2.correr()
b1.parar()

# acessando os atributos 
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b2)


