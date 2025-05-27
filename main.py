from src.api import HeadHunterAPI
from src.file_storage import JSONStorage
from src.utils import filter_top_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """Основной цикл взаимодействия с пользователем."""
    api = HeadHunterAPI()
    storage = JSONStorage()

    while True:
        print("\nМеню:")
        print("1. Найти и сохранить вакансии по ключевому слову")
        print("2. Показать топ N вакансий по зарплате")
        print("3. Поиск по ключевому слову в описании")
        print("4. Удалить вакансию по названию")
        print("5. Выход")
        choice = input("Выберите опцию: ").strip()

        if choice == "1":
            keyword = input("Введите ключевое слово для поиска: ").strip()
            vacancies_data = api.get_vacancies(keyword)
            if not vacancies_data:
                print("Вакансии не найдены.")
                continue

            for item in vacancies_data:
                vacancy = Vacancy(
                    title=item.get("name"),
                    link=item.get("alternate_url"),
                    salary=item.get("salary"),
                    description=item.get("snippet", {}).get("responsibility", "")
                )
                storage.add_vacancy(vacancy)

            print(f"Сохранено {len(vacancies_data)} вакансий.")

        elif choice == "2":
            try:
                n = int(input("Сколько вакансий показать (ТОП по зарплате)?: "))
            except ValueError:
                print("Введите корректное число.")
                continue

            all_vacancies = storage.get_vacancies()
            top_vacancies = filter_top_vacancies(all_vacancies, n)
            print(f"\nТОП-{n} вакансий:")
            for vac in top_vacancies:
                print(vac)

        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска по описанию: ").strip()
            matched = storage.get_vacancies(keyword)
            if matched:
                print(f"\nНайдено {len(matched)} вакансий:")
                for vac in matched:
                    print(vac)
            else:
                print("Вакансии не найдены.")

        elif choice == "4":
            title = input("Введите точное название вакансии для удаления: ").strip()
            storage.delete_vacancy(title)
            print(f"Вакансия '{title}' удалена, если она была найдена.")

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.")


if __name__ == "__main__":
    user_interaction()