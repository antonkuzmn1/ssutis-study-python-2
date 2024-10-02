from app.lab.lab_7.array import Array


class Vector(Array):
    def processing(self):
        arr = self.get_array()

        min_positive = min([x for x in arr if x > 0], default=None)

        if min_positive is not None:
            new_arr = [min_positive if x < 0 else x for x in arr]
            self.set_array(new_arr)
        else:
            # noinspection SpellCheckingInspection
            print("В массиве нет положительных элементов для замены")

    def print_array(self):
        print("\t".join(map(str, self.get_array())))