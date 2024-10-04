def load_dictionary(dictionary_file):
    dictionary = {}
    with open(dictionary_file, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                en_word, ru_word = line.strip().split("\\t-\\t")
                dictionary[en_word.lower()] = ru_word
    return dictionary


def translate_line(line, dictionary):
    translated_line = []
    words = line.split()

    for word in words:
        clean_word = word.strip('.,!?;:')
        lower_word = clean_word.lower()

        translated_word = dictionary.get(lower_word, clean_word)

        if word[-1] in '.,!?;:':
            translated_word += word[-1]

        translated_line.append(translated_word)

    return " ".join(translated_line)


def translate_text(input_file, output_file, dictionary):
    with open(input_file, "r", encoding="utf-8") as en_file, open(output_file, "w", encoding="utf-8") as ru_file:
        for line in en_file:
            translated_line = translate_line(line.strip(), dictionary)
            ru_file.write(translated_line + "\n")


# noinspection SpellCheckingInspection
def main():
    dictionary_file = "en-ru.dic"
    input_file = "en_text.txt"
    output_file = "ru_text.txt"

    dictionary = load_dictionary(dictionary_file)

    translate_text(input_file, output_file, dictionary)

    print(f"Перевод завершен. Результат сохранен в {output_file}")
