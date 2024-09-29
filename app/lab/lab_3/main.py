def split_string(input_str, char):
    pos = input_str.find(char)
    if pos == -1:
        return 0
    return input_str[:pos], input_str[pos + 1:], pos


def main():
    print('lab3')

    input_str = "hello, world"
    char = ","
    result = split_string(input_str, char)
    print(result)
