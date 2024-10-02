from app.lab.lab_7.matrix import Matrix
from app.lab.lab_7.vector import Vector


# noinspection SpellCheckingInspection
def main():
    print(
        '2.10 Объектно-ориентированное программирование массивов разной размерности посредством принудительного наследования абстрактных классов')

    size = int(input("Введите количество элементов для вектора: "))
    low = int(input("Введите нижнюю границу значений: "))
    high = int(input("Введите верхнюю границу значений: "))

    vector = Vector(size=size, low=low, high=high)
    print("\nИсходный вектор:")
    vector.print_array()
    vector.processing()
    print("\nОбработанный вектор:")
    vector.print_array()

    # Ввод данных для двумерного массива (матрицы)
    rows = int(input("\nВведите количество строк для матрицы: "))
    cols = int(input("Введите количество столбцов для матрицы: "))
    low = int(input("Введите нижнюю границу значений для матрицы: "))
    high = int(input("Введите верхнюю границу значений для матрицы: "))

    matrix = Matrix(rows=rows, cols=cols, low=low, high=high)
    print("\nИсходная матрица:")
    matrix.print_array()
    print("\nP (разница диагоналей):", matrix.calc())
    matrix.processing()
    print("\nОбработанная матрица:")
    matrix.print_array()


if __name__ == '__main__':
    main()
