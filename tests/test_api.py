import unittest
from unittest.mock import patch, Mock
from src.api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()

    @patch('src.api.requests.Session.get')
    def test_connect_success(self, mock_get):
        # Мокаем ответ от API
        mock_response = Mock()
        expected_json = {"items": [{"name": "Python Developer"}]}
        mock_response.status_code = 200
        mock_response.json.return_value = expected_json
        mock_get.return_value = mock_response

        # Вызов
        result = self.api._connect("python")

        # Проверка
        mock_get.assert_called_once()
        self.assertEqual(result, expected_json)

    @patch('src.api.HeadHunterAPI._connect')
    def test_get_vacancies_returns_items(self, mock_connect):
        mock_connect.return_value = {"items": [{"name": "Backend Dev"}, {"name": "Data Scientist"}]}
        result = self.api.get_vacancies("backend")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Backend Dev")

    @patch('src.api.requests.Session.get')
    def test_connect_failure_raises_exception(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(ConnectionError):
            self.api._connect("java")


if __name__ == '__main__':
    unittest.main()
