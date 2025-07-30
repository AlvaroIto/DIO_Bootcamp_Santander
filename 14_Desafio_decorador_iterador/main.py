from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep
from functools import wraps


def log_transacao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tipo = func.__name__.capitalize()
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f'[LOG - {data_hora}] Iniciando transação: {tipo}')
        resultado = func(*args, **kwargs)
        print(f'[LOG - {data_hora}] Finalizando transação: {tipo}\n')
        return resultado
    return wrapper

def gerar_relatorio(historico, tipo=None):
    for transacao in historico.transacoes:
        if tipo is None or transacao['tipo'].lower() == tipo.lower():
            yield transacao


class ContaIterador:
    def __init__(self, contas):
        self._contas = contas
        self._indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._indice >= len(self._contas):
            raise StopIteration
        conta = self._contas[self._indice]
        self._indice += 1
        return f'Conta Nº {conta.numero} | Saldo: R$ {conta.saldo:.2f}'


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
        if not conta.historico.pode_transacionar():
            print('Transação não permitida: limite diário atingido.')
            return

        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        if not conta.historico.pode_transacionar():
            print('Transação não permitida: limite diário atingido.')
            return

        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self.transacoes = []
        self.transacoes_por_dia = {}
        self.limite_diario = 5

    def adicionar_transacao(self, transacao):
        hoje = datetime.now().date()

        if self.transacoes_por_dia[hoje] >= self.limite_diario:
            print('Limite diário de transações atingido.')
            return False

        self.transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })
        self.transacoes_por_dia[hoje] += 1
        return True

    def pode_transacionar(self):
        hoje = datetime.now().date()
        return self.transacoes_por_dia[hoje] < self.limite_diario


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    @staticmethod
    @log_transacao
    def nova_conta(cliente, numero):
        return ContaCorrente(numero, cliente)

    @log_transacao
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

    @log_transacao
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
[6] Gerar relatório
[7] Todas as Contas
[8] Sair
''')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cpf = input('CPF (somente números): ').strip()
            cliente = buscar_cliente(cpf, clientes)
            if cliente:
                print('Cliente já cadastrado.')
                sleep(1)
                continue

            nome = input('Nome completo: ').strip().title()
            nascimento = input('Data de nascimento (dd/mm/aaaa): ').strip()
            endereco = input('Endereço (logradouro, nº - bairro - cidade/UF): ').strip()
            novo_cliente = Cliente(nome, cpf, nascimento, endereco)
            clientes.append(novo_cliente)
            print('Cliente criado com sucesso!')
            sleep(1)

        elif opcao == '2':
            cpf = input('Informe o CPF do cliente: ').strip()
            cliente = buscar_cliente(cpf, clientes)
            if not cliente:
                print('Cliente não encontrado.')
                sleep(1)
                continue

            conta = ContaCorrente(numero_conta_seq, cliente)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print(f'Conta criada com sucesso! Número: {numero_conta_seq}')
            sleep(1)
            numero_conta_seq += 1

        elif opcao == '3':
            conta = selecionar_conta(contas)
            if not conta:
                print('Não há contas criadas')
                sleep(1)
                continue

            valor = float(input('Valor do depósito: '))
            transacao = Deposito(valor)
            conta.cliente.realizar_transacao(conta, transacao)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            sleep(1)

        elif opcao == '4':
            conta = selecionar_conta(contas)
            if not conta:
                print('Não há contas criadas')
                sleep(1)
                continue

            valor = float(input('Valor do saque: '))
            transacao = Saque(valor)
            conta.cliente.realizar_transacao(conta, transacao)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            sleep(1)

        elif opcao == '5':
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)
                sleep(1)

        elif opcao == '6':
            conta = selecionar_conta(contas)
            if conta:
                tipo = input('Filtrar por tipo (Saque, Deposito ou deixar vazio): ').strip()
                print('\n==== RELATÓRIO ====    ')
                for t in gerar_relatorio(conta.historico, tipo=tipo if tipo else None):
                    print(f'{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}')
                print('=======================\n')
                sleep(1)
        
        elif opcao == '7':
            print('\n=== Toddas as Contas ===')
            for info in ContaIterador(contas):
                print(info)
            print('========================\n')
            sleep(1)

        elif opcao == '8':
            print('Encerrando o sistema. Até logo!')
            sleep(1)
            break

        else:
            print('Opção inválida. Tente novamente.')
            sleep(1)


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
