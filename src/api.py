import requests
import json


class HeadHunterAPI:
    """Класс для получения вакансий с hh.ru по ключевому слову."""

    def get_vacancies(self, keyword: str) -> list[dict]:
        """Возвращает список вакансий с hh.ru по ключевому слову."""
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,
            "per_page": 100
        }
        headers = {
            "User-Agent": "HH-User-Agent"
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json().get("items", [])
