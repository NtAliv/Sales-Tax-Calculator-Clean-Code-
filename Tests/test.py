import unittest

import sys
sys.path.append( 'src')

from Models import app_logic

from Models import Exceptions


class TestCalculatorTax(unittest.TestCase):
    # Casos normales.

    def test_normal1(self):
        # ENTRADAS

        valor: float = 20000
        impuesto = 19 / 100


        valor_calculado = app_logic.calculate_iva(valor, impuesto)

        valor_esperado = 23800

        self.assertAlmostEqual(valor_calculado, valor_esperado, 2)
    
    def test_normal2(self):
        # ENTRADAS

        valor: float = 5800
        impuesto = 5/100

        valor_calculado = app_logic.calculate_iva(valor, impuesto)

        valor_esperado = 6090

        self.assertAlmostEqual(valor_calculado, valor_esperado, 2)
    
    def test_normal3(self):
        # ENTRADAS

        valor: float = 4000
        impuesto = 19 / 100

        valor_calculado = app_logic.calculate_iva(valor, impuesto)

        valor_esperado = 4760

        self.assertAlmostEqual(valor_calculado, valor_esperado, 2)

    def test_excento(self):
        #Caso exento de impuestos, el valor calculado debe ser igual al valor ingresado.
        # ENTRADAS
  
        valor = 18000
        impuesto = 0

        valor_calculado = app_logic.calculate_iva(valor, impuesto)
        valor_esperado = 18000

        self.assertEqual(valor_calculado, valor_esperado)

    def test_licores(self):
        #Caso de calculo de licores, se espera
        # ENTRADAS

        valor = 112000
        impuesto = 19/100
        grado = 40
        volumen = 750
        tarifa = 342

        calular_licor = app_logic.calculate_licores(valor, grado, tarifa, volumen)

        valor_calculado = app_logic.calculate_iva(calular_licor, impuesto)
        valor_esperado = 149559.2

        self.assertAlmostEqual(valor_calculado, valor_esperado, 2)
    
    def test_impuesto_nacional_consumo(self):
        # ENTRADAS
        valor = 14000
        impuesto = 10/100

        calular_licor = app_logic.calculte_impuesto_nacional_consumo(valor, impuesto)

        valor_esperado = 15400

        self.assertAlmostEqual(calular_licor, valor_esperado, 2)
    
    def test_bolsa(self):
        # Impuesto de bolsa, se espera que el valor calculado sea igual al valor ingresado mas el impuesto.
         # ENTRADAS
    
        impuesto = 75
        numero_bolsas = 10
        
        calular_bolsa = app_logic.Calculate_bolsa(impuesto, numero_bolsas)

        valor_esperado = 750

        self.assertAlmostEqual(calular_bolsa, valor_esperado, 2)
    
    def test_error_negativo(self):
        #Caso de valor negativo, se espera que el valor calculado sea igual al valor ingresado.
        # ENTRADAS

        valor = -10000
        impuesto = 19/100

        with self.assertRaises(Exceptions.NegativeValueError):
            app_logic.calculate_iva(valor, impuesto)
    
    def test_error_compra(self):
    #Caso de valor igual a 0, se espera que el valor calculado sea igual al mensaje de error.
        # ENTRADAS
        
        valor = 0
        impuesto = 19/100
        
        with self.assertRaises(Exceptions.ZeroValueError):
            app_logic.calculate_iva(valor, impuesto)
            app_logic.calculte_impuesto_nacional_consumo(valor, impuesto)
            app_logic.Calculate_bolsa(impuesto, 10)

    def test_error_IVA(self):
    # Caso de IVA mayor al permitido, se espera que el valor calculado sea igual al mensaje de error.
        # ENTRADAS
        valor = 10000
        impuesto = 20 /100

        with self.assertRaises(Exceptions.InvalidTaxError):
            app_logic.calculate_iva(valor, impuesto)      
    

    def test_errror_IVA_negativo(self):
    # Caso de IVA negativo, se espera que el valor calculado sea igual al mensaje de error.
        # ENTRADAS
        valor = 10000
        impuesto = -10 /100

        with self.assertRaises(Exceptions.NegativeIVAError):
            app_logic.calculate_iva(valor, impuesto)
    

if __name__ == "__main__":
    unittest.main()