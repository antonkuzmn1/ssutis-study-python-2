def sequence_processing(sequence):
    max_Li = 1000
    min_Li = 9999
    Li = "ABCD"
    for i in range(len(sequence)):
        index = (i + 1) % 4
        current_number = sequence[i].replace("\n", "")
        Li = Li.replace(Li[index], current_number[0])
        if (i % 4 == 0 and i > 0) or i == len(sequence) - 1:
            Li = Li[::-1]
            Li = Li.replace("A", "0").replace("B", "0").replace("C", "0").replace("D", "0")
            print(i, Li, int(Li))
            Li = int(Li)
            min_Li = min(min_Li, Li)
            max_Li = max(max_Li, Li)
            Li = "ABCD"
    return min_Li, max_Li


def task_2():
    file = open('sourse.dat', 'r')

    sequence = file.readlines()
    min_c, max_c = sequence_processing(sequence)

    result_file = open('results.dat', 'w')
    result_file.write(str(min_c) + "\n")
    result_file.write(str(max_c))
    result_file.close()


if __name__ == '__main__':
    task_2()
