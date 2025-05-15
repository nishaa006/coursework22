import unittest
from src.utils import filter_top_vacancies
from src.vacancy import Vacancy


class TestFilterTopVacancies(unittest.TestCase):
    def setUp(self):
        self.v1 = Vacancy("Junior Dev", "url1", 50000, "desc")
        self.v2 = Vacancy("Middle Dev", "url2", 100000, "desc")
        self.v3 = Vacancy("Senior Dev", "url3", 150000, "desc")
        self.v4 = Vacancy("Intern", "url4", 30000, "desc")

    def test_top_2_vacancies(self):
        vacancies = [self.v1, self.v2, self.v3, self.v4]
        result = filter_top_vacancies(vacancies, 2)
        self.assertEqual(result, [self.v3, self.v2])

    def test_top_1_vacancy(self):
        vacancies = [self.v1, self.v2, self.v3]
        result = filter_top_vacancies(vacancies, 1)
        self.assertEqual(result, [self.v3])

    def test_top_all(self):
        vacancies = [self.v1, self.v2, self.v3]
        result = filter_top_vacancies(vacancies, 5)
        self.assertEqual(result, [self.v3, self.v2, self.v1])

    def test_empty_list(self):
        result = filter_top_vacancies([], 3)
        self.assertEqual(result, [])

    def test_top_zero(self):
        result = filter_top_vacancies([self.v1, self.v2], 0)
        self.assertEqual(result, [])

    def test_with_none_salary(self):
        v_none = Vacancy("Unknown", "url", None, "desc")
        vacancies = [self.v1, self.v2, v_none]
        result = filter_top_vacancies(vacancies, 2)
        self.assertEqual(result, [self.v2, self.v1])  # None считается как 0


if __name__ == "__main__":
    unittest.main()
