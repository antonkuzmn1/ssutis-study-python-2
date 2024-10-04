import pickle
from datetime import datetime, timedelta


def calculate_arrival_time(departure_time, travel_time):
    departure = datetime.strptime(departure_time, "%H:%M")
    if "ч" in travel_time or "мин" in travel_time:
        travel_hours, travel_minutes = map(int, travel_time.replace("ч", "").replace("мин", "").split())
    else:
        travel_hours, travel_minutes = map(int, travel_time.split(":"))
    arrival_time = departure + timedelta(hours=travel_hours, minutes=travel_minutes)
    return arrival_time.strftime("%H:%M")


# noinspection PyTypeChecker,PyShadowingNames,SpellCheckingInspection
def main():
    try:
        with open("dictionary.dat", "rb") as file:
            dictionary = pickle.load(file)
    except FileNotFoundError:
        print("Файл словаря не найден, создаем новый пустой словарь.")
        dictionary = {}

    departure_time_input = input("Введи время отправления (формат HH:MM): ")

    if departure_time_input in dictionary:
        travel_time = dictionary[departure_time_input]
        arrival_time = calculate_arrival_time(departure_time_input, travel_time)
        print(f"Время прибытия для отправления {departure_time_input}: {arrival_time}")
    else:
        travel_time_input = input("Данных нет. Введи время в пути (формат Xч Yмин или X:YY): ")
        dictionary[departure_time_input] = travel_time_input

        with open("dictionary.dat", "wb") as file:
            pickle.dump(dictionary, file)

        print(f"Новая запись добавлена: {departure_time_input} - {travel_time_input}")
