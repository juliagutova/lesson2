'''
def cut_cake(people):
    try:
        parts = 1 / people
        print(f"Каждый получит {parts} пирога")
    except (ZeroDivisionError, TypeError):
        print("Не могу поделить")
cut_cake('5')
'''
'''
# Как делать не надо
import random

def cut_cake(people):
    try:
        parts = 1 / people
        print(f"Каждый получит {parts} пирога")
    except:
        print("Не могу поделить")


while True:
    p = random.randint(1, 10)
    cut_cake(p)


def hello_user():
    while True:
        try:
            how = input("Как дела? ")
        except(KeyboardInterrupt):
            print("Пока")
            break
    
if __name__ == "__main__":
    hello_user()
'''

def discounted(price, discount, max_discount=50):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99%')
        if discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price - price * discount / 100
        return(price_with_discount)
    except(ValueError, TypeError):
        print("Веденные данные не корректны")

print(discounted(100, 40))
