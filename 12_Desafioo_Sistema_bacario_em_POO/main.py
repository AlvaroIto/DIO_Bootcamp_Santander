from abc import ABC, abstractmethod
from datetime import datetime


class PessoaFisica:
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Cliente(PessoaFisica):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, cpf, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    @staticmethod
    def nova_conta(cliente, numero):
        return ContaCorrente(numero, cliente)

    def sacar(self, valor):
        if valor <= 0:
            print('Valor inválido para saque.')
            return False
        elif valor > self.saldo:
            print('Saldo insuficiente.')
            return False

        self.saldo -= valor
        print(f'Saque de R${valor:.2f} realizado com sucesso!')
        return True

    def depositar(self, valor):
        if valor <= 0:
            print('Valor inválido para depósito.')
            return False

        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = 500
        self.limite_saques = 3
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print('Limite de saques diários atingido.')
            return False
        elif valor > self.limite:
            print('Valor do saque excede o limite de R$500.')
            return False
        else:
            sucesso = super().sacar(valor)
            if sucesso:
                self.numero_saques += 1
            return sucesso


def exibir_extrato(conta):
    print('\n========= EXTRATO =========')
    for transacao in conta.historico.transacoes:
        print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
    print(f'\nSaldo atual: R$ {conta.saldo:.2f}')
    print('===========================\n')


def menu():
    clientes = []
    contas = []
    numero_conta_seq = 1

    while True:
        print('''
===== MENU =====
[1] Criar cliente
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair
''')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cpf = input('CPF (somente números): ').strip()
            cliente = buscar_cliente(cpf, clientes)
            if cliente:
                print('Cliente já cadastrado.')
                continue

            nome = input('Nome completo: ').strip().title()
            nascimento = input('Data de nascimento (dd/mm/aaaa): ').strip()
            endereco = input('Endereço (logradouro, nº - bairro - cidade/UF): ').strip()
            novo_cliente = Cliente(nome, cpf, nascimento, endereco)
            clientes.append(novo_cliente)
            print('Cliente criado com sucesso!')

        elif opcao == '2':
            cpf = input('Informe o CPF do cliente: ').strip()
            cliente = buscar_cliente(cpf, clientes)
            if not cliente:
                print('Cliente não encontrado.')
                continue

            conta = ContaCorrente(numero_conta_seq, cliente)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print(f'Conta criada com sucesso! Número: {numero_conta_seq}')
            numero_conta_seq += 1

        elif opcao == '3':
            conta = selecionar_conta(contas)
            if not conta:
                continue

            valor = float(input('Valor do depósito: '))
            transacao = Deposito(valor)
            conta.cliente.realizar_transacao(conta, transacao)

        elif opcao == '4':
            conta = selecionar_conta(contas)
            if not conta:
                continue

            valor = float(input('Valor do saque: '))
            transacao = Saque(valor)
            conta.cliente.realizar_transacao(conta, transacao)

        elif opcao == '5':
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)

        elif opcao == '6':
            print('Encerrando o sistema. Até logo!')
            break

        else:
            print('Opção inválida. Tente novamente.')


def buscar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def selecionar_conta(contas):
    numero = input('Digite o número da conta: ').strip()
    for conta in contas:
        if str(conta.numero) == numero:
            return conta
    print('Conta não encontrada.')
    return None


if __name__ == '__main__':
    menu()
