import psycopg2
from configs.config import config_hh


class DBManager():

    def get_companies_and_vacancies_count(self):
        """ Получает список всех компаний и количество вакансий у каждой компании."""
        connection = psycopg2.connect(**config_hh())
        with connection.cursor() as cur:
            cur.execute("SELECT name_company, number_vacancies FROM company")
            cur = cur.fetchall()
            for i in range(len(cur)):
                print(f"Название компании: {cur[i][0]}, количество вакансий: {cur[i][1]}")

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        connection = psycopg2.connect(**config_hh())
        with connection.cursor() as cur:
            cur.execute(
                "SELECT name_company, name_vacancy, salary, url_vacancy FROM vacancies INNER JOIN company USING(id_company)"
            )
            cur = cur.fetchall()
            for i in range(len(cur)):
                if cur[i][2] is None:
                    print(
                        f"Название компании: {cur[i][0]}\n"
                        f"Названия вакансии: {cur[i][1]}\n"
                        f"Зарплата не указана\n"
                        f"Ссылка на вакансию: {cur[i][3]}\n"
                    )
                else:
                    print(
                        f"Название компании: {cur[i][0]}\n"
                        f"Названия вакансии: {cur[i][1]}\n"
                        f"Зарплата: {cur[i][2]} рублей\n"
                        f"Ссылка на вакансию: {cur[i][3]}\n"
                    )

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        connection = psycopg2.connect(**config_hh())
        with connection.cursor() as cur:
            cur.execute("SELECT ROUND(AVG(salary)) FROM vacancies")
            cur = cur.fetchone()
            print(f"Средняя зарплата: {cur[0]} рублей")

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        connection = psycopg2.connect(**config_hh())
        with connection.cursor() as cur:
            cur.execute(
                "SELECT name_company, name_vacancy, salary, url_vacancy FROM vacancies INNER JOIN company USING(id_company) WHERE salary > (SELECT ROUND(AVG(salary)) FROM vacancies)"
            )
            cur = cur.fetchall()
            for i in range(len(cur)):
                print(
                    f"Название компании: {cur[i][0]}\n"
                    f"Названия вакансии: {cur[i][1]}\n"
                    f"Зарплата: {cur[i][2]} рублей\n"
                    f"Ссылка на вакансию: {cur[i][3]}\n"
                )

    def get_vacancies_with_keyword(self, key_word=input()):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        pass


a = DBManager()
a.get_vacancies_with_higher_salary()
