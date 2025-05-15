def filter_top_vacancies(vacancies: list, top_n: int) -> list:
    return sorted(vacancies, reverse=True)[:top_n]