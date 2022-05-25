# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
vowels = 'аоеиыуюэёя'
count_vowels = 0
for leter in word:
    if leter in vowels:
        count_vowels += 1
print(count_vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word_count = sentence.count(' ') + 1
print(word_count)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list = []
sentence_list = sentence.split()
for first_ch in sentence_list:
    print(first_ch[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

sentence_list = []
sentence_list = sentence.split()
sentence_with_out_space = ''.join(sentence_list)
length_sentence = len(sentence_with_out_space)
length_sentence_list = len(sentence_list)
average_length_word = length_sentence // length_sentence_list

print(average_length_word)