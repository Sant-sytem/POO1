import abc
from datetime import datetime

class Usuario(abc.ABC):
    """Classe abstrata para definir atributos e metodos comuns aos usuários"""
    
    def __init__(self, nome, cpf, endereco):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
    
    @abc.abstractmethod
    def __str__(self):
        pass

class Cliente(Usuario):
    """Classe que representa um cliente"""
    
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf, endereco)
        self.conta_corrente = None
        self.conta_poupanca = None
        self.seguros = []
    
    def __str__(self):
        return f"Nome: {self._nome}, CPF: {self._cpf}, Endereco: {self._endereco}"

class SeguroDeVida:
    """Classe para representar o seguro de vida"""
    
    def __init__(self, cpf, valor_mensal, valor_total):
        self._cpf = cpf
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total

class Conta(abc.ABC):
    """Classe abstrata para as contas bancarias"""
    
    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo
        self._historico = []

    def depositar(self, valor):
        self._saldo += valor
        self._historico.append(f"Deposito: R${valor}")
    
    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
            return False
        self._saldo -= valor
        self._historico.append(f"Saque: R${valor}")
        return True
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            self._historico.append(f"Transferencia para conta {conta_destino._numero}: R${valor}")
            return True
        return False
    
    def exibir_historico(self):
        print(f"Historico da Conta {self._numero}:")
        for transacao in self._historico:
            print(transacao)

    @abc.abstractmethod
    def calcular_tributacao(self):
        pass

class ContaCorrente(Conta):
    """Classe que representa uma conta corrente"""
    
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)
    
    def calcular_tributacao(self):
        return self._saldo * 0.01

class ContaPoupanca(Conta):
    """Classe que representa uma conta poupança"""
    
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)
    
    def calcular_tributacao(self):
        return 0  

class Banco:
    """Classe que representa o banco e suas operações"""
    
    def __init__(self):
        self.clientes = {}
        self.seguros = []
        self.tributacao_total = 0
        self.historico_tributacao = []
    
    def cadastrar_cliente(self, nome, cpf, endereco):
        if cpf in self.clientes:
            print(f"Cliente com CPF {cpf} ja cadastrado!")
            return
        cliente = Cliente(nome, cpf, endereco)
        self.clientes[cpf] = cliente
        print(f"Cliente {nome} cadastrado com sucesso!")
    
    def criar_conta_corrente(self, cpf, numero, saldo_inicial):
        cliente = self.clientes.get(cpf)
        if cliente and cliente.conta_corrente is None:
            cliente.conta_corrente = ContaCorrente(numero, saldo_inicial)
            print(f"Conta Corrente {numero} criada com sucesso!")
        else:
            print(f"Cliente {cpf} ja possui um CPF com essa conta corrente.")
    
    def criar_conta_poupanca(self, cpf, numero, saldo_inicial):
        cliente = self.clientes.get(cpf)
        if cliente and cliente.conta_poupanca is None:
            cliente.conta_poupanca = ContaPoupanca(numero, saldo_inicial)
            print(f"Conta Poupança {numero} criada com sucesso!")
        else:
            print(f"Cliente {cpf} ja possui um CPF com essa conta poupanca.")
    
    def criar_seguro(self, cpf, valor_mensal, valor_total):
        cliente = self.clientes.get(cpf)
        if cliente:
            seguro = SeguroDeVida(cpf, valor_mensal, valor_total)
            cliente.seguros.append(seguro)
            print(f"Seguro de vida criado para o cliente {cpf}.")
    
    def calcular_tributacao(self):
        tributacao_total = 0
        for cliente in self.clientes.values():
            tributacao = 10  
            if cliente.conta_corrente:
                tributacao += cliente.conta_corrente.calcular_tributacao()
            if cliente.seguros:
                for seguro in cliente.seguros:
                    tributacao += seguro._valor_mensal * 0.02
            tributacao_total += tributacao
            self.historico_tributacao.append(tributacao_total)
        self.tributacao_total = tributacao_total
        print(f"Total da tributação calculada: R${tributacao_total:.2f}")
    
    def mostrar_historico_tributacao(self):
        if not self.historico_tributacao:
            print("Não há histórico de tributação.")
        else:
            print("Histórico de Tributação:")
            for idx, valor in enumerate(self.historico_tributacao, start=1):
                print(f"{idx}ª tributação = {valor:.2f}")
    
    def exibir_informacoes_banco(self):
        print(f"Total de clientes cadastrados: {len(self.clientes)}")
        for cliente in self.clientes.values():
            print(cliente)
            conta_corrente = cliente.conta_corrente
            conta_poupanca = cliente.conta_poupanca
            if conta_corrente:
                print(f"Conta Corrente: R${conta_corrente._saldo:.2f}")
            else:
                print("Conta Corrente: Nenhuma")
            if conta_poupanca:
                print(f"Conta Poupança: R${conta_poupanca._saldo:.2f}")
            else:
                print("Conta Poupança: Nenhuma")
            print(f"Seguros de vida: {len(cliente.seguros)}")
    
    def mostrar_menu(self):
        while True:
            print("\n1 - Cadastrar Cliente")
            print("2 - Criar Conta Corrente")
            print("3 - Criar Conta Poupança")
            print("4 - Criar Seguro de Vida")
            print("5 - Calcular Tributacao (taxando com sucesso)")
            print("6 - Exibir Informações do Banco")
            print("7 - Sacar")
            print("8 - Depositar")
            print("9 - Transferir")
            print("10 - Exibir Historico")
            print("0 - Sair")
            
            opcao = int(input("Escolha uma opcao: "))
            
            if opcao == 1:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                endereco = input("Endereco: ")
                self.cadastrar_cliente(nome, cpf, endereco)
            
            elif opcao == 2:
                cpf = input("CPF do cliente: ")
                numero = input("Numero da conta: ")
                saldo_inicial = float(input("Saldo inicial: "))
                self.criar_conta_corrente(cpf, numero, saldo_inicial)
            
            elif opcao == 3:
                cpf = input("CPF do cliente: ")
                numero = input("Numero da conta: ")
                saldo_inicial = float(input("Saldo inicial: "))
                self.criar_conta_poupanca(cpf, numero, saldo_inicial)
            
            elif opcao == 4:
                cpf = input("CPF do cliente: ")
                valor_mensal = float(input("Valor mensal: "))
                valor_total = float(input("Valor total: "))
                self.criar_seguro(cpf, valor_mensal, valor_total)
            
            elif opcao == 5:
                self.calcular_tributacao()
            
            elif opcao == 6:
                self.exibir_informacoes_banco()
            
            elif opcao == 7:
                cpf = input("CPF do cliente: ")
                cliente = self.clientes.get(cpf)
                if cliente:
                    conta = cliente.conta_corrente if cliente.conta_corrente else cliente.conta_poupanca
                    if conta:
                        valor = float(input("Valor para saque: "))
                        conta.sacar(valor)
                else:
                    print("Cliente não encontrado.")
            
            elif opcao == 8:
                cpf = input("CPF do cliente: ")
                cliente = self.clientes.get(cpf)
                if cliente:
                    conta = cliente.conta_corrente if cliente.conta_corrente else cliente.conta_poupanca
                    if conta:
                        valor = float(input("Valor para deposito: "))
                        conta.depositar(valor)
                else:
                    print("Cliente nao encontrado.")
            
            elif opcao == 9:
                cpf_origem = input("CPF do cliente origem: ")
                cpf_destino = input("CPF do cliente destino: ")
                valor = float(input("Valor para transferencia: "))
                cliente_origem = self.clientes.get(cpf_origem)
                cliente_destino = self.clientes.get(cpf_destino)
                if cliente_origem and cliente_destino:
                    conta_origem = cliente_origem.conta_corrente if cliente_origem.conta_corrente else cliente_origem.conta_poupanca
                    conta_destino = cliente_destino.conta_corrente if cliente_destino.conta_corrente else cliente_destino.conta_poupanca
                    if conta_origem and conta_destino:
                        conta_origem.transferir(valor, conta_destino)
                else:
                    print("Clientes nao encontrados.")
            
            elif opcao == 10:
                cpf = input("CPF do cliente: ")
                cliente = self.clientes.get(cpf)
                self.mostrar_historico_tributacao()  
                if cliente:
                    conta = cliente.conta_corrente if cliente.conta_corrente else cliente.conta_poupanca
                    if conta:
                        conta.exibir_historico()  
                else:
                    print("Cliente nao encontrado.")
            
            elif opcao == 0:
                print("Saindo...")
                break
            else:
                print("Opcao invalida.")


banco = Banco()
banco.mostrar_menu()
