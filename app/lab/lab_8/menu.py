from app.lab.lab_8.airplane_park import AirplanePark
from app.lab.lab_8.military_airplane import MilitaryAirplane
from app.lab.lab_8.passenger_airplane import PassengerAirplane
from app.lab.lab_8.sport_airplane import SportAirplane


# noinspection SpellCheckingInspection
def menu():
    park = AirplanePark()

    while True:
        print("\nМеню:")
        print("1. Добавить самолет")
        print("2. Внести изменения в характеристики самолета")
        print("3. Выполнить специальную операцию")
        print("4. Удалить самолет")
        print("5. Вывести сведения о самолетах")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            model = input("Введите модель самолета: ")
            flight_range = int(input("Введите дальность полета: "))
            plane_type = input("Тип самолета (военный, пассажирский, спортивный): ").lower()

            if plane_type == "военный":
                weaponry = input("Введите вооружение: ")
                park.add_airplane(MilitaryAirplane(model, flight_range, weaponry))
            elif plane_type == "пассажирский":
                passenger_capacity = int(input("Введите число пассажирских мест: "))
                park.add_airplane(PassengerAirplane(model, flight_range, passenger_capacity))
            elif plane_type == "спортивный":
                speed_record = float(input("Введите рекорд скорости: "))
                park.add_airplane(SportAirplane(model, flight_range, speed_record))
            else:
                print("Неправильный тип самолета.")

        elif choice == "2":
            index = int(input("Введите номер самолета для изменения: "))
            park.update_airplane(index)

        elif choice == "3":
            index = int(input("Введите номер самолета для выполнения спецоперации: "))
            park.perform_special_operation(index)

        elif choice == "4":
            index = int(input("Введите номер самолета для удаления: "))
            park.remove_airplane(index)

        elif choice == "5":
            park.display_airplanes()

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неправильный ввод.")
