class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.deposits = []
        self.withdrawals = []
        self.max_withdrawals_per_day = 3
        self.withdrawal_limit = 500.00
        self.withdrawals_today = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.deposits.append(valor)
            print(f"Depósito realizado: R$ {valor:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if self.withdrawals_today >= self.max_withdrawals_per_day:
            print("Limite de saques diários atingido.")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        elif valor > self.withdrawal_limit:
            print(f"O valor do saque não pode exceder R$ {self.withdrawal_limit:.2f}.")
        else:
            self.saldo -= valor
            self.withdrawals.append(valor)
            self.withdrawals_today += 1
            print(f"Saque realizado: R$ {valor:.2f}")
    
    def extrato(self):
        if not self.deposits and not self.withdrawals:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.deposits:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.withdrawals:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")
    
    def resetar_saques_diarios(self):
        self.withdrawals_today = 0
        print("Contador de saques diários resetado.")

# Exemplo de uso
conta = ContaBancaria()
conta.depositar(1500.00)
conta.sacar(200.00)
conta.sacar(500.00)
conta.sacar(600.00)  # Exemplo de saque acima do limite
conta.extrato()
conta.resetar_saques_diarios()  # Reseta o contador de saques diários
