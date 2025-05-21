from src.api import fetch_vacancies
from src.file_storage import JSONStorage
from src.utils import filter_top_vacancies
import os



def user_interaction():
    api_key = os.getenv("HH_API_KEY")
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    fetch_vacancies(api_key, keyword)

    storage = JSONStorage()

while True:
    print("\nМеню:")
    print("1. Найти вакансии")
    print("2. Показать топ N вакансий")
    print("3. Поиск по ключевому слову в описании")
    print("4. Удалить вакансию по названию")
    print("5. Выход")
    choice = input("Выберите опцию: ")

    if choice == "1":
        keyword = input("Введите ключевое слово для поиска в названии вакансии: ").strip()
        matched = JSONStorage().get_vacancies_by_title(keyword)
        if matched:
            print(f"\nНайдено {len(matched)} вакансий по ключевому слову '{keyword}':")
            for vac in matched:
                print(vac)
        else:
            print("Вакансии не найдены.")

    elif choice == "2":
        try:
            n = int(input("Сколько вакансий показать (топ по зарплате)?: "))
        except ValueError:
            print("Введите корректное число.")
            continue

        all_vacancies = JSONStorage().get_vacancies("")
        top_vacancies = filter_top_vacancies(all_vacancies, n)
        print(f"\nТОП-{n} вакансий:")
        for vac in top_vacancies:
            print(vac)

    elif choice == "3":
        keyword = input("Введите ключевое слово для поиска по описанию: ").strip()
        matched = JSONStorage().get_vacancies(keyword)
        if matched:
            print(f"\nНайдено {len(matched)} вакансий:")
            for vac in matched:
                print(vac)
        else:
            print("Вакансии не найдены.")

    elif choice == "4":
        title = input("Введите точное название вакансии для удаления: ").strip()
        JSONStorage().delete_vacancy(title)
        print(f"Вакансия '{title}' удалена, если она была найдена.")

    elif choice == "5":
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод. Пожалуйста, выберите пункт от 1 до 5.")

if __name__ == "__main__":
    user_interaction()