import unittest
import os
import json
from tempfile import NamedTemporaryFile
from src.file_storage import JSONStorage
from src.vacancy import Vacancy


class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        self.temp_file = NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.storage = JSONStorage(self.temp_file.name)

        self.sample_vacancy = Vacancy(
            title="Python Developer",
            link="https://example.com/vacancy/1",
            salary={"from": 100000, "to": 150000},
            description="Develop Python apps"
        )

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_add_vacancy(self):
        self.storage.add_vacancy(self.sample_vacancy)

        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Python Developer")

    def test_add_duplicate_vacancy(self):
        self.storage.add_vacancy(self.sample_vacancy)
        self.storage.add_vacancy(self.sample_vacancy)  # Add same vacancy again

        with open(self.temp_file.name, 'r') as f:
            data = json.load(f)

        self.assertEqual(len(data), 1)  # Should still be only one

    def test_get_vacancies(self):
        self.storage.add_vacancy(self.sample_vacancy)
        vacancies = self.storage.get_vacancies()

        self.assertEqual(len(vacancies), 1)
        self.assertIsInstance(vacancies[0], Vacancy)
        self.assertEqual(vacancies[0].title, "Python Developer")

    def test_get_vacancies_by_description(self):
        self.storage.add_vacancy(self.sample_vacancy)

        found = self.storage.get_vacancies_by_description("python")
        self.assertEqual(len(found), 1)

        not_found = self.storage.get_vacancies_by_description("java")
        self.assertEqual(len(not_found), 0)

    def test_delete_vacancy(self):
        self.storage.add_vacancy(self.sample_vacancy)
        self.storage.delete_vacancy("Python Developer")

        vacancies = self.storage.get_vacancies()
        self.assertEqual(len(vacancies), 0)
