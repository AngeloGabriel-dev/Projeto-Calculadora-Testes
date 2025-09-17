import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
        print("Teste de soma OK")
    
    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 2)
        print("Teste de subtrair OK")
    
    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)
        self.assertEqual(calc.obter_ultimo_resultado(), 15)
        print("Teste de multiplicacao OK")

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(15, 3)
        self.assertEqual(resultado, 5)
        self.assertEqual(calc.obter_ultimo_resultado(), 5)
        print("Teste de divisao OK")
    
    def test_tipagem_invalida(self):
        calc = Calculadora()
        # Somar com tipo inválido
        with self.assertRaises(TypeError):
            calc.somar("5", 3)
        with self.assertRaises(TypeError):
            calc.somar(5, "3")

        # Subtrair com tipo inválido
        with self.assertRaises(TypeError):
            calc.subtrair("5", 3)
        with self.assertRaises(TypeError):
            calc.subtrair(5, [3])

        # Multiplicar com tipo inválido
        with self.assertRaises(TypeError):
            calc.multiplicar({}, 3)
        with self.assertRaises(TypeError):
            calc.multiplicar(5, None)

        # Dividir com tipo inválido
        with self.assertRaises(TypeError):
            calc.dividir("dez", 2)
        with self.assertRaises(TypeError):
            calc.dividir(10, None)

        # Potência com tipo inválido
        with self.assertRaises(TypeError):
            calc.potencia("2", 3)
        with self.assertRaises(TypeError):
            calc.potencia(2, "3")

    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        calc.subtrair(5, 2)
        calc.dividir(15, 3)

        self.assertEqual(len(calc.historico), 4)

        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)
        self.assertIn("5 - 2 = 3", calc.historico)
        self.assertIn("15 / 3 = 5.0", calc.historico)

        calc.limpar_historico()

        self.assertEqual(len(calc.historico), 0)
        self.assertListEqual(calc.historico, [])

        print("OK")

    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)       # Deve iniciar com resultado 0
        self.assertEqual(len(calc.historico), 0)  # O histórico deve começar vazio

    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

        calc.subtrair(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
        
        calc.multiplicar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

        calc.dividir(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    def test_limite_inferior(self):
        calc = Calculadora()
        
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)

        resultado = calc.dividir(-2e-10, 2)
        self.assertEqual(resultado, -1e-10)

        resultado = calc.subtrair(0, 5)
        self.assertEqual(resultado, -5)

    def test_limite_superior(self):
        calc = Calculadora()
        
        # Teste com números grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)

        resultado = calc.multiplicar(1e10, 1e10)
        self.assertEqual(resultado, 1e20)

        resultado = calc.dividir(1e20, 1e10)
        self.assertEqual(resultado, 1e10)

        resultado = calc.subtrair(1e10, 1e10)
        self.assertEqual(resultado, 0)

    def test_divisao_por_zero(self):
        calc = Calculadora()
        
        # Testa se a divisão por zero levanta ValueError
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    def test_fluxos_divisao(self):
        calc = Calculadora()
        
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        
        # Caminho de erro (divisão por zero)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    def test_mensagens_erro(self):
        calc = Calculadora()
        
        # Verifica se a mensagem de erro da divisão por zero está correta
        with self.assertRaises(ValueError) as contexto:
            calc.dividir(5, 0)
        
        self.assertEqual(str(contexto.exception), "Divisao por zero nao permitida")


