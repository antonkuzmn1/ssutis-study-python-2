import random


def positive_swap(array: list, start: int, end: int):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


# noinspection SpellCheckingInspection
def main():
    print('\n2.4 Программирование обработки одномерных массивов')

    length = int(input("Введите длину массива: "))
    array = [random.randint(-50, 50) for _ in range(length)]
    print(f"Исходный массив: {array}")
    i = 0

    while i < length:
        if array[i] > 0:
            end = i

            while end < (length - 1) and array[end] > 0:
                end += 1

            if array[end] > 0:
                positive_swap(array, i, end)
                i = length

            else:
                positive_swap(array, i, end - 1)
                i = end

        else:
            i += 1

    print(f"Обработаннный массив: {array}")


if __name__ == '__main__':
    main()
