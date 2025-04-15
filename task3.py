import os
import pandas as pd
from enum import Enum
from Person import Person
from Student import Student
from Employee import Employee

def getNumericInput(field_name):
    value = input(f"{field_name}: ")
    while not value.isdigit():
        print(f"Error: {field_name} must be a number. {value} is not a number. Try again!")
        value = input(f"{field_name}: ")
    return int(value)

class MenuOption(Enum):
    SAVE_NEW_ENTRY = 1
    SEARCH_BY_ID = 2
    PRINT_AVERAGE_AGE = 3
    PRINT_ALL_NAMES = 4
    PRINT_ALL_IDS = 5
    PRINT_ALL_ENTRIES = 6
    PRINT_BY_INDEX = 7
    SAVE_TO_CSV = 8
    EXIT = 9

def printMenu():
    for option in MenuOption:
        print(f"{option.value}. {option.name.replace('_', ' ').title()}")

def saveNewEntry(data):
    id = input("ID: ")
    if id in data['entries']:
        existing = data['entries'][id]
        print(f"Error: Id already exists {{ 'name': {existing.getName()}, 'age': {existing.getAge()} }}")
        return

    if not id.isdigit():
        print(f"Error: ID must be a number, {id} is not a number")
        return

    name = input("Name: ")
    age = getNumericInput("Age")

    print("Is this person:")
    print("1. Regular Person\n2. Student\n3. Employee")
    type_choice = input("Choose option (1-3): ")

    if type_choice == "2":
        field_of_study = input("Field of study: ")
        year_of_study = getNumericInput("Year of study")
        score_avg = getNumericInput("Score average")
        person = Student(name, age, field_of_study, year_of_study, score_avg)
    elif type_choice == "3":
        field_of_work = input("Field of work: ")
        salary = getNumericInput("Salary")
        person = Employee(name, age, field_of_work, salary)
    else:
        person = Person(name, age)

    data['records'].append(id)
    data['entries'][id] = person
    data['age_sum'] += person.getAge()

    print(f"ID [{id}] saved successfully")

def printRecord(id, person):
    print(f"ID: {id}")
    person.printMyself()

def printAgesAverage(data):
    if len(data['records']) == 0:
        print("0")
    else:
        print(f"{data['age_sum'] / len(data['records']):.2f}")

def printAllNames(data):
    for i, id in enumerate(data['records']):
        print(f"{i}. {data['entries'][id].getName()}")

def printAllIds(data):
    for i, id in enumerate(data['records']):
        print(f"{i}. {id}")

def printAllEntries(data):
    for i, id in enumerate(data['records']):
        printRecord(id, data['entries'][id])

def searchById(data):
    id_val = input("Please enter the ID you want to look for: ")
    if not id_val.isdigit():
        print(f"Error: ID must be a number. {id_val} is not a number.")
        return

    if id_val in data['entries']:
        printRecord(id_val, data['entries'][id_val])
    else:
        print(f"Error: ID {id_val} is not saved")

def printEntryByIndex(data):
    index = input("Please enter the index of the entry you want to print: ")
    if not index.isdigit():
        print(f"Error: Index must be a number. {index} is not a number.")
        return

    index = int(index)
    if 0 <= index < len(data['records']):
        id = data['records'][index]
        printRecord(id, data['entries'][id])
    else:
        print(f"Index out of range. The maximum index allowed is {len(data['records']) - 1}")

def transformToDict(data):
    result = []
    for id in data['records']:
        person = data['entries'][id]
        row = person.to_dict()
        row['id'] = id
        result.append(row)
    return result

def saveAllData(data):
    file_name = input("What is your output CSV file name? ").strip()
    if not file_name.endswith('.csv'):
        file_name += '.csv'

    mapped_data = transformToDict(data)
    df = pd.DataFrame(mapped_data)
    df.to_csv(file_name, index=False)
    print(f"File saved at {file_name}")

def main():
    data = {
        'records': [],
        'entries': {},
        'age_sum': 0
    }

    while True:
        printMenu()
        try:
            choice = int(input("Please enter your choice: "))
            option = MenuOption(choice)
        except (ValueError, KeyError):
            print("Invalid choice, try again.")
            continue

        if option == MenuOption.SAVE_NEW_ENTRY:
            saveNewEntry(data)
        elif option == MenuOption.SEARCH_BY_ID:
            searchById(data)
        elif option == MenuOption.PRINT_AVERAGE_AGE:
            printAgesAverage(data)
        elif option == MenuOption.PRINT_ALL_NAMES:
            printAllNames(data)
        elif option == MenuOption.PRINT_ALL_IDS:
            printAllIds(data)
        elif option == MenuOption.PRINT_ALL_ENTRIES:
            printAllEntries(data)
        elif option == MenuOption.PRINT_BY_INDEX:
            printEntryByIndex(data)
        elif option == MenuOption.SAVE_TO_CSV:
            saveAllData(data)
        elif option == MenuOption.EXIT:
            ans = input("Are you sure? (y/n) ").strip().lower()
            while ans not in ('y', 'n'):
                ans = input("Are you sure? (y/n) ").strip().lower()
            if ans == 'y':
                print('Goodbye!')
                break
        input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
