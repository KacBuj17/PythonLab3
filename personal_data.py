import json, os
from typing import List


class PersonalData:
    def __init__(self, first_name, last_name, age, address, postal_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.postal_code = postal_code
        self.pesel = pesel


def append_to_json(objects: List[PersonalData], file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_pesels = {person['pesel'] for person in existing_data}

    new_data = [obj.__dict__ for obj in objects if obj.pesel not in existing_pesels]

    if new_data:
        existing_data.extend(new_data)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)
        print(f"Dodano {len(new_data)} nowych osób.")
    else:
        print("Brak nowych osób do dodania (wszystkie osoby z tymi samymi PESEL-ami już istnieją).")


def delete_from_json(pesel: str, file_path: str):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    person_to_remove = None
    for person in existing_data:
        if person.get('pesel') == pesel:
            person_to_remove = person
            break

    if person_to_remove:
        existing_data.remove(person_to_remove)
        print(f"Osoba z PESEL {pesel} została usunięta.")
    else:
        print(f"Osoba z PESEL {pesel} nie została znaleziona.")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)


def load_from_json(file_path: str) -> List[PersonalData]:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return [PersonalData(**item) for item in data]
            except json.JSONDecodeError:
                return []
    return []


if __name__ == "__main__":
    person1 = PersonalData("Jan", "Kowalski", 30, "Warszawa, ul. Kwiatowa 10", "00-001", "12345678901")
    person2 = PersonalData("Anna", "Nowak", 20, "Kraków, ul. Lipowa 15", "31-111", "98765432109")

    append_to_json([person1], "people.json")
    append_to_json([person2], "people.json")

    loaded_people = load_from_json("people.json")
    for person in loaded_people:
        print(person.first_name, person.last_name, person.address, person.postal_code, person.pesel)

    delete_from_json("12345678901", "people.json")

    loaded_people2 = load_from_json("people.json")
    for person in loaded_people2:
        print(person.first_name, person.last_name, person.address, person.postal_code, person.pesel)