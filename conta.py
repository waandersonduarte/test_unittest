

class Conta():
    
    def __init__(self, numero, nome, saldo=0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    def altera_nome(self, novo_nome):
        self.__nome = novo_nome

    def mostra_nome(self):
        return self.__nome

    def mostra_numero(self):
        return self.__numero

    def mostra_saldo(self):
        return self.__saldo

    def saque(self, valor):
        self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor
        
