from abc import ABC, abstractmethod


# noinspection SpellCheckingInspection
class Airplane(ABC):
    def __init__(self, model, flight_range):
        self.model = model
        self.flight_range = flight_range

    @abstractmethod
    def processing(self):
        pass

    def __str__(self):
        return f"Модель: {self.model}, Дальность полета: {self.flight_range}"