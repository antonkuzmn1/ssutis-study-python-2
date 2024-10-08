def space_string(text, width):
    result_file = open('lab7_2.txt', 'a')
    a = 0
    words = text.split()
    result = ""
    for word in words:
        result += word + width * ' '
        a += width
    result = result.strip()
    a -= width
    result_file.write(str(a) + ' ' + result + '\n')
    result_file.close()


def task_1():
    texts = open('lab7_1.txt', 'r')
    width = int(texts.readline())
    for line in texts:
        space_string(line, width)


if __name__ == '__main__':
    task_1()
