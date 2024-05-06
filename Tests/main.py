documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def find_person_by_document(doc_number):
    for document in documents:
        if document["number"] == doc_number:
            return document["name"]
    return "Документ не найден."

def find_shelf_by_document(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Документ не найден на полках."

def list_all_documents():
    return '\n'.join([f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"' for doc in documents])

def add_document(doc_type, doc_number, doc_name, shelf_number):
    if shelf_number not in directories:
        return "Такой полки не существует."
    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    directories[shelf_number].append(doc_number)
    return "Документ успешно добавлен."

def main_command_handler():
    while True:
        command = input("Введите команду (p, s, l, a или 'exit' для выхода): ")
        if command == 'exit':
            break
        elif command == 'p':
            doc_number = input("Введите номер документа: ")
            print(find_person_by_document(doc_number))
        elif command == 's':
            doc_number = input("Введите номер документа: ")
            print(find_shelf_by_document(doc_number))
        elif command == 'l':
            print(list_all_documents())
        elif command == 'a':
            doc_type = input("Введите тип документа: ")
            doc_number = input("Введите номер документа: ")
            doc_name = input("Введите имя владельца: ")
            shelf_number = input("Введите номер полки: ")
            print(add_document(doc_type, doc_number, doc_name, shelf_number))
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main_command_handler()