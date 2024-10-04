from app.lab.lab_8.airplane import Airplane


# noinspection SpellCheckingInspection
class MilitaryAirplane(Airplane):
    def __init__(self, model, flight_range, weaponry):
        super().__init__(model, flight_range)
        self.weaponry = weaponry

    def processing(self):
        self.weaponry = input(f"Введите новое вооружение для {self.model}: ")

    def __str__(self):
        return super().__str__() + f", Вооружение: {self.weaponry}"