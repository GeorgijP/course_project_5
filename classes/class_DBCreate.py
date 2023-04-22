import psycopg2
import json

from configs.config import config, config_hh


class DBCreate():

    def creating_db(self):

        """Создает базу данных"""

        connection = psycopg2.connect(**config())
        try:
            with connection.cursor() as cur:
                connection.autocommit = True
                cur.execute("CREATE DATABASE data_hh")
        except Exception:
            print("Ошибка при создании базы данных")
        finally:
            connection.close()

    def creating_table(self):

        """Создает таблицы и заполняет их данными"""

        with open('data_hh.json', 'r') as f:
            data = json.load(f)

        connection = psycopg2.connect(**config_hh())
        connection.autocommit = True

        try:
            with connection.cursor() as cur:
                cur.execute("CREATE TABLE company(id_company int, name_company varchar(50), number_vacancies smallint)")
                cur.execute(
                    "CREATE TABLE vacancies(id_company int, id_vacancy int, name_vacancy varchar, salary int, url_vacancy varchar)")
                for index_one in range(len(data)):
                    cur.execute(f"INSERT INTO company VALUES (%s, %s, %s)",
                                (int(data[index_one]['items'][0]['employer']['id']),
                                 data[index_one]['items'][0]['employer']['name'],
                                 data[index_one]['found']))
                    for index_two in range(len(data[index_one]['items'])):
                        if data[index_one]['items'][index_two]['salary'] is None:
                            cur.execute(f"INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)",
                                        (int(data[index_one]['items'][0]['employer']['id']),
                                         int(data[index_one]['items'][index_two]['id']),
                                         data[index_one]['items'][index_two]['name'],
                                         None,
                                         data[index_one]['items'][index_two]['alternate_url']))
                        else:
                            cur.execute(f"INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)",
                                        (int(data[index_one]['items'][0]['employer']['id']),
                                         int(data[index_one]['items'][index_two]['id']),
                                         data[index_one]['items'][index_two]['name'],
                                         data[index_one]['items'][index_two]['salary']['from'],
                                         data[index_one]['items'][index_two]['alternate_url']))

        except Exception:
            print("Ошибка при записи данных")

        finally:
            connection.close()
