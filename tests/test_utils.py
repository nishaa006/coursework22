import unittest
from src.utils import filter_top_vacancies
from src.vacancy import Vacancy


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy("Junior", "", {"from": 50000}, ""),
            Vacancy("Middle", "", {"from": 100000}, ""),
            Vacancy("Senior", "", {"from": 150000}, "")
        ]

    def test_filter_top_vacancies(self):
        top = filter_top_vacancies(self.vacancies, 2)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].title, "Senior")
        self.assertEqual(top[1].title, "Middle")

        # Test getting more than available
        top = filter_top_vacancies(self.vacancies, 5)
        self.assertEqual(len(top), 3)
        top = filter_top_vacancies([], 2)
        self.assertEqual(len(top), 0)
