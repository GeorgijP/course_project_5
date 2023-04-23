from classes.class_HH import HH
from classes.class_DBCreate import DBCreate
from classes.class_DBManager import DBManager

if __name__ == "__main__":

    # Запрашиваем названия компаний
    company_names = []
    for i in range(10):
          company_name = input(f'Введите название {i + 1} компании: ')
          company_names.append(company_name)

    # Список для проверки
    # company_names = [
    #     'CAPYBARA IT AGENCY',
    #     'IT-Prof',
    #     'ics-it',
    #     'Ventra IT Solutions',
    #     'Capital-IT',
    #     'I Like IT',
    #     'Labirint IT',
    #     'Kamensk-IT',
    #     'zGroup-IT',
    #     'Surf IT',
    # ]

    hh = HH(company_names)  # Создаем экземпляр класс HH и передаем в него список компаний
    hh.get_request()  # Вызваем метод get_request для получения данных с сайта HH.ru
    hh.save_data_hh()  # Вызваем метод save_data_hh для сохранения в json файл данных полученных ранее

    dbc = DBCreate()  # Создаем экземпляр класс DBCreating
    dbc.creating_db()  # Вызваем метод creating_db для создания базы данных
    dbc.creating_table()  # Вызваем метод creating_table для создания таблиц

    dbm = DBManager()  # Создаем экземпляр класс DBManager

    # Запускаем цикл взаимодействия с пользвателем
    user_input = 0
    while user_input != 6:
        user_input = int(input("Выберете номер интересующей информации:\n"
                               "1 - список всех компаний и количество вакансий у каждой компании\n"
                               "2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
                               "3 - средняя зарплату по вакансиям\n"
                               "4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
                               "5 - список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”\n"
                               "6 - остановить работу программы\n"
                               ">>> "
                               ))
        if user_input == 1:
            dbm.get_companies_and_vacancies_count()
        elif user_input == 2:
            dbm.get_all_vacancies()
        elif user_input == 3:
            dbm.get_avg_salary()
        elif user_input == 4:
            dbm.get_vacancies_with_higher_salary()
        elif user_input == 5:
            dbm.get_vacancies_with_keyword()
        elif user_input == 6:
            print('\nПрограмма остановлена.')
        else:
            print('\nВведено неизвестное значение.\n')
