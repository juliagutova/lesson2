'''
while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print('Сам ты {}'.format(user_say))
'''
'''
names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
while True:
    names == 'Валера'
    name = names.pop(3)
    print(f'{name} нашелся!')
    break

def find_person(name):
    names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
    while True:
        name = names.pop(3)
        print(f'{name} нашелся!')
        break

find_person(name="Валера")
'''
'''
def ask_user():
    while True:
        ask = input("Как дела?")
        if ask == "Хорошо":
            break
ask_user()
'''
def ask_user():
    while True:
        ask = input("Как дела?")
        
    def get_answer(ask):
        while True:
            answer = input(" ")
            if answer == "Пока":
                break
ask_user()