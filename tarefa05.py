class ContaCorrente:

    def __init__(self, numeroConta, correntista, saldo = 0.0):
        self.conta = numeroConta
        self.correntista = correntista
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.correntista = novoNome

    def deposito(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
        else:
            return False

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

conta1 = ContaCorrente(1452, 'Joelma Oliveira')

print(f'A conta {conta1.conta} pertence a {conta1.correntista} e tem o saldo de R$ {conta1.saldo} ')
conta1.saldo = 1000.00
print(f'A conta {conta1.conta} pertence a {conta1.correntista} e tem o saldo de R$ {conta1.saldo} ')
conta1.alterarNome("Ana Maria")

if conta1.sacar(500) == True:
    print("Saque efetuadao! Novo Saldo:")
    print(f'Conta: {conta1.conta} - Saldo: R$ {conta1.saldo} ')
else:
    print("A conta não possui saldo para saque!")

if conta1.sacar(500) == True:
    print("Saque efetuadao! Novo Saldo:")
    print(f'Conta: {conta1.conta} - Saldo: R$ {conta1.saldo} ')
else:
    print("A conta não possui saldo para saque!")

if conta1.sacar(500) == True:
    print("Saque efetuadao! Novo Saldo:")
    print(f'Conta: {conta1.conta} - Saldo: R$ {conta1.saldo} ')
else:
    print("A conta não possui saldo para saque!")

print(f'A conta {conta1.conta} pertence a {conta1.correntista} e tem o saldo de R$ {conta1.saldo} ')
