import unittest
import requests

class TestExpressServer(unittest.TestCase):

    BASE_URL = 'http://localhost:3000'

    def test_add(self):
        expected_code = 200

        response = requests.get(f'{self.BASE_URL}/add', params={'a': 2, 'b': 3})
        response_status = response.status_code
        
        if 400 <= response_status < 500:
            msg = f"Ошибка клиента: получен код {response_status}. Проверьте запрос."
        elif 500 <= response_status < 600:
            msg = f"Ошибка сервера: получен код {response_status}. Проверьте сервер."
        else:
            msg = f"Неожиданный код ответа: {response_status}."
        
        self.assertEqual(response_status, expected_code, msg)
        self.assertEqual(response.json()['result'], 5)

if __name__ == '__main__':
    unittest.main()
