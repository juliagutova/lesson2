
for number in range(3):
    print(f"Hello world {number}!")


for letter in "python":
    print(letter.upper())


exsample_string = "Я изучаю язык python"

for word in exsample_string.split():
    print(f"Длиина слова '{word}': {len(word)}.")


students_scores = [1, 21, 19, 6, 5]

print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')

scores_sum = 0
for score in students_scores:
    scores_sum += score
    print(scores_sum)

print(f'Средняя оценка: {scores_sum/len(students_scores)}')

from learning_if import discounted

stock = [
	{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
                'discount': 25},
	{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
                'discount': 10},
	{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

for phone in stock:
    phone['final_price'] = discounted(phone['price'], phone['discount'], name=phone['name'])

print(stock)

# Практика Цикл

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    num +=1
    print(num)


string = input("Введите фразу: ")
for string in string:
    print(string.upper())


