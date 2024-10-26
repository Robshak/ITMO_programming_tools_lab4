import unittest
import ctypes
import os

lib_path = os.path.join(os.path.dirname(__file__), "CPPProject", "project.dll")
math_lib = ctypes.CDLL(lib_path)

# Указываем аргументы и возвращаемое значение для функции C++
math_lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
math_lib.add.restype = ctypes.c_int

# Класс тестов для проверки функции add
class TestMathUtils(unittest.TestCase):
    def test_add(self):
        # Успешный случай
        self.assertEqual(math_lib.add(2, 3), 5, "Должно быть 5")
        
        # Проверка с отрицательными числами
        self.assertEqual(math_lib.add(-1, -1), -2, "Должно быть -2")
        
        # Проверка при одном отрицательном числе
        self.assertEqual(math_lib.add(-1, 1), 0, "Должно быть 0")

if __name__ == "__main__":
    unittest.main()
