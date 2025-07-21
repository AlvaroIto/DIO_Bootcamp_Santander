'''
Métoodos de classe estão ligados a classe e não ao objeto. Eles tem acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto

Metodo estático não recebe um primeiro argumento explícito. Ele também é um metódo vinculado a classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.

Diferenças:
    - Um métodoo de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um métoodo estático não.
    - Um método de classe pode acesssar ou modificar o estado da clase enquanto um método estático não pode acessá-lo ou modificá-lo.

Quando utilizar o método de classe ou estático.

    - Geralmente usamos o método de classe para criar métodos de fábrica
    - Geralmente usamos métodos estáticos para criar funções utilitárias

'''

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa('Fulano', 25)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1998, 1, 5, 'Ciclano')
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(19))
print(Pessoa.e_maior_idade(12))