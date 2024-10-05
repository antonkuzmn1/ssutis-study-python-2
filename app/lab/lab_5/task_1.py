import pickle


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
            total_time += 24 * 60
        return self.distance / (total_time / 60)  # км/ч


# noinspection SpellCheckingInspection
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
def main():
    filename = input("Введите имя файла (с расширением .dat): ")

    bus_data = []
    while True:
        bus_data.append(input_data())
        continue_input = input("Продолжить ввод? (y/n): ").lower()
        if continue_input == 'n':
            break

    bus_data.sort(key=lambda x: x.average_speed(), reverse=True)

    with open(filename, 'wb') as f:
        # noinspection PyTypeChecker
        pickle.dump(bus_data, f)

    print(f"Данные сохранены в файл {filename}. Записей: {len(bus_data)}.")


if __name__ == "__main__":
    main()