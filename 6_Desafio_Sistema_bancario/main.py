from time import sleep

def dormir():
    sleep(1)

contas = {}
numero_conta = 1000
LIMITE_SAQUES = 3

menu_principal = """

[c] Cria Conta
[l] Logar Conta
[q] Sair

=> """

while True:
    opcao = input(menu_principal).lower()

    if opcao == "c":
        nome = str(input('Digite seu nome: ')).strip().title()
        sobrenome = str(input('Digite seu sobrenome: ')).strip().title()
        senha = input('Crie uma senha para a conta: ').strip()
        id_conta = numero_conta

        contas[id_conta] = {
            'nome': nome,
            'sobrenome': sobrenome,
            'senha': senha,
            'saldo': 0,
            'extrato': "",
            'numero_saques': 0
        }

        numero_conta += 1
        print(f'Conta criada com sucesso! Número da conta: {id_conta}')
        dormir()

    elif opcao == "l":
        
        if not contas:
            print('Ainda não há contas cadastradas. Crie uma conta primeiro')
            dormir()
            continue

        numero = int(input('Digite o número da conta: '))
        if numero in contas:
            senha = input('Digite a senha: ')
            if contas[numero]['senha'] == senha:
                print(f'Bem-vindo(a), {contas[numero]['nome']}!')

                while True:
                    menu_conta = '''
                    [d] Depositar
                    [s] Sacar
                    [t] Transferir
                    [e] Extrato
                    [q] Sair da conta
                    => '''
                    acao = input(menu_conta).lower()

                    if acao == 'd':
                        valor_deposito = float(input('Digite o valor a ser depositado: R$ '))
                        if valor_deposito > 0:
                            contas[numero]['saldo'] += valor_deposito
                            contas[numero]['extrato'] += f'Depósito: R$ {valor_deposito:.2f}\n'
                            print(f'Depósito realizado. Saldo: R$ {contas[numero]['saldo']:.2f}')
                        else:
                            print('Valor inválido')
                        dormir()

                    elif acao == 's':
                        saldo_atual = contas[numero]['saldo']

                        if saldo_atual <= 0:
                            print('Saldo insuficiente para saque.')
                            dormir()
                            continue

                        if contas[numero]['numero_saques'] >= LIMITE_SAQUES:
                            print('Limite de saques atingido.')
                            dormir()
                            continue

                        valor_saque = float(input('Digite o valor do saque: R$ '))

                        if 0 < valor_saque <= 500:
                            if valor_saque <= saldo_atual:
                                contas[numero]['saldo'] -= valor_saque
                                contas[numero]['numero_saques'] += 1
                                contas[numero]['extrato'] += f'Saque: R$ {valor_saque:.2f}\n'
                                print(f'Saque realizado. Saldo: R$ {contas[numero]["saldo"]:.2f}')
                            else:
                                print('Saldo insuficiente para este valor de saque.')
                        else:
                            print('Saque inválido. O limite por saque é R$ 500,00.')
                        dormir()
                    
                    elif acao == 'e':
                        print("===== EXTRATO =====")
                        print(contas[numero]['extrato'] if contas[numero]['extrato'] else "Nenhuma movimentação.")
                        print(f"Saldo atual: R$ {contas[numero]['saldo']:.2f}")
                        print("===================")
                        dormir()

                    elif acao == 't':
                        if contas[numero]['saldo'] <= 0:
                            print('Saldo insuficiente para realizar transferência')
                            dormir()
                            continue

                        conta_destino = input('Digite o número da conta de destino: ').strip()

                        if not conta_destino.isdigit():
                            print('Número da conta inválido')
                            dormir()
                            continue

                        conta_destino = int(conta_destino)

                        if conta_destino not in contas:
                            print('Conta de destino não encontrada.')
                            dormir()
                            continue

                        if conta_destino == numero:
                            print('Você não pode transferir para a mesma conta')
                            dormir()
                            continue

                        valor = input('Digite o valor da transferência: R$ ').strip()

                        if not valor.replace('.', '', 1).isdigit():
                            print('Valor inválido')
                            dormir()
                            continue

                        valor = float(valor)

                        if valor <= 0:
                            print('O valor deve ser maior que zero')
                            dormir()
                            continue

                        if contas[numero]['saldo'] < valor:
                            print('Saldo insuficiente para realizar a transferência')
                            dormir()
                            continue

                        contas[numero]['saldo'] -= valor
                        contas[conta_destino]['saldo'] += valor

                        contas[numero]['extrato'] += f'Transferência enviada para conta {conta_destino}: R$ {valor:.2f}\n'
                        contas[conta_destino]['extrato'] += f'Transferência recebida da conta {numero}: R$ {valor:.2f}\n'
                        
                        print(f'Transferência de R$ {valor:.2f} para a conta {conta_destino} realizada com sucesso')
                        dormir()

                    elif acao == 'q':
                        print('Saindo da conta...')
                        break
                    
                    else:
                        print('Opção inválida')
                        dormir()

            else:
                print('Senha incorreta')
                dormir()

        else:
            print('Conta não encontrada')
        dormir()
    
    elif opcao == 'q':
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida')
