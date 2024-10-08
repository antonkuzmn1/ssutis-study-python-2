def space_string(text, width):
    a = 0
    words = text.split()
    result = ""

    for word in words:
        result += word + width * ' '
        a += width

    result = result.strip()
    a -= width

    return result, a


# noinspection SpellCheckingInspection
def main():
    print('2.6 Алгоритмизация обработки символьных строк. Пользовательские функции')

    text = input("Введите строку: ")
    width = int(input("Введите ширину: "))
    result_string, result = space_string(text, width)
    print(f"Разреженная строка: {result_string}")
    print(f"Суммарное количество добавленных пробелов: {result}")


if __name__ == '__main__':
    main()
