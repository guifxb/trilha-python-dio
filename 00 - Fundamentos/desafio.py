menu = """
[d] Depositar | [s] Sacar | [e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato_str = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor: int):
    global saldo, extrato_str
    if valor > 0:
        saldo += valor
        extrato_str += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito: R$ {valor:.2f}\n")

    else:
        print("Valor inválido. Refaça a operação.")

def saque(valor: int):
    global saldo, extrato_str, numero_saques
    if valor > saldo:
        print("Saldo insuficiente. Refaça a operação.")
    elif valor > limite:
        print("Valor excedido. Refaça a operação.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite diário excedido. Refaça a operação.")
    elif valor > 0:
            saldo -= valor
            extrato_str += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque: R$ {valor:.2f}\n")

    else:
        print("Valor inválido. Refaça a operação.")

def extrato():
    global extrato_str, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_str else extrato_str)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        deposito(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saque(valor)
      
    elif opcao == "e":
        extrato()
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
