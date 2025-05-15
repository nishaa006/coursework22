from abc import ABC, abstractmethod
import requests

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        pass

class HeadHunterAPI(VacancyAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self._session = requests.Session()

    def _connect(self, keyword: str) -> dict:
        params = {
            "text": keyword,
            "per_page": 50
        }
        response = self._session.get(self.BASE_URL, params=params)
        if response.status_code != 200:
            raise ConnectionError("Failed to connect to HeadHunter API")
        return response.json()

    def get_vacancies(self, keyword: str) -> list:
        data = self._connect(keyword)
        return data.get("items", [])
