menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>
'''
saldo = 0
limite = 500
extrato = ""
qtdSaques = 0
limiteSaques = 3


def deposito(valor):
    global saldo
    global extrato
    saldo += valor
    extrato += f"deposito: {valor} \n"


def saque(valor):
    global qtdSaques
    global saldo
    global extrato
    if qtdSaques < limiteSaques and valor <= limite and saldo >= valor:
        qtdSaques += 1
        saldo -= valor
        extrato += f"saque: {valor} \n"
    elif valor > limite:
        print('Valor excedeu o limite diário.')
    elif saldo < valor:
        print('Saldo insuficiente.')
    else:
        print('Quantidade de saques diários atingida!')


while True:
    opcao = input(menu)
    if opcao == 'd':
        print("Depósito")
        valor = float(input("Valor: "))
        deposito(valor)

    elif opcao == 's':
        print("Saque")
        valor = float(input("Valor: "))
        saque(valor)

    elif opcao == 'e':
        print("Extrato")
        print(f"{extrato} \n ---- \n saldo: {saldo} \n")

    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada.")
