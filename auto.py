import unittest
from func import function


class FunctionTest(unittest.TestCase):

    def test_integers(self):
        # Позитивный тест (целые числа)
        result = function(2, 3, 5, 3, 4)
        self.assertAlmostEqual(result, 4.5)

    def test_floats(self):
        # Позитивный тест (дробные числа)
        result = function(1.5, 2.5, 4.0, 2.0, 0.25)
        self.assertAlmostEqual(result, 2.5)

    def test_zero(self):
        # Подкоренное выражение f равно нулю
        result = function(1, 1, 3, 1, 0)
        self.assertAlmostEqual(result, 1.0)

    def test_zero_division(self):
        # Тест ZeroDivisionError (c - d = 0)
        with self.assertRaises(ZeroDivisionError):
            function(5, 5, 2, 2, 9)

    def test_value_error(self):
        # Тестирование ValueError (отрицательное под корнем)
        with self.assertRaises(ValueError):
            function(4, 2, 5, 1, -4)

    def test_type_error(self):
        # Тестирование TypeError (строка вместо числа)
        with self.assertRaises(TypeError):
            function('2', 3, 5, 3, 4)

    def test_complex(self):
        # Тестирование TypeError (комплексное число)
        with self.assertRaises(TypeError):
            function(2, 3, 5, 3, complex(4, 1))
          
if __name__ == '__main__':
    unittest.main()
