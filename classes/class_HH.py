import json

import requests


class HH():
    """
    Делает GET запрос к api hh.ru
    """
    data = []

    def __init__(self, company_names: list[str]):
        self.company_names = company_names

    def get_request(self):

        """Делает get запрос к api сайта HH.ru"""

        for name in self.company_names:
            url = "https://api.hh.ru/vacancies?text=" + name
            self.response = requests.get(url, params={'areas': 113, 'per_page': 100}).json()
            if self.response == []:
                continue
            self.data.append(self.response)

    def save_data_hh(self):

        """Сохраняет полученные данные в json файл"""

        with open('data_hh.json', 'w') as f:
            json.dump(self.data, f, indent=4)
