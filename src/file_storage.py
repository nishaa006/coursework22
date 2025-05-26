from abc import ABC, abstractmethod
import json
import os
from src.vacancy import Vacancy

class FileStorage(ABC):
    """Абстрактный класс для хранилищ вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy): pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[Vacancy]: pass

    @abstractmethod
    def delete_vacancy(self, title: str): pass


class JSONStorage(FileStorage):
    """Хранилище вакансий в формате JSON."""

    def __init__(self, filename: str = "vacancies.json"):
        """Создаёт файл, если он не существует."""
        self._filename = filename
        if not os.path.exists(self._filename):
            with open(self._filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)

    def _load(self) -> list[dict]:
        """Загружает данные из файла."""
        with open(self._filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, vacancies: list[dict]):
        """Сохраняет данные в файл."""
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию в хранилище."""
        data = self._load()
        data.append(vacancy.to_dict())
        self._save(data)

    def get_vacancies(self, keyword: str = "") -> list[Vacancy]:
        """
        Возвращает список вакансий, содержащих ключевое слово в описании.
        """
        data = self._load()
        result = []
        for v in data:
            if isinstance(v, dict):
                description = v.get("description", "").lower()
                if keyword.lower() in description:
                    result.append(Vacancy(**v))
        return result

    def delete_vacancy(self, title: str):
        """
        Удаляет вакансию по названию.
        """
        data = self._load()
        new_data = []

        for item in data:
            if isinstance(item, dict):
                if item.get("title") != title:
                    new_data.append(item)
            else:
                new_data.append(item)

        self._save(new_data)

    def get_vacancies_by_title(self, keyword: str) -> list[Vacancy]:
        """
        Возвращает список вакансий, в названии которых содержится ключевое слово.
        """
        data = self._load()
        filtered = []
        for item in data:
            if isinstance(item, dict) and keyword.lower() in item.get("name", "").lower():
                filtered.append(Vacancy(
                    title=item.get("name"),
                    link=item.get("link"),
                    salary=item.get("salary"),
                    description=item.get("description")
                ))
        return filtered