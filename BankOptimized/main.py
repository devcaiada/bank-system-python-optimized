from bank import *

LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
numero_conta = 1

while True:
    opcao = menu()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except:
            print("Valor inválido! Digite apenas números.")
            valor = float(input("Informe o valor correto do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))
        except:
            print("Valor inválido! Digite apenas números.")
            valor = float(input("Informe o valor correto do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
            numero_conta += 1

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        break

    else:
        print("Opção inválida! Selecione uma operação novamente.")