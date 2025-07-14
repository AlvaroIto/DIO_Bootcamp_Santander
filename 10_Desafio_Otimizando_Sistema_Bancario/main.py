import time 

# Função para realizar saque, considerando saldo, limite por saque e limite diário de saques
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print('Saldo insuficiente')
    elif valor > limite:
        print('O valor excede o limite de R$ 500,00')
    elif numero_saques >= limite_saques:
        print('Limite diário de saques atingido')
    elif valor <= 0:
        print('Valor inválido')
    else:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        numero_saques += 1
        print(f'Saque de R$ {valor:.2f} realizado com Sucesso!')

    time.sleep(2)
    return saldo, extrato, numero_saques

# Função para realizar depósito, apenas se o valor for positivo
def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print('O valor deve ser positivo.')
    else:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Depósito de R$ {valor:.2f} realizado como sucesso!')
    
    time.sleep(2)
    return saldo, extrato

# Função para exibir o extrato de movimentações e o saldo atual
def exibir_extrato(saldo, *, extrato):
    print('\n========= EXTRATO =========')
    print(extrato if extrato else 'Nenhuma movimentação realizada')
    print(f'\nSaldo atual: R$ {saldo:.2f}')
    print('===========================\n')
    time.sleep(2)


# Função para criar um novo usuário, garantindo CPF único
def criar_usuario(usuarios):
    cpf = input('Digite o CPF (somente números): ').strip()
    # Verifica se o CPF já existe
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Já existe um usuário com esse CPF.')
        time.sleep(2)
        return
    
    nome = input('Nome completo: ').strip().title()
    nascimento = input('Data de nascimento (dd/mm/aaaa): ').strip()
    endereco = input('Endereço (logradouro, nº - bairro - cidade/sigla): ').strip()

    novo_usuario = {
        'nome': nome,
        'data_nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    usuarios.append(novo_usuario)
    print('Usuario criado com sucesso!')
    time.sleep(2)

# Função para buscar um usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

# Função para criar uma nova conta vinculada a um usuário existente
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ').strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        nova_conta = {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario,
            'saldo': 0,
            'extrato': '',
            'numero_saques': 0

        }
        print(f'Conta criada com sucesso! Número: {numero_conta}')
        time.sleep(2)
        return nova_conta
    else:
        print('Usuário não encontrado. Conta não criada.')
        time.sleep(2)
        return None

# Função para buscar uma conta pelo número da conta
def filtrar_conta(numero_conta, contas):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            return conta
    return None

# Função principal que exibe o menu e gerencia as operações
def menu():
    usuarios = []
    contas = []
    agencia = '0001'
    numero_conta_seq = 1
    limite_saques = 3
    limite = 500

    while True:
        print('''
        ===== MENU =====
        [1] Criar usuário
        [2] Criar conta
        [3] Depositar
        [4] Sacar
        [5] Extrato
        [6] Sair
        ''')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            criar_usuario(usuarios)

        elif opcao == '2':
            conta = criar_conta(agencia, numero_conta_seq, usuarios)
            if conta:
                contas.append(conta)
                numero_conta_seq += 1

        elif opcao == '3':
            numero_conta = input('Informe o número da conta para depósito: ').strip()
            conta = filtrar_conta(int(numero_conta), contas)

            if conta:
                valor = float(input('Informe o valor do depósito: '))
                conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor, conta['extrato'])
            else:
                print('Conta não encontrada.')
                time.sleep(2)

        elif opcao == '4':
            numero_conta = input('Informe o número da conta para saque: ').strip()
            conta = filtrar_conta(int(numero_conta), contas)

            if conta:
                valor = float(input('Informe o valor do saque: '))
                conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
                    saldo=conta['saldo'],
                    valor=valor,
                    extrato=conta['extrato'],
                    limite=limite,
                    numero_saques=conta['numero_saques'],
                    limite_saques=limite_saques
                )
            else:
                print('Conta não encontrada.')
                time.sleep(2)

        elif opcao == '5':
            numero_conta = input('Informe o número da conta para exibir extrato: ').strip()
            conta = filtrar_conta(int(numero_conta), contas)

            if conta:
                exibir_extrato(conta['saldo'], extrato=conta['extrato'])
            else:
                print('Conta não encontrada.')
                time.sleep(2)

        elif opcao == '6':
            print('Saindo do sistema. Obrigado!')
            time.sleep(2)
            break

        else:
            print('Opção inválida. Tente novamente.')
            time.sleep(2)

if __name__ == '__main__':
    menu()
