import unittest

class TestMetodosDeString(unittest.TestCase):
    def test_primeira_letra_maiuscula(self):
        palavra='ifpi'
        self.assertEqual(palavra.capitalize(), 'Ifpi', f"a palavra {palavra} não está com a primeira letra em maiuscula.")
       

    def test_palavra_toda_maiuscula(self):
        palavra = 'ifpi'.upper()
        self.assertTrue(palavra.isupper(), f"A palavra não está em maiúscula")
    

    def test_dividir_frase_em_palavra(self):
        frase = 'ifpi 2022'
        #self.assertEqual(frase.split(" "), ['ifpi', '2022'])
        self.assertEqual(frase.split(), ['ifpi', '2022'])
