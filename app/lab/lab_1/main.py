import random


def get_array(length: int) -> list[int]:
    range_min = -50
    range_max = 50

    array: list[int] = []
    for _ in range(length):
        array.append(random.randint(range_min, range_max))

    return array


def process_array(arr):
    positive = [i for i, x in enumerate(arr) if x > 0]

    n = len(positive)
    for i in range(n // 2):
        arr[positive[i]], arr[positive[n - 1 - i]] = arr[positive[n - 1 - i]], arr[positive[i]]

    return arr


def main():
    # noinspection SpellCheckingInspection
    print('\n2.4 Программирование обработки одномерных массивов')

    array = get_array(int(input('\nEnter Array Length: ')))
    print('\nGenerated Array:')
    print(array)

    print('\nProcessed Array:')
    print(process_array(array))

if __name__ == '__main__':
    main()