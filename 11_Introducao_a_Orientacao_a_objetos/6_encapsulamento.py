'''
O que é encapsulamento?

O encapsulamento é um dos concenitos fundamentais em programação orientada a objetos. Ele descreve a idéia de agrupar dados e os métodos que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodoos e pode evitar a modificação acidental de dados.
Para evitar alterações acidentais, a variável de um oobjeto só pode ser alterada pelo método desse objeto.

Em linguagens como Java e C++, existem palabras reservadas para definir o nível de acesso aos atributos e métodos dda classe. Em Python não temos palavras reservadas, porém usamos convenções no nome do recurso, para definir se a variável é pública ou privada.

Todos os recursos são públicos, a menos que o nome inicie com underline. Ou seja, o interpretador Python não irá garantir a proteção do recurso, mas pode ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado poor underline, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.

Recursos públicos - Pode ser acessado de fora da classe

Recursos privados - Só pode ser acessado pela classe

Exemplo:
class Conta:
    def __init__(self, nro_agencia , saldo=0):
        self._saldo =  saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta('0001', 1100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

##################################################################
Propety

Com property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

Exemplo:
class FOO:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = FOO(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

Exemplo2:
'''
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa('Fulano', 1988)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')