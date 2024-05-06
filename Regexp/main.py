from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# функция для исправления ФИО
def fix_names(contact):
    full_name = ' '.join(contact[:3]).split()
    return [full_name[0] if i == 0 else full_name[1] if i == 1 else (full_name[2] if len(full_name) > 2 else '') for i in range(3)] + contact[3:]

# функция для приведения номеров телефонов к единому формату
def fix_phone_numbers(contact):
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*\(?(доб\.)\s*(\d{4})\)?)?"
    replacement = r"+7(\2)\3-\4-\5 \7\8"
    contact[-2] = re.sub(pattern, replacement, contact[-2]).strip()
    return contact

# выполнение пунктов 1-3
def process_contacts(contacts):
    result = []
    temp_contacts = {}
    for contact in contacts:
        contact = fix_names(contact)
        contact = fix_phone_numbers(contact)
        key = (contact[0], contact[1])
        if key in temp_contacts:
            for i in range(len(contact)):
                if contact[i]:
                    temp_contacts[key][i] = contact[i]
        else:
            temp_contacts[key] = contact
    return list(temp_contacts.values())

contacts_list = process_contacts(contacts_list)

# сохранение данных в другой файл
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)