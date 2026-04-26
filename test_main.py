import unittest

# Funções simples para testar
def soma(a, b): return a + b
def subtrai(a, b): return a - b
def multiplica(a, b): return a * b
def divide(a, b): return a / b if b != 0 else 0
def saudacao(nome): return f"Ola {nome}"

class TestProjeto(unittest.TestCase):
    def test_soma(self): self.assertEqual(soma(2, 3), 5)
    def test_subtrai(self): self.assertEqual(subtrai(10, 5), 5)
    def test_multiplica(self): self.assertEqual(multiplica(3, 3), 9)
    def test_divide(self): self.assertEqual(divide(10, 2), 5)
    def test_saudacao(self): self.assertEqual(saudacao("Fernando"), "Ola Fernando")

if __name__ == '__main__':
    unittest.main()
