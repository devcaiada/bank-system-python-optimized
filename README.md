# Sistema Bancário Otimizado com Python

Desafio proposto na trilha de python da DIO.

## Objetivo Geral

Utilizando o [primeiro desafio](https://github.com/devcaiada/bank-system-python-dio), separar as funções existentes de **saque, depósito, e extrato** em funções. Criar duas novas funções: **cadastrar usuário** (cliente) e **cadastrar conta bancária**.

## Código original

```python
menu = """
--------------------------------
======== Menu Principal ========
|| Opções:                    ||
||  (D) Depositar             ||
||  (S) Sacar                 ||
||  (E) Extrato               ||
||  (X) Sair                  ||
================================
>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro de operação! Valor inválido.")

    elif opcao.lower() == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro de operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Erro de operação! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Erro de operação! Número máximo de saques diário excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao.lower() == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print("Volte sempre!")
```

A partir desse código que as funções deveriam ser criadas e implementado mais duas novas funcionalidades.

## Código final

```python
import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    || (1)\tDepositar                   ||
    || (2)\tSacar                       ||
    || (3)\tExtrato                     ||
    || (4)\tNovo usuário                ||
    || (5)\tNova conta                  ||
    || (6)\tListar contas               ||
    || (0)\tSair                        ||
    ======================================
    >> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nXX Operação falhou! O valor informado é inválido. XX")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nXX Operação falhou! Você não tem saldo suficiente. XX")

    elif excedeu_limite:
        print("\nXX Operação falhou! O valor do saque excede o limite. XX")

    elif excedeu_saques:
        print("\nXX Operação falhou! Número máximo de saques excedido. XX")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\nXX Operação falhou! O valor informado é inválido. XX")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nXX Já existe usuário com esse CPF! XX")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nXX Usuário não encontrado, fluxo de criação de conta encerrado! XX")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
```

## Conclusão

Através das funções o código ficou mais limpo e de fácil manuntenção. Eu importei o arquivo bank para um main, na qual contrui o sistema bancário, chamando as funções e tratando eventuais erros.

```python
from bank import *
```
