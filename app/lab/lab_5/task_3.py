import pickle
import os
from datetime import datetime


class PData:
    def __init__(self, departure_point, departure_time, arrival_point, arrival_time, distance, bus_model, bus_number,
                 driver_name, frequency):
        self.departure_point = departure_point
        self.departure_time = departure_time
        self.arrival_point = arrival_point
        self.arrival_time = arrival_time
        self.distance = distance
        self.bus_model = bus_model
        self.bus_number = bus_number
        self.driver_name = driver_name
        self.frequency = frequency


# noinspection DuplicatedCode,SpellCheckingInspection
def input_data():
    departure_point = input("Введите пункт отправления: ")
    departure_time = input("Введите время отправления (HH:MM): ")
    arrival_point = input("Введите пункт прибытия: ")
    arrival_time = input("Введите время прибытия (HH:MM): ")
    distance = float(input("Введите расстояние (км): "))
    bus_model = input("Введите марку автобуса: ")
    bus_number = input("Введите госномер автобуса: ")
    driver_name = input("Введите ФИО водителя: ")
    frequency = input("Введите частоту следования: ")

    return PData(departure_point, departure_time, arrival_point, arrival_time, distance, bus_model, bus_number,
                 driver_name, frequency)


# noinspection SpellCheckingInspection
def create_list(filename):
    bus_data = []
    while True:
        bus_data.append(input_data())
        continue_input = input("Продолжить ввод? (y/n): ").lower()
        if continue_input == 'n':
            break

    with open(filename, 'wb') as f:
        # noinspection PyTypeChecker
        pickle.dump(bus_data, f)

    return len(bus_data)


# noinspection SpellCheckingInspection
def display_list(filename, message):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    with open(filename, 'rb') as f:
        bus_data = pickle.load(f)

    print(message)
    print(
        f"{'Пункт отправления':<20}{'Время отправления':<20}{'Пункт прибытия':<20}{'Время прибытия':<20}{'Расстояние':<12}{'Модель автобуса':<20}{'Госномер':<10}{'ФИО водителя':<20}{'Частота следования':<20}")
    print("-" * 170)

    for data in bus_data:
        print(
            f"{data.departure_point:<20}{data.departure_time:<20}{data.arrival_point:<20}{data.arrival_time:<20}{data.distance:<12}{data.bus_model:<20}{data.bus_number:<10}{data.driver_name:<20}{data.frequency:<20}")


# noinspection SpellCheckingInspection
def delete_record(filename, record_index):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    with open(filename, 'rb') as f:
        bus_data = pickle.load(f)

    if 0 <= record_index < len(bus_data):
        del bus_data[record_index]
        with open(filename, 'wb') as f:
            # noinspection PyTypeChecker
            pickle.dump(bus_data, f)
        print(f"Запись с индексом {record_index} успешно удалена.")
    else:
        print("Указанный индекс записи вне диапазона.")


# noinspection SpellCheckingInspection
def search_by_route_today(filename, route):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return 0

    today = datetime.now().strftime("%H:%M")
    found_records = []

    with open(filename, 'rb') as f:
        bus_data = pickle.load(f)

    for data in bus_data:
        if data.departure_point == route and data.departure_time >= today:
            found_records.append(data)

    display_list_inline(found_records)
    return len(found_records)


# noinspection SpellCheckingInspection
def display_list_inline(data_list):
    print(
        f"{'Пункт отправления':<20}{'Время отправления':<20}{'Пункт прибытия':<20}{'Время прибытия':<20}{'Расстояние':<12}{'Модель автобуса':<20}{'Госномер':<10}{'ФИО водителя':<20}{'Частота следования':<20}")
    print("-" * 170)

    for data in data_list:
        print(
            f"{data.departure_point:<20}{data.departure_time:<20}{data.arrival_point:<20}{data.arrival_time:<20}{data.distance:<12}{data.bus_model:<20}{data.bus_number:<10}{data.driver_name:<20}{data.frequency:<20}")


# noinspection SpellCheckingInspection
def main():
    filename = input("Введите имя файла для хранения данных (с расширением .dat): ")

    print("\nСоздание списка...")
    num_records = create_list(filename)
    print(f"Создано записей: {num_records}")
    display_list(filename, "Список после создания:")

    record_index = int(input("\nВведите индекс записи для удаления: "))
    delete_record(filename, record_index)
    display_list(filename, f"Список после удаления записи с индексом {record_index}:")

    route = input("\nВведите маршрут для поиска рейсов на сегодня: ")
    found_records_count = search_by_route_today(filename, route)
    print(f"Найдено записей по маршруту {route}: {found_records_count}")


if __name__ == "__main__":
    main()