import random
from typing import Any

import numpy as np
from numpy import bool, unsignedinteger, signedinteger, ndarray, dtype
from numpy._typing import _8Bit, _16Bit, _32Bit, _64Bit


def get_matrix(length_x: int, length_y: int) -> int | bool | bool | unsignedinteger[_8Bit] | unsignedinteger[_16Bit] | \
                                                unsignedinteger[_32Bit] | unsignedinteger[Any] | unsignedinteger[
                                                    _64Bit] | signedinteger[_8Bit] | signedinteger[_16Bit] | \
                                                signedinteger[_32Bit] | signedinteger[Any] | signedinteger[_64Bit] | \
                                                ndarray[Any, dtype[signedinteger[Any]]] | ndarray[Any, dtype[bool]] | \
                                                ndarray[Any, dtype[signedinteger[_8Bit]]] | ndarray[
                                                    Any, dtype[signedinteger[_16Bit]]] | ndarray[
                                                    Any, dtype[signedinteger[_32Bit]]] | ndarray[
                                                    Any, dtype[signedinteger[_64Bit]]] | ndarray[
                                                    Any, dtype[unsignedinteger[_8Bit]]] | ndarray[
                                                    Any, dtype[unsignedinteger[_16Bit]]] | ndarray[
                                                    Any, dtype[unsignedinteger[_32Bit]]] | ndarray[
                                                    Any, dtype[unsignedinteger[_64Bit]]] | ndarray[
                                                    Any, dtype[unsignedinteger[Any]]]:
    range_min = -10
    range_max = 5

    return np.random.randint(range_min, range_max, (length_x, length_y))


def main():
    # noinspection SpellCheckingInspection
    print('2.5 Обработка матриц')

    matrix = get_matrix(5, 5)
    print(matrix)

if __name__ == '__main__':
    main()