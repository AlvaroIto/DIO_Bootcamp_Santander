'''
O que são e como utilizamos

Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cad objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

Exemplo:



'''

class Estudante:
    #atributos de classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        #atributos de instancia
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} ({self.matricula} - {self.escola})'

fulano = Estudante('Fulano', 123)
ciclano = Estudante('Ciclano', 124)

print(fulano)
print(ciclano)