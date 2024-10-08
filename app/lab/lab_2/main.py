import random

def main():
    # noinspection SpellCheckingInspection
    print('2.5 Обработка матриц')

    size = 8
    mat = [[random.randint(1, 10) for i in range(size)] for j in range(size)]

    for row in mat:
        for x in row:
            print(f"{x:4d}", end="")
        print()

    main_diag = [mat[i][i] for i in range(size)]
    side_diag = [mat[i][size - 1 - i] for i in range(size)]
    p = sum(main_diag) - sum(side_diag)
    print("Indicator is equal to: " + str(p))

    transposed_mat = list(zip(*mat))
    p = p % size
    shifted_mat = transposed_mat[-p:] + transposed_mat[:-p]
    mat = list(zip(*shifted_mat))  # транспонируем обратно
    print(f"New matrix is shifted {p % size} columns right")

    for row in mat:
        for x in row:
            print(f"{x:4d}", end="")
        print()
    print()

    x = y = 9
    m = [[0 for j in range(y)] for i in range(x)]  #
    с = 0

    for i in range(0, 9):
        ii = 0
        jj = i
        for j in range(0, i + 1):
            с += 1
            m[ii][jj] = с
            ii += 1
            jj -= 1

    for i in range(1, 9):
        ii = i
        jj = 8
        for j in range(1, 9 - i + 1):
            с += 1
            m[ii][jj] = с
            ii += 1
            jj -= 1
    print("Matrix from an illustration is: ")

    for row in m:
        for x in row:
            print(f"{x:4d}", end="")
        print()
    print()

    for i in range(9):
        for j in range(9 - i):
            m[i][j], m[8 - j][8 - i] = m[8 - j][8 - i], m[i][j]
    print("Reflected matrix is: ")

    for row in m:
        for x in row:
            print(f"{x:4d}", end="")
        print()

if __name__ == '__main__':
    main()