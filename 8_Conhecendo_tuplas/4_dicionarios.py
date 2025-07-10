'''
Criação e acesso aos dados

Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separados por vírgulas

Exemplo
pessoa = {'nome': 'Fulano', 'idade': 28}
pessoa = dict('nome': 'Fulano', 'idade': 28)

pessoa['telefone'] = '3333-1234' # {'nome': 'Fulano', 'idade': 28, 'telefone': '3333-1234'}

Acessando os dados

Os dados são acessados e doficados através da chave

Exemplo
{'nome': 'Fulano', 'idade': 28, 'telefone': '3333-1234'}

dados['nome'] # 'Fulano'
dados['idade'] # '28'
dados['telefone'] # '3333-1234'

dados['nome'] = 'Ciclano'
dados['idade'] = 14
dados['telefone'] = '9999-9876'

dados # {'nome': Ciclano, 'idade':'14', 'telefone':'9999-9876'}

#######################################################################
Dicinários aninhados

Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strions e números)

Exemplo
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
    'ciclano@email.com': {'nome': 'Ciclano', 'telefone': 4444-3332'},
    'maria@email.com': {'nome': 'Maria', 'telefone': 5555-4443'},
    'joao@email.com': {'nome': 'João', 'telefone': 6666-5554' 'extra': {'a': 1}},
}

contatos['ciclano@email.com']['telefone'] # '4444-3332'

extra = contatos['joao@email.com']['extra']['a'] # 1

#######################################################################
Iterar dicionários

A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for

Exemplo
for chave in contatos:
    print(chave, contatos[chave])

    for chave valor in contatos.items():
        print(chave, valor)

# 'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
# 'ciclano@email.com': {'nome': 'Ciclano', 'telefone': 4444-3332'},
# 'maria@email.com': {'nome': 'Maria', 'telefone': 5555-4443'},
# 'joao@email.com': {'nome': 'João', 'telefone': 6666-5554' 'extra': {'a': 1}},


#######################################################################
Metodos da classe dict

{}.clear
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
    'ciclano@email.com': {'nome': 'Ciclano', 'telefone': 4444-3332'},
    'maria@email.com': {'nome': 'Maria', 'telefone': 5555-4443'},
    'joao@email.com': {'nome': 'João', 'telefone': 6666-5554' 'extra': {'a': 1}},
}
contatos.clear()
contatos # {}

{}.copy
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}
copia = contatos.copy()
copia['fulano@email.com'] = {'nome':'ful'}

contatos['fulano@gmail.com] # {'nome':'Fulano', 'telefone': '3333-2221'}
copia['fulano@gmail.com] # {'nome':'ful'}

{}.fromkeys
dict.fromkeys(['nome', 'telefone']) # {'nome': None, 'telefone': None}

dict.fromkeys(['nome', 'telefone'], 'vazio') # {'nome': 'vazio', 'telefone': 'vazio'}

{}.get
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}

contatos['chave'] #KeyError

contatos.get('chave') #None
contatos.get('chave, {}) # {}
contatos.get('fulano@email.com', {}) # {'fulano@email.com': {'nome': 'Fulano', 'telefone': '333-2221'}}

{}.items
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}
contatos.items() # dict_items([('fulano@email.com', {'nome': 'Fulano', 'telefone': '3333-2221'})])

{}.keys
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}
contatos.keys() # dict_keys(['fulano@email.com'])

{}.pop
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}

contatos.pop('fulano@email.com') # {'nome': 'Fulano', 'telefone': 3333-2221'}
contato.pop('fulano@email.com', {}) #{}

{}.popitem
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}

contatos.popitem() # ('fulano@email.com', {'nome': 'Fulano', 'telefone': 3333-2221'})
contato.popitem() #KeyError

{}.setdefault
contato = {'nome': 'Fulano', 'telefone': 3333-2221'}

contato.setdefault('nome', 'Jose') # 'Fulano'
contato # {'nome': 'Fulano', 'telefone': 3333-2221'}

contato.setdefault('idade', 28) # 28
contato # {'nome': 'Fulano', 'telefone': 3333-2221', idade, 28}

{}.update
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
}

contatos.update({'fulano@email.com': {'nome':'ful'}})
contatos # {'fulano@email.com': {'nome': 'ful'}}

{}.values
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
    'ciclano@email.com': {'nome': 'Ciclano', 'telefone': 4444-3332'},
    'maria@email.com': {'nome': 'Maria', 'telefone': 5555-4443'},
    'joao@email.com': {'nome': 'João', 'telefone': 6666-5554' 'extra': {'a': 1}},
}

contatos.values() # dict_values([{'nome': 'Fulano', 'telefone': '3333-2221'}, {'nome': 'Ciclano', 'telefone': '4444-3332'}, {'nome': 'Maria', 'telefone': '5555-4443'}, {'nome': 'João', 'telefone': '6666-5554', 'extra': {'a': 1}}])

in
contatos = {
    'fulano@email.com': {'nome': 'Fulano', 'telefone': 3333-2221'},
    'ciclano@email.com': {'nome': 'Ciclano', 'telefone': 4444-3332'},
    'maria@email.com': {'nome': 'Maria', 'telefone': 5555-4443'},
    'joao@email.com': {'nome': 'João', 'telefone': 6666-5554' 'extra': {'a': 1}},
}

'fulano@email.com' in contatos # True
'teste@emaillcom' in contatos # False
'idade' in contatos['fulano@email.com'] # False
'telefone' in contatos['ciclano@email.com] # True


'''

