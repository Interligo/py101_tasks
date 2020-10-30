"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

def top100_word_counter(file_path):
    # WORD_LIMIT = 100
    
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            stop_words = set(stopwords.words('english'))
            words = []
            TODO: добавить текст без стоп-слов в список words
                
    except IOError:
        return 'Файл не найден.'
    
    TODO: добавить отфильтрованные слова в словарь и к ним значением добавить количество упоминаний в списке words
        
    TODO: отсортировать словарь по значениям по убыванию
    ''' https://pythoner.name/sortdict - сортировка по значениям '''
        
    return 'Типа топ100 слов'

if __name__ == '__main__':
    from nltk.corpus import stopwords
    
    print(top100_word_counter(file_path))    
