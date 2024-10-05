import pickle
import os


# Структура данных для хранения информации об автобусных рейсах
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

    def average_speed(self):
        dep_hours, dep_minutes = map(int, self.departure_time.split(':'))
        arr_hours, arr_minutes = map(int, self.arrival_time.split(':'))
        total_dep_minutes = dep_hours * 60 + dep_minutes
        total_arr_minutes = arr_hours * 60 + arr_minutes
        total_time = total_arr_minutes - total_dep_minutes
        if total_time <= 0:
            total_time += 24 * 60  # если время прибытия на следующий день
        return self.distance / (total_time / 60)  # км/ч


def print_table(data_list):
    print(
        f"{'Пункт отправления':<20}{'Время отправления':<20}{'Пункт прибытия':<20}{'Время прибытия':<20}{'Расстояние':<12}{'Модель автобуса':<20}{'Госномер':<10}{'ФИО водителя':<20}{'Частота следования':<20}{'Ср. скорость (км/ч)':<15}")
    print("-" * 170)
    for data in data_list:
        print(
            f"{data.departure_point:<20}{data.departure_time:<20}{data.arrival_point:<20}{data.arrival_time:<20}{data.distance:<12}{data.bus_model:<20}{data.bus_number:<10}{data.driver_name:<20}{data.frequency:<20}{data.average_speed():<15.2f}")


def load_data(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return None
    with open(filename, 'rb') as f:
        return pickle.load(f)


def main():
    filename = input("Введите имя файла для загрузки (с расширением .dat): ")

    bus_data = load_data(filename)
    if bus_data is None:
        return

    print("\nЗагруженные данные:")
    print_table(bus_data)

    # Сортировка по убыванию средней скорости
    bus_data.sort(key=lambda x: x.average_speed(), reverse=True)

    print("\nОтсортированные данные (по убыванию средней скорости):")
    print_table(bus_data)


if __name__ == "__main__":
    main()