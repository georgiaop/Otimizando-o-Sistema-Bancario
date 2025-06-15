def calcular_saldo(transacoes):
    saldo = sum(transacoes)
    print(f"Saldo: R$ {saldo:.2f}")


transacoes = [2000, -500,-200]
calcular_saldo(transacoes)

#================ EXTRATO ================
#Depósito:       R$ 2000.00
#saque:          R$ 500.00
#saque:          R$ 200.00

#Saldo:          R$ 1300.00