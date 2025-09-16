import math, unittest

class Calculadora:
    def __init__(self):
        self.historico = []
        self.resultado = 0

    def somar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
            raise TypeError("Argumentos devem ser numeros")
        resultado = base ** expoente
        self.historico.append(f"{base} ^ {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def limpar_historico(self):
        self.historico.clear()

    def obter_ultimo_resultado(self):
        return self.resultado

class Tests(unittest.TestCase):
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

        print("Tudo certo!")

    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)       # Deve iniciar com resultado 0
        self.assertEqual(len(calc.historico), 0)  # O histórico deve começar vazio

if __name__ == "__main__":
    print("Resultados dos testes: ")
    unittest.main()
    # testes_unitarios.test_entrada_saida_soma()
    # testes_unitarios.test_entrada_saida_subtracao()
    # testes_unitarios.test_entrada_saida_multiplicacao()
    # testes_unitarios.test_entrada_saida_divisao()
    # testes_unitarios
    