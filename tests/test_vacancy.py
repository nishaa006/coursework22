import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "title": "Python Developer",
            "link": "https://example.com/vacancy/1",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "description": "Developing Python applications"
        }
        self.vacancy = Vacancy(**self.sample_data)

    def test_vacancy_creation(self):
        self.assertEqual(self.vacancy.title, "Python Developer")
        self.assertEqual(self.vacancy.link, "https://example.com/vacancy/1")
        self.assertEqual(self.vacancy.description, "Developing Python applications")
        self.assertEqual(self.vacancy._salary, 125000)  # (100000 + 150000) / 2

    def test_salary_parsing(self):
        salary = {"from": 100000, "to": 150000}
        self.assertEqual(self.vacancy._parse_salary(salary), 125000)

        salary = {"from": 100000}
        self.assertEqual(self.vacancy._parse_salary(salary), 100000)

        salary = {"to": 150000}
        self.assertEqual(self.vacancy._parse_salary(salary), 150000)

        self.assertEqual(self.vacancy._parse_salary(None), 0)

    def test_to_dict(self):
        expected_dict = {
            "title": "Python Developer",
            "link": "https://example.com/vacancy/1",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "description": "Developing Python applications"
        }
        self.assertEqual(self.vacancy.to_dict(), expected_dict)

    def test_comparison_operators(self):
        higher_vacancy = Vacancy("Senior Python", "", {"from": 200000}, "")
        lower_vacancy = Vacancy("Junior Python", "", {"from": 50000}, "")

        self.assertTrue(self.vacancy == 125000)
        self.assertTrue(self.vacancy == "python developer")
        self.assertTrue(self.vacancy == self.vacancy)

        self.assertTrue(self.vacancy < higher_vacancy)
        self.assertTrue(lower_vacancy < self.vacancy)

    def test_repr(self):
        self.assertEqual(repr(self.vacancy), "Vacancy('Python Developer', salary=125000)")
