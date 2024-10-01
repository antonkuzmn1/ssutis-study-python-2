def split_string(input_str, char):
    pos = input_str.find(char)
    if pos == -1:
        return 0
    return input_str[:pos], input_str[pos + 1:], pos


def main():
    print('2.6 Алгоритмизация обработки символьных строк. Пользовательские функции')

    input_str = "hello, world"
    char = ","
    result = split_string(input_str, char)
    print(result)

if __name__ == '__main__':
    main()