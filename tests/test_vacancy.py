import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_vacancy_creation_with_int_salary(self):
        vac = Vacancy("Developer", "http://example.com", 100000, "Python dev")
        self.assertEqual(vac._salary, 100000)
        self.assertEqual(vac._title, "Developer")

    def test_vacancy_creation_with_dict_salary(self):
        vac = Vacancy("Dev", "http://example.com", {"from": 80000}, "Some desc")
        self.assertEqual(vac._salary, 80000)

    def test_vacancy_creation_with_invalid_salary(self):
        vac = Vacancy("Dev", "http://example.com", "Not a number", "desc")
        self.assertEqual(vac._salary, 0)

    def test_less_than_comparison(self):
        v1 = Vacancy("Junior", "url", 50000, "")
        v2 = Vacancy("Senior", "url", 150000, "")
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)

    def test_equal_comparison(self):
        v1 = Vacancy("A", "url", 100000, "")
        v2 = Vacancy("B", "url", 100000, "")
        self.assertTrue(v1 == v2)

    def test_to_dict(self):
        vac = Vacancy("Test", "link", 1000, "desc")
        expected = {
            "title": "Test",
            "link": "link",
            "salary": 1000,
            "description": "desc"
        }
        self.assertEqual(vac.to_dict(), expected)

    def test_str_representation(self):
        vac = Vacancy("Dev", "http://example.com", 75000, "Backend developer")
        expected = "Dev | 75000 | http://example.com\nBackend developer"
        self.assertEqual(str(vac), expected)


if __name__ == "__main__":
    unittest.main()
