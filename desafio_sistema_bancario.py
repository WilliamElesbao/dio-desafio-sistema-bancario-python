# instituição: DIO
# desafio: Sistema Bancário com Python
# dev: William Elesbão (WillTubeTech)
# data: 26.07.2023
# github: https://github.com/WilliamElesbao
# linkedin: https://www.linkedin.com/in/william-elesb%C3%A3o-869839209/
# instagram: https://www.instagram.com/willtubetech/

# importando a biblioteca datetime para registrar no extrato a data e hora das operações realizadas
from datetime import datetime

# criado uma classe chamada SistemaBancario onde irá conter as funções como depósito, saque e extrato.
class SistemaBancario:

    def __init__(self):
        self.saldo = 0 # saldo inicial da conta
        self.limite = 500 # limite estimado por saque
        self.extrato = "" # extrato inicia vazio
        self.numero_saques = 0 # numero de saques por dia inicia vazio
        self.LIMITE_SAQUES_DIARIO = 3 # numero máximo de saques por dia
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f} - {datetime.now():%d/%m/%Y %H:%M:%S}\n"
        else:
            print("Operação falhou! O valor informado é inválido!")
    
    def sacar(self, valor):
        
        saldo_insuficiente = valor > self.saldo
        excedeu_limite_valor_permitido = valor > self.limite
        excedeu_limite_saques_diarios = self.numero_saques >= self.LIMITE_SAQUES_DIARIO
        
        if saldo_insuficiente:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite_valor_permitido:
            print("Operação falhou! O valor do saque excede o limite permitido por saque.")
        elif excedeu_limite_saques_diarios:
            print("Operação falhou! O número máximo de saques diário foi excedido!")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f} - {datetime.now():%d/%m/%Y %H:%M:%S}\n"
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        if self.extrato == "":
            print(f"""
            ╔════════════ EXTRATO - DIO Bank ════════════╗
             Não foram realizadas movimentações

             Saldo: R$ {self.saldo:.2f}                        
            ╚════════════════════════════════════════════╝
            """)
        else:
            print("╔════════════ EXTRATO - DIO Bank ════════════╗")
            print("\nOperação realizada           Data/Hora")
            print(f"\n{self.extrato}")
            print(f"\nSaldo: R$ {self.saldo:.2f}")
            print("╚════════════════════════════════════════════╝")

# teste do sistema bancario
if __name__ == "__main__":
    banco = SistemaBancario()

    while True:
        menu = """
        ╔════════════ Bem-Vindo DIO Bank ════════════╗
        ║ → Selecione a operação que desejas realizar║
        ║                                            ║
        ║ [d] Depositar                              ║
        ║ [s] Sacar                                  ║
        ║ [e] Extrato                                ║
        ║ [q] Sair                                   ║
        ║                                            ║
        ╚════════════════════════════════════════════╝
        ► """

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            banco.depositar(valor)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            banco.sacar(valor)

        elif opcao == "e":
            banco.exibir_extrato()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")