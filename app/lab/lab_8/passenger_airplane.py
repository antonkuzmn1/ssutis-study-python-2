from app.lab.lab_8.airplane import Airplane


# noinspection SpellCheckingInspection
class PassengerAirplane(Airplane):
    def __init__(self, model, flight_range, passenger_capacity):
        super().__init__(model, flight_range)
        self.passenger_capacity = passenger_capacity

    def processing(self):
        self.passenger_capacity = int(input(f"Введите новое количество пассажирских мест для {self.model}: "))

    def __str__(self):
        return super().__str__() + f", Пассажирских мест: {self.passenger_capacity}"