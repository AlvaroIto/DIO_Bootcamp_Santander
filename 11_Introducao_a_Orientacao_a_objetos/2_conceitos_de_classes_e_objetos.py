'''
Classes e objetos

Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

Exemplo Classe:

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print('Auau')

    def dormir(self):
        self.acordado = False
        print('ZZZZzzzzz...')

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print('Auau')

    def dormir(self):
        self.acordado = False
        print('ZZZZzzzzz...')

Exemplo objeto:

cao_1 = Cachorro('chappie', 'amarelo', False)
cao_2 = Cachorro('Aladim', 'branco e preto')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)



'''
