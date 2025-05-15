from functools import total_ordering

@total_ordering
class Vacancy:
    __slots__ = ("_title", "_link", "_salary", "_description")

    def __init__(self, title: str, link: str, salary: int | str, description: str):
        self._title = title
        self._link = link
        self._salary = self._validate_salary(salary)
        self._description = description

    def _validate_salary(self, salary) -> int:
        if isinstance(salary, int):
            return salary
        if isinstance(salary, dict) and salary.get("from"):
            return salary["from"]
        return 0

    def __lt__(self, other):
        return self._salary < other._salary

    def __eq__(self, other):
        return self._salary == other._salary

    def to_dict(self) -> dict:
        return {
            "title": self._title,
            "link": self._link,
            "salary": self._salary,
            "description": self._description
        }

    def __str__(self):
        return f"{self._title} | {self._salary} | {self._link}\n{self._description}"