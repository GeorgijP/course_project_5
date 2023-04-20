import requests


class HH():
    """
    Делает GET запрос к api hh.ru
    """
    ids = []
    vacancies_url = []

    def __init__(self, company_names: list[str]):
        self.company_names = company_names

    def get_request(self):
        for name in self.company_names:
                url = "https://api.hh.ru/employers/"
                par = {
                    'text': name,
                    'areas': 113,
                    # 'page': i,
                    # 'per_page': 1,
                }
                self.response = requests.get(url, params=par).json()
                if self.response == []:
                    continue
                self.ids.append(self.response['items'][0]['id'])

    def get_ids(self):
        for i in range(len(self.ids)):
            self.vacancies_url.append(
                f"https://hh.ru/search/vacancy?employer_id={self.ids[i]}&enable_snippets=true")


# hh = HH('Бега', 'Флораполис')
# hh.get_request()
# hh.get_ids()
# print(hh.ids)
# print(hh.vacancies_url)
