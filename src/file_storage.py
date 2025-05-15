from abc import ABC, abstractmethod
import json
import os
from src.vacancy import Vacancy

class FileStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy): pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[Vacancy]: pass

    @abstractmethod
    def delete_vacancy(self, title: str): pass


class JSONStorage(FileStorage):
    def __init__(self, filename: str = "vacancies.json"):
        self._filename = filename
        if not os.path.exists(self._filename):
            with open(self._filename, "w") as f:
                json.dump([], f)

    def _load(self) -> list[dict]:
        with open(self._filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, vacancies: list[dict]):
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, indent=4)

    def add_vacancy(self, vacancy: Vacancy):
        data = self._load()
        data.append(vacancy.to_dict())
        self._save(data)

    def get_vacancies(self, keyword: str = "") -> list:
        data = self._load()
        result = []
        for v in data:
            if isinstance(v, dict):
                description = v.get("description", "").lower()
                if keyword.lower() in description:
                    result.append(Vacancy(**v))
        return result

    def delete_vacancy(self, title: str):
        data = self._load()
        new_data = []

        for item in data:
            if isinstance(item, dict):
                if item.get("title") != title:
                    new_data.append(item)
            else:
                new_data.append(item)

        self._save(new_data)

    def get_vacancies_by_title(self, keyword: str) -> list:
        """
        Возвращает список вакансий, в названии которых содержится ключевое слово.
        """
        data = self._load()
        filtered = []
        for item in data:
            if isinstance(item, dict) and keyword.lower() in item.get("title", "").lower():
                filtered.append(Vacancy(
                    title=item.get("title"),
                    link=item.get("link"),
                    salary=item.get("salary"),
                    description=item.get("description")
                ))
        return filtered
