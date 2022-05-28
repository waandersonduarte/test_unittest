import unittest
from conta import Conta

class TestContaCorrente(unittest.TestCase):
    def test_criar_conta_sem_saldo(self):
        conta1 = Conta(123, 'wanderson', 0)
        self.assertEqual(conta1.mostra_saldo(), 0)

    def test_criar_conta_com_saldo(self):
        conta1 = Conta(123, 'wanderson', 1000)
        self.assertEqual(conta1.mostra_saldo(), 1000)

    def test_deposita_dinheiro_conta(self):
        conta1 = Conta(123, 'wanderson', 1000)
        conta1.deposita(1000)
        self.assertEqual(conta1.mostra_saldo(), 2000)

    def test_saca_dinheiro_conta(self):
        conta1 = Conta(123, 'wanderson', 1000)
        conta1.saque(100)
        self.assertEqual(conta1.mostra_saldo(), 900)

    def test_numero_conta(self):
        conta1 = Conta(123, 'wanderson', 1000)
        self.assertTrue(int(conta1.mostra_numero()))


    def test_criar_joao_da_silva(self):
        conta1 = Conta(123, 'João da Silva', 1000)
        self.assertTrue(conta1.mostra_nome(), 'João da Silva')
        