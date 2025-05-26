class Vacancy:
    """
    Класс для представления вакансии.
    """

    def __init__(self, title: str, link: str, salary: dict | None, description: str):
        """
        Инициализация вакансии.

        :param title: Название вакансии
        :param link: Ссылка на вакансию
        :param salary: Зарплата (словарь с полями 'from', 'to', 'currency') или None
        :param description: Описание вакансии
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self._salary = self._parse_salary(salary)

    def _parse_salary(self, salary: dict | None) -> int:
        """
        Преобразует словарь зарплаты в одно значение (среднее) для сравнения.

        :param salary: словарь {'from': int, 'to': int}
        :return: int — средняя зарплата или 0, если данных нет
        """
        if not salary:
            return 0
        _from = salary.get("from")
        _to = salary.get("to")
        if _from and _to:
            return (_from + _to) // 2
        return _from or _to or 0

    def to_dict(self) -> dict:
        """
        Преобразует объект вакансии в словарь для JSON-сохранения.

        :return: dict
        """
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description
        }

    def __eq__(self, other):
        """
        Сравнение вакансий по зарплате или названию.

        :param other: Vacancy или str/int
        :return: bool
        """
        if isinstance(other, Vacancy):
            return self._salary == other._salary
        if isinstance(other, (int, float)):
            return self._salary == int(other)
        if isinstance(other, str):
            return self.title.lower() == other.lower()
        return False

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (для сортировки)."""
        if isinstance(other, Vacancy):
            return self._salary < other._salary
        return NotImplemented

    def __repr__(self):
        return f"Vacancy('{self.title}', salary={self._salary})"
