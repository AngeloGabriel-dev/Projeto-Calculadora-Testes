import unittest
from src.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    # Verifica se a aplicação permanece consistente mesmo após
    # diversas operações
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        
        # Sequência de operações: 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()
        
        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()
        
        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()
        
        # Verifica resultado final
        self.assertEqual(resultado_final, 10)
        
        # Verifica se o histórico tem 3 registros
        self.assertEqual(len(calc.historico), 3)

    # Verifica se as operações matemáticas estão sincronizadas 
    # com o histórico
    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        
        # Operações sequenciais usando o último resultado
        calc.potencia(2, 3)                     # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10

        # Verifica o último resultado
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        
        # Verifica se o histórico tem 2 registros
        self.assertEqual(len(calc.historico), 2)
        
        # Verifica se os registros corretos estão no histórico
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

    # Verifica se o historico permance consistente mesmo após
    # erro seguido de operação
    def test_integracao_erro_consistencia(self):
        calc = Calculadora()
        calc.somar(2, 2)  # 4
        with self.assertRaises(ValueError):
            calc.dividir(5, 0)  # erro
        self.assertEqual(calc.obter_ultimo_resultado(), 4)
        self.assertEqual(len(calc.historico), 1)


