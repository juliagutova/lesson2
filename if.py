'''
# Пример работы условного опертора if
balance = 5
price = 10

print(bool(balance < 0 or price > balance))

if balance < 0 or price > balance:
    print("Пожалуйста пополните баланс")

balance = 100

# Условный оператор if и else
balance = 50
price = 10

if balance > price:
    print("Спасибо за покупку")
else:
    print("Пополните баланс")


# If, elif, else
tempriture = 0

if tempriture <= 0:
    print("На улице холодно")
elif 1 <= tempriture <= 15:
    print("На улице прохладно")
elif 16 <= tempriture <= 25:
    print("На улице тепло")
else:
    print("На улице жарко")


# Использование функции

def weather(tempriture):
    if tempriture <= 0:
        return("На улице холодно") #возврат функии
    elif 1 <= tempriture <= 15:
        return("На улице прохладно")
    elif 16 <= tempriture <= 25:
        return("На улице тепло")
    else:
        return("На улице жарко")

print(weather(-2))
print(weather(30))
print(weather(12))


# Формирование более сложных условий
phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
            'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
            'discount': 80}
phone3 = {'name': '', 'stock': 18, 'price': 10000.0,
            'discount': 10}

def discounted(price, discount, max_discount=20, name=' '):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)

apple_disc = discounted(phone1["price"], phone1["discount"], name=phone1["name"])
print(apple_disc)

android_disc = discounted(phone2["price"], phone2["discount"], name=phone2["name"])
print(android_disc)  

noname_disc = discounted(phone3["price"], phone3["discount"], name=phone3["name"])
print(noname_disc)


# Практика возраст
age = int(input("Введите свой возраст: "))
def activity(age):
    if 0 <= age <= 2:
        return("Пользователь еще совсем малыш")
    elif 3 <= age <= 6:
        return("Пользователь посещает детский сад")
    elif 7 <= age <= 18:
        return("Пользователь учиться в школе")
    elif 19 <= age <= 22:
        return("Пользователь учиться в ВУЗе")
    else:
        return("Пользователь работает")
user_age = activity(age)
print(user_age)

'''
# Практика сравнение строк

string1 = str(input("Введите сообщение: "))
string2 = str(input("Введите сообщение: "))

def string_length(string1, string2):
    lenstr1 = len(string1)
    lenstr2 = len(string2)
    if string1 == string2 or string1 < string2:
        return('1')
    elif string1 > string2:
        return('2')
    elif string2 == "learn":
        return('3')
    else:
        return('0')
print(string_length(string1, string2))
