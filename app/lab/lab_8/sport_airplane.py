from app.lab.lab_8.airplane import Airplane


# noinspection SpellCheckingInspection
class SportAirplane(Airplane):
    def __init__(self, model, flight_range, speed_record):
        super().__init__(model, flight_range)
        self.speed_record = speed_record

    def processing(self):
        self.speed_record = float(input(f"Введите новый рекорд скорости для {self.model}: "))

    def __str__(self):
        return super().__str__() + f", Рекорд скорости: {self.speed_record} км/ч"