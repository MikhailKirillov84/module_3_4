
#1. Объявить функцию single_root_words и написать в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_words):
    #2. Создать внутри функции пустой список([]) same_words, который пополнится нужными словами.
    same_words = []    #новый список
    #3. При помощи цикла for переберите предполагаемо подходящие слова.
    for i in other_words:  #переборка для(for) переменной "i" внутри переменной *other_worlds.
        #4. Условие при котором добавляются слова в результирующий список same_words[], не учитывая регистр символов.
        if root_word.lower().count(i.lower()) or i.lower().count(root_word.lower()):
            # count() - метод позволяет подсчитывать количество вхождений заданной подстроки в строку.
            # lower() - метод преобразует все символы верхнего регистра в строчные буквы.
            same_words.append(i)   # append() - метод позволяют добавить новый элемент в уже существующий список
            #5. Вернуть образованный функцией список same_words.
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
