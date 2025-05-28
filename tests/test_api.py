import unittest
from unittest.mock import patch, Mock
from src.api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()
        self.sample_response = {
            "items": [
                {
                    "name": "Python Developer",
                    "alternate_url": "https://hh.ru/vacancy/1",
                    "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
                    "snippet": {"responsibility": "Develop Python apps"}
                }
            ]
        }

    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = self.sample_response
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        vacancies = self.api.get_vacancies("Python")

        mock_get.assert_called_once()
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['name'], "Python Developer")

    @patch('requests.get')
    def test_get_vacancies_empty(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"items": []}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        vacancies = self.api.get_vacancies("NonExistentLanguage")
        self.assertEqual(len(vacancies), 0)

    @patch('requests.get')
    def test_get_vacancies_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("API Error")
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            self.api.get_vacancies("Python")
