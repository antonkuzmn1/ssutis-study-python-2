# noinspection SpellCheckingInspection
class AirplanePark:
    def __init__(self):
        self.airplanes = []

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)

    def update_airplane(self, index):
        if 0 <= index < len(self.airplanes):
            self.airplanes[index].processing()
        else:
            print("Самолет с таким номером не найден.")

    def remove_airplane(self, index):
        if 0 <= index < len(self.airplanes):
            del self.airplanes[index]
        else:
            print("Самолет с таким номером не найден.")

    def perform_special_operation(self, index):
        if 0 <= index < len(self.airplanes):
            self.airplanes[index].processing()
        else:
            print("Самолет с таким номером не найден.")

    def display_airplanes(self):
        if not self.airplanes:
            print("Коллекция пустая.")
        for i, airplane in enumerate(self.airplanes):
            print(f"{i}. {airplane}")
