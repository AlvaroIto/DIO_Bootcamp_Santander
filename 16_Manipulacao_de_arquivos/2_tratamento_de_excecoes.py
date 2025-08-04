'''
Tratar erros é uma parte importante da manipulação de arquivos. Python oferece uma variedaded de exceções que nos permitem lidar com erros comuns.

Exceções mais comuns:
    - FileNotFoundError: Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretórioo especificado
    - PermissionError: Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação
    - IOError: Lançada quando ocorre um erro geral de E/S (entrada/saida) ao trabalhar com o arquivo, com problemas de permissão, falta de espaço em disco, entre outros
    - UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usandod uma codificação inadedquada.
    - UnicodeEncodeError: Lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto
    - IsADirectoryError: Lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto

Exemplo de código:
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print('Arquivo não encontrado')

    

'''
