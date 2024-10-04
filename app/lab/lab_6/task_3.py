import re
from collections import Counter


# noinspection SpellCheckingInspection
def main():
    with open('text.txt', "r", encoding="utf-8") as file:
        text = file.read()

    text = text.lower()
    words = re.findall(r'\b[a-zA-Zа-яА-Я]{3,}\b', text)

    word_counts = Counter(words)

    top_10_words = word_counts.most_common(10)

    with open("count_words.res", "w", encoding="utf-8") as result_file:
        for word, count in top_10_words:
            result_file.write(f"{word}: {count}\n")

    print("ТОП-10 слов записаны в файл count_words.res")
