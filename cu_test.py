import unittest
from cu import trig_test, convert_test, factorial_test

class TestCalculatorFunctions(unittest.TestCase):
    def test_trig_test(self):
        self.assertAlmostEqual(trig_test(30, "sin"), 0.5, places=2)  # sin(30°)
        self.assertAlmostEqual(trig_test(60, "cos"), 0.5, places=2)  # cos(60°)
        self.assertAlmostEqual(trig_test(45, "tg"), 1.0, places=2)   # tg(45°)
        self.assertAlmostEqual(trig_test(45, "ctg"), 1.0, places=2)  # ctg(45°)
        self.assertEqual(trig_test(90, "tg"), "Тангенс не определён для данного угла.")  # tg(90°)
        self.assertEqual(trig_test(0, "ctg"), "Котангенс не определён для данного угла.")  # ctg(0°)
    def test_convert_test(self):
        self.assertEqual(convert_test(10, 2), "1010")    # 10 в двоичной системе
        self.assertEqual(convert_test(255, 16), "FF")    # 255 в шестнадцатеричной системе
        self.assertEqual(convert_test(7, 8), "7")        # 7 в восьмеричной системе
        self.assertRaises(ValueError, convert_test, 10, 37)  # Основание > 36
        self.assertRaises(ValueError, convert_test, 10, 1)   # Основание < 2
    def test_factorial_test(self):
        self.assertEqual(factorial_test(5), 120)  # 5! = 120
        self.assertEqual(factorial_test(0), 1)    # 0! = 1
        self.assertRaises(ValueError, factorial_test, -1)  # Факториал отрицательного числа
        self.assertRaises(ValueError, factorial_test, 5.5)  # Факториал нецелого числа