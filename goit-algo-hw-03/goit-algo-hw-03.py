

#  ЗАВДАННЯ №1
from datetime import datetime, timedelta
import re
import random
from datetime import datetime


def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = current_date - date_object
        return delta.days
    except ValueError as e:
        print(
            "Помилка: Неправильний формат дати. Введіть коректну дату у форматі YYYY-MM-DD.")
        return None


data = "2019-01-24"
print(get_days_from_today(data))

# ЗАВДАННЯ №2


def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= (max_num - min_num + 1)):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))
    return sorted(list(numbers))


min_num = 1
max_num = 24
quantity = 12
print(get_numbers_ticket(min_num, max_num, quantity))

# Третє завдання


def normalize_phone(phone_number):
    cleaned_numbers = re.sub(r'\D', '', phone_number)
    if not cleaned_numbers.startswith('+'):
        cleaned_numbers = '+38' + cleaned_numbers.lstrip('38')
    return cleaned_numbers


phone_numbers = ["    +38(050)123-32-34",
                 "     0503451234",
                 "(050)8889900",
                 "38050-111-22-22",
                 "38050 111 22 11   "]

for number in phone_numbers:
    print(normalize_phone(number))

# Четверте завдання

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    birthdays_dict = {}

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday <= 7:
            if birthday_this_year.weekday() in [5, 6]:
                monday = today + timedelta(days=(7 - today.weekday()) + 1)
                congratulation_date = monday
            else:
                congratulation_date = birthday_this_year

            if birthday_this_year not in birthdays_dict:
                birthdays_dict[birthday_this_year] = {"congratulation_date": congratulation_date, "users": [user["name"]]}
            else:
                birthdays_dict[birthday_this_year]["users"].append(user["name"])

   
    for date, data in birthdays_dict.items():
        for name in data["users"]:
            days_until_birthday = (data["congratulation_date"] - today).days
            upcoming_birthdays.append({"name": name, "congratulation_date": data["congratulation_date"],
                                       "days_until_birthday": days_until_birthday})

    return upcoming_birthdays


def print_upcoming_birthdays(upcoming_birthdays):
    for entry in upcoming_birthdays:
        print(f"Ім'я: {entry['name']}")
        print(f"Дата народження: {entry['congratulation_date'].strftime('%Y.%m.%d')}")
        if entry['days_until_birthday'] == 0:
            print("Сьогодні день народження!")
        elif entry['days_until_birthday'] == 1:
            print("Завтра день народження!")
        else:
            print(f"Днів до дня народження: {entry['days_until_birthday']}")
        print()


users = [
    {'name': 'Jane Smith', 'birthday': '1990.03.29'},
    {'name': 'Nick Darsel', 'birthday': '1984.03.30'},
    {'name': 'John Doe', 'birthday': '1985.04.01'},
    {'name': 'Ethan Williams', 'birthday': '1970.04.02'},
    {'name': 'Smith Smith', 'birthday': '1990.04.03'},
    {'name': 'Liam Smith', 'birthday': '1995.04.04'},
    {'name': 'Liam Smith', 'birthday': '1995.04.05'},
    {'name': 'Mohel Smith', 'birthday': '1995.04.06'},
    {'name': 'John Dark', 'birthday': '1985.04.07'},
    {'name': 'Mary Dark', 'birthday': '1985.04.08'},
    {'name': 'Derek Dark', 'birthday': '1985.04.09'},
    {'name': 'Jane Smith', 'birthday': '1990.04.10'},
    {'name': 'Nick Darsel', 'birthday': '1984.04.11'},
    {'name': 'Liam Smith', 'birthday': '1995.04.12'},
    {'name': 'Mohel Smith', 'birthday': '1995.04.13'}
]

upcoming = get_upcoming_birthdays(users)
print_upcoming_birthdays(upcoming)



