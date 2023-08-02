# instituição: DIO
# desafio: Sistema Bancário com Python
# dev: William Elesbão (WillTubeTech)
# data: 02.08.2023
# github: https://github.com/WilliamElesbao
# linkedin: https://www.linkedin.com/in/william-elesb%C3%A3o-869839209/
# instagram: https://www.instagram.com/willtubetech/

# importando a biblioteca datetime para registrar no extrato a data e hora das operações realizadas
from datetime import datetime
import textwrap

#funcao principal - regras definidas e operações(funcoes(menu,depositar,sacar,exibir extrato, criar usuário, filtrar usuario, criar conta, listar conta))
# + criado a função para validar o cpf digitado, se é válido
def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            #caso a lista de usuários cadastrados esteja vazia não é permitido realizar o depósito
            if usuarios == []:
                print("não há nenhuma conta cadastrada para realizar o depósito!")
            #caso tenha ao menos 1 usuário cadastrado é possível realizar o depósito
            else:
                valor = float(input("insira o valor do depósito: "))
                saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("insira o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor escolha dentro das opções informadas: ")

def menu():
    #como vistos na aula foi usado o \t para tabulação (apresentar de forma mais organizada as informações no terminal)
    menu = """\n
    ╔════════════ Bem-Vindo DIO Bank ════════════╗
    ║                                            ║
     [d]\tDepositar
     [s]\tSacar                                 
     [e]\tExtrato                               
     [nc]\tNova conta                           
     [lc]\tListar contas                        
     [nu]\tNovo usuário                         
     [q]\tSair                                  
    ║                                            
    ╚════════════════════════════════════════════╝
    → """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\t-\t{datetime.now():%d/%m/%Y %H:%M:%S}\n"
        print("\n>>> Depósito realizado com sucesso! <<<")
    else:
        print("\nxxx Operação falhou! O valor informado é inválido. xxx")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nxxx Operação falhou! Você não tem saldo suficiente. xxx")

    elif excedeu_limite:
        print("\nxxx Operação falhou! O valor do saque excede o limite permitido por saque. xxx")

    elif excedeu_saques:
        print("\nxxx Operação falhou! O número máximo de saques diário foi excedido! xxx")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\t-\t{datetime.now():%d/%m/%Y %H:%M:%S}\n"
        numero_saques += 1
        print("\n>>> Saque realizado com sucesso! <<<")

    else:
        print("\nxxx Operação falhou! O valor informado é inválido. xxx")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n════════════ EXTRATO - DIO BANK ═════════════")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("═══════════════════════════════════════════════")

def valida_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0

    # Verifica se os dígitos verificadores estão corretos
    if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
        return True

    return False

def criar_usuario(usuarios):

    while True:
        cpf = input("Digite o CPF: ")

        if valida_cpf(cpf):
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                print("\nJá possui um usuário com esse CPF cadastrado no sistema!")
                return

            nome = input("insira o nome completo: ")
            data_nascimento = input("insira a data de nascimento (dd-mm-aaaa): ")
            endereco = input("insira o endereço: ")

            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

            print(">>> Usuário criado com sucesso! <<<")
            break
        else:
            print("CPF inválido. Tente novamente.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n>>> Conta criada com sucesso! <<<")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nxxx cliente não cadastrado, criação de conta encerrada! xxx")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#invoca a funcao main para inicializacao do programa
main()