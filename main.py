from utils import HH

company_names = [
    'CAPYBARA IT AGENCY',
    'IT-Prof',
    'ics-it',
    'Ventra IT Solutions',
    'Capital-IT',
    'I Like IT',
    'Labirint IT',
    'Kamensk-IT',
    'zGroup-IT',
    'Surf IT',
]

# for i in range(10):
#     company_name = input(f'Введите название {i + 1} компании: ')
#     company_names.append(company_name)

hh = HH(company_names)
hh.get_request()
hh.get_ids()
print(hh.vacancies_url)
