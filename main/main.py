from classes.class_HH import HH
from classes.class_DBCreate import DBCreate

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
hh.save_data_hh()
dbc = DBCreate()
dbc.creating_db()
dbc.creating_table()
