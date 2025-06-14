def exibir_menu():
    print("""
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    """)

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido para saque.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===========================\n")

# Variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha upma opção: ").lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
    elif opcao == "e":
        mostrar_extrato(saldo, extrato)
    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário!")
        break
    else:
        print("Opção inválida. Por favor, selecione novamente.")
