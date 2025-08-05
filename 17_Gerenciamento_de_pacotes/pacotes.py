'''
Pacotes são módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você utilize código que foi escrito por outras pessoas, economizando tempo e esforço.

Pip é o gerenciador de pacotes do Python. Eles nos permite instalar, atualizar e remover pacotes facilmente. Ele se comunica com PyPI (Python Package Index), que é  onde a maioria dos pacotes Python são armazenados.
Exemplo:
pip install nome_pacote
pip uninstall nome_pacote
pip list

Uso do ambiente virtual
Ambientes virtuais, como os criados por venvs, nos permitem manter as dependências de diferentes projetos. Isso é importante para evitar conflitos entre versões de pacotes.
Exemplo:
python -m venv nome_do_ambiente_virtual
source nome_do_ambiente_virtual/bin/activate

Comandos pip
# Instalar pacote
pip install nome_pacote
# Desinstalar pacote
pip uninstall nome_pacote
# Listar pacotes instalados
pip list
# Atualizar um pacote
pip install --upgrade nome_pacote




'''