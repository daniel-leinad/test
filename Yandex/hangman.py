import random
import requests


def printtheword(w, gl):  # печатает слово с пропусками в необходимых местах
    amountofletters = 0
    res = ''
    if w[0] in gl:
        res += w[0]
        amountofletters += 1
    else:
        res += '_'
    for i in range(1, len(w)):
        res += ' '
        if w[i] in gl:
            res += w[i]
            amountofletters += 1
        else:
            res += '_'
    print(res)
    return amountofletters  # возвращает количество угаданных букв в слове


def drawthehuman(g):  #  рисует виселицу, g - число неудачных попыток
    s = []
    s.append('     /')
    s.append('     / \\')
    s.append('      _\n     / \\')
    s.append('     |_\n     / \\')
    s.append('     |\n     |_\n     / \\')
    s.append('     |\n     |\n     |_\n     / \\')
    s.append('    _\n     |\n     |\n     |_\n     / \\')
    s.append('   __\n     |\n     |\n     |_\n     / \\')
    s.append('   __\n  |  |\n     |\n     |_\n     / \\')
    s.append('   __\n  |  |\n  O  |\n     |_\n     / \\')
    s.append('   __\n  |  |\n  O  |\n  |  |_\n     / \\')
    s.append('   __\n  |  |\n  O  |\n /|  |_\n     / \\')
    s.append('   __\n  |  |\n  O  |\n /|\\ |_\n     / \\')
    s.append('   __\n  |  |\n  O  |\n /|\\ |_\n /   / \\')
    s.append('   __\n  |  |\n  O  |\n /|\\ |_\n / \\ / \\')
    if g > 0:
        print(s[g-1])
    print()  # для красоты


'''
   __
  |  |
  O  |
 /|\ |_
 / \ / \
'''


animals = requests.get('https://raw.githubusercontent.com/guitrst/test/master/Yandex/animals.txt').content.decode('utf-8')
thelist = animals.split('\n')[:-1]  # список слов, последний элемент - всегда пустая строка
guessedletters = []  # угаданные буквы
unguessedletters = []  # неугаданные буквы
word = random.choice(thelist)  # слово, которое будет угадываться
guesses = 0  # неудачные попытки


print('Ваша тема - животные')
print('У вас есть 15 попыток, чтобы угадать слово из '+str(len(word))+' букв')
while guesses < 15:
    print()  # для красоты
    newletter = input('Введите букву: ')
    if newletter.lower() in guessedletters or newletter.lower() in unguessedletters:
        print('Эта буква уже была названа')
        continue
    elif len(newletter) == 1 and newletter.isalpha():
        if newletter.lower() in word:  # случай если пользователь угадал букву
            print('Да!')
            guessedletters.append(newletter.lower())
        else:  # случай если пользователь не угадал букву
            print('Нет.')
            unguessedletters.append(newletter.lower())
            guesses += 1  # увеличиваем число неудачных попыток
    else:
        print('Это не буква')
        continue
    drawthehuman(guesses)  # рисуем виселицу
    aol = printtheword(word, guessedletters)  # aol - количество угаданных букв в слове
    if aol == len(word):
        break  # цикл кончается в случае выигрыша


if newletter.lower() in guessedletters:
    print('Победа!')
else:
    drawthehuman(guesses)
    print('Проигрыш.')
