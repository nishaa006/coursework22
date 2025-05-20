import unittest
import os
import json
from src.file_storage import JSONStorage
from src.vacancy import Vacancy


class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_vacancies.json"
        self.storage = JSONStorage(filename=self.test_file)


    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


    def test_add_and_get_vacancy(self):
        vacancy = Vacancy(
            title="Python Developer",
            link="http://example.com",
            salary={"from": 100000, "to": 150000},
            description="Python, Django"
        )
        self.storage.add_vacancy(vacancy)
        result = self.storage.get_vacancies("python")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]._title, "Python Developer")



    def test_duplicate_vacancy_not_added(self):
        vacancy = Vacancy(
            title="Python Developer",
            link="http://example.com",
            salary={"from": 100000, "to": 150000},
            description="Python, Flask"
        )
        self.storage.add_vacancy(vacancy)
        self.storage.add_vacancy(vacancy)  # Повторно

        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)


    def test_delete_vacancy(self):
        vacancy = Vacancy(
            title="To Delete",
            link="http://example.com",
            salary={"from": 100000, "to": 150000},
            description="Удалить эту вакансию"
        )
        self.storage.add_vacancy(vacancy)
        self.storage.delete_vacancy("To Delete")

        result = self.storage.get_vacancies("Удалить")
        self.assertEqual(len(result), 0)


    def test_get_vacancies_no_match(self):
        vacancy = Vacancy(
            title="Java Developer",
            link="http://example.com",
            salary={"from": 80000, "to": 120000},
            description="Java, Spring"
        )
        self.storage.add_vacancy(vacancy)
        result = self.storage.get_vacancies("python")
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
