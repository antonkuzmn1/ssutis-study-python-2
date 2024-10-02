import random


class Array:
    __N: int
    __Arr: list[int] | list[list[int]]

    def __init__(self, size: int, low: int = -100, high: int = 100) -> None:
        self.__N = size
        self.__Arr = [random.randint(low, high) for _ in range(size)]

    def get_size(self) -> int:
        return self.__N

    def set_size(self, size: int) -> None:
        self.__N = size

    def get_array(self) -> list[int]:
        return self.__Arr

    def set_array(self, arr: list[int]) -> None:
        self.__Arr = arr

    def calc(self):
        pass

    def processing(self):
        pass

    def print_array(self):
        pass