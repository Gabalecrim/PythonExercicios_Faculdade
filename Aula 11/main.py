class ContaBancaria:
    def __init__(self, numero, titular, saldo=0.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, destino, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            destino.depositar(valor)
            print(
                f"Transferência de R${valor:.2f} para {destino.titular} realizada com sucesso."
            )
        else:
            print("Transferência não realizada. Verifique o saldo ou o valor.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.__titular}: R${self.__saldo:.2f}")

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero


class CaixaEletronico:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular):
        if numero in self.contas:
            print("Conta já existente.")
        else:
            self.contas[numero] = ContaBancaria(numero, titular)
            print(f"Conta criada para {titular} com número {numero}.")

    def acessar_conta(self, numero):
        return self.contas.get(numero, None)

    def menu(self):
        while True:
            print("\n====== Caixa Eletrônico ======")
            print("1. Criar nova conta")
            print("2. Acessar conta existente")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                numero = input("Número da conta: ")
                titular = input("Nome do titular: ")
                self.criar_conta(numero, titular)

            elif opcao == "2":
                numero = input("Número da conta: ")
                conta = self.acessar_conta(numero)
                if conta:
                    self.menu_conta(conta)
                else:
                    print("Conta não encontrada.")

            elif opcao == "3":
                print("Saindo... Obrigado por usar o Caixa Eletrônico.")
                break
            else:
                print("Opção inválida.")

    def menu_conta(self, conta):
        while True:
            print(f"\n--- Conta de {conta.titular} ---")
            print("1. Ver saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferir")
            print("5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                conta.exibir_saldo()

            elif opcao == "2":
                valor = float(input("Valor para depósito: "))
                conta.depositar(valor)

            elif opcao == "3":
                valor = float(input("Valor para saque: "))
                conta.sacar(valor)

            elif opcao == "4":
                numero_destino = input("Número da conta de destino: ")
                destino = self.acessar_conta(numero_destino)
                if destino:
                    valor = float(input("Valor para transferência: "))
                    conta.transferir(destino, valor)
                else:
                    print("Conta de destino não encontrada.")

            elif opcao == "5":
                break

            else:
                print("Opção inválida.")


# Execução do programa
if __name__ == "__main__":
    caixa = CaixaEletronico()
    caixa.menu()
