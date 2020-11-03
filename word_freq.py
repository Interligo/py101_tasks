"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""


def top100_word_counter(file_path, limit_words):
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            raw_data = file.read()
            print('Файл найден. Загружаю...')
    except IOError:
        return print('Файл не найден.')

    # data cleaning
    print('Анализирую текст...')
    file_name, file_exp = file_path.split('.')
    stop_words = set(stopwords.words('russian'))
    tokens = word_tokenize(raw_data)
    clean_data = [word.lower() for word in tokens if not word.lower() in stop_words and word.isalnum()]
    words_counter = {}

    # words counting
    print('Считаю количество упоминаний...')
    for word in clean_data:
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1

    # sorting data from dict
    print('Сортирую слова по частоте употребления...')
    print()
    sorted_words_counter = list(words_counter.items())
    sorted_words_counter.sort(key=lambda i: i[1], reverse=True)
    sorted_words_counter = sorted_words_counter[:limit_words]

    # printing limit_words words
    print(f'В "{file_name}" наиболее часто повторялись следующие слова:')
    print()
    for (counter, item) in enumerate(sorted_words_counter, 1):
        print(f'{counter}. "{item[0]}": {item[1]} р.')


if __name__ == '__main__':
    from nltk import word_tokenize
    from nltk.corpus import stopwords

    top100_word_counter(file_path, limit_words)
    # top100_word_counter('text_for_word_freq.txt', 100)
    
