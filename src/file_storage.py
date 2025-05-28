from abc import ABC, abstractmethod
import json
import os
from src.vacancy import Vacancy


class FileStorage(ABC):
    """Абстрактный класс для хранилищ вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy): pass

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]: pass

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
        if vacancy.to_dict() not in data:
            data.append(vacancy.to_dict())
            self._save(data)

    def get_vacancies(self) -> list[Vacancy]:
        """
        Возвращает список всех вакансий.
        """
        data = self._load()
        result = []
        for v in data:
            result.append(Vacancy(**v))
        return result

    def delete_vacancy(self, title: str):
        """
        Удаляет вакансию по названию.
        """
        data = self._load()
        new_data = [item for item in data if isinstance(item, dict) and item.get("title") != title]
        self._save(new_data)

    def get_vacancies_by_description(self, keyword: str) -> list[Vacancy]:
        """
        Возвращает список вакансий, в описании которых содержится ключевое слово.
        """
        data = self._load()
        filtered = []
        for item in data:
            if isinstance(item, dict) and keyword.lower() in item.get("description", "").lower():
                filtered.append(Vacancy(
                    title=item.get("title"),
                    link=item.get("link"),
                    salary=item.get("salary"),
                    description=item.get("description")
                ))
        return filtered