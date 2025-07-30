'''
Geradores são tipos especiais de iteraores, ao contrário das listas ou outros iteráveis, não armazenam todos os seus valores na memória.
São definidor usando funções regulares, mas, ao invés de retornar valores usando 'return'm utilizam 'yield'

Características de geradores:
    - Uma vez que um item gerado é consumido, ele é esquecio e não pode ser acessado novamente.
    - O estado interno de um gerador é mantido entre chamadas.
    - A execução de um gerador é pausada na declaração 'yield' e retomada daí na próxima vez que ele for chamado


Recuperar dados de uma API
    - Solicitar dados por páginas (paginação)
    - Fornecer um produto por vez entre as chamadas
    - Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas.
    - Tratar o consumo da API como uma lista Python

Exemplo 1:
def meu_gerador(numeros: list[int]):
    for num in numeros:
        yield num * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

    
Exemplo 2:
import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f'{api_url}?page={page}')
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

# uso do gerador
for product in fetch_products('htpp://api.example.com/products'):
    print(product['name'])
    

'''
