def menu():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
    [c] Criar Usuario
    [f] Criar Conta

    => """
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return valor, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUES: # type: ignore
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        for chave, valor in usuario.items():
            if valor == cpf:
                return True

def criar_usuario(usuarios):
    cpf = input("Digite o cpf: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        return print("Usuario ja cadastrado")
        
    
    nome = input("Nome Completo: ")
    nasc = input("Data de Nascimento: ")
    ende = input("Endereço completo: ")

    usuarios.append({"nome": nome, "nasc": nasc, "endereço":ende, "cpf": cpf})
    print("Usuario Criado")

def criar_conta(usuarios):
    cpf = input("Digite o cpf: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if(usuario):
        print("Conta criada com sucesso")
        return usuario
    
    print("Usuario nao encontrado")
    return 


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            extrato(saldo, extrato=extrato)

        elif opcao == "c":
            criar_usuario(usuarios)

        elif opcao == "f":
            usuario = criar_conta(usuarios)
            num_conta = len(contas) + 1

            if usuario:
                contas.append({ "usuario" : usuario, "agencia": AGENCIA, "conta": num_conta })

        elif opcao == "x":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.") 