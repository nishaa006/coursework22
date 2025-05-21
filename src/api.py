import requests
import json


def fetch_vacancies(api_key: str, keyword: str):
    """
    Получает вакансии через API и сохраняет их в файл.

    Args:
        api_key (str): API ключ.
        keyword (str): Ключевое слово для поиска вакансий.
    """
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "per_page": 100
    }
    headers = {
        "User-Agent": "HH-User-Agent",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, params=params, headers=headers)
    vacancies = response.json().get("items", [])

    with open("vacancies.json", "w", encoding="utf-8") as f:
        json.dump(vacancies, f, indent=4)