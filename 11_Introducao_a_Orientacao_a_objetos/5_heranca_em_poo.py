'''
Herança em POOO

Em programação herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

Benefícioos da herança

    - Representa bem os relacionamentos do mundo real.
    - *Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursso a uma classe sem modificá-la
    - *É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

Exemplo:
class A:
    pass
    
clas B(A):
    pass

#################################################################################################        
Herança simples

Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples.

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f'Ligando o motor da {self.__class__.__name__}')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        if self.carregado:
            print('Estou carregado')
        else:
            print('Não estou carregado')

moto = Motocicleta('preta', 'ABC-1234', 2)
print(moto)
moto.ligar_motor()

carro = Carro('branco', 'ABB-1234', 4)
print(carro)
carro.ligar_motor()

caminhao = Caminhao('azul', 'CBA-1234', 8, False)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()


#################################################################################################
Herança múltipla

Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla


class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas


    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leão(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo='preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo='marrom', cor_bico='laranja')
print(ornitorrinco)
'''
