# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0                       # в эту переменную будут прибавляться все гласные
vowels = set("аяоёуюыиэе")      # функция set разбивает строку на символы и формирует множество
for letter in word.lower():     # в цикле проверяем каждую букву(приведя ее к строчной)б есть ли она во множестве
    if letter in vowels:        # если есть то к переменной count прибавляем 1. и так далее для каждой гласной
        count += 1
print(f"Количество гласных букв в слове: {count}.")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' '))) # split() разбивает слова на список, len подсчитывает элементы(в нашем случае слова) в списке


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence = sentence.lower().split(' ') 
for words in sentence:
    print(words[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
list_sent = sentence.split(' ')
len_sent = len(list_sent)
fw = len(list_sent[0])
sw = len(list_sent[1])
fw = len(list_sent[2])
fow = len(list_sent[3])
all_words = (fw + sw + fw + fow) / len_sent
print(all_words)

