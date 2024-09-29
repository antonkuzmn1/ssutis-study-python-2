import random


def main():
    print('lab1')

    array = [random.randint(-50, 50) for _ in range(30)]

    positive_indices = [i for i, num in enumerate(array) if num > 0]
    num_positives = len(positive_indices)

    for i in range(num_positives // 2):
        first_idx = positive_indices[i]
        last_idx = positive_indices[-(i + 1)]
        array[first_idx], array[last_idx] = array[last_idx], array[first_idx]

    print(array)
