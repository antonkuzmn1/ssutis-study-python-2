import random

from app.lab.lab_7.array import Array


class Matrix(Array):
    def __init__(self, rows: int, cols: int, low: int = -100, high: int = 100) -> None:
        super().__init__(rows * cols)
        self.rows = rows
        self.cols = cols
        self.__Arr = [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]

    def calc(self):
        main_diag_sum = sum(self.__Arr[i][i] for i in range(min(self.rows, self.cols)))
        anti_diag_sum = sum(self.__Arr[i][self.cols - 1 - i] for i in range(min(self.rows, self.cols)))
        return main_diag_sum - anti_diag_sum

    def processing(self):
        P = self.calc()

        for j in range(self.cols):
            column = [self.__Arr[i][j] for i in range(self.rows)]
            shift = P % self.rows
            column = column[-shift:] + column[:-shift]
            for i in range(self.rows):
                self.__Arr[i][j] = column[i]

    def print_array(self):
        for row in self.__Arr:
            print("\t".join(map(str, row)))
