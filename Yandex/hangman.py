import random
import request


def printtheword(w, gl):  # печатает слово с пропусками в необходимых местах
    amountofletters = 0
    res = ""
    if w[0] in gl:
        res += w[0]
        amountofletters += 1
    else:
        res += "_"
    for i in range(1, len(w)):
        res += " "
        if w[i] in gl:
            res += w[i]
            amountofletters += 1
        else:
            res += "_"
    print(res)
    return amountofletters


def drawthehuman(g):  #  рисует виселицу, g - число неудачных попыток
    s = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    s[0] = "     /"
    s[1] = "     / \\"
    s[2] = "      _\n     / \\"
    s[3] = "     |_\n     / \\"
    s[4] = "     |\n     |_\n     / \\"
    s[5] = "     |\n     |\n     |_\n     / \\"
    s[6] = "    _\n     |\n     |\n     |_\n     / \\"
    s[7] = "   __\n     |\n     |\n     |_\n     / \\"
    s[8] = "   __\n  |  |\n     |\n     |_\n     / \\"
    s[9] = "   __\n  |  |\n  O  |\n     |_\n     / \\"
    s[10] = "   __\n  |  |\n  O  |\n  |  |_\n     / \\"
    s[11] = "   __\n  |  |\n  O  |\n /|  |_\n     / \\"
    s[12] = "   __\n  |  |\n  O  |\n /|\\ |_\n     / \\"
    s[13] = "   __\n  |  |\n  O  |\n /|\\ |_\n /   / \\"
    s[14] = "   __\n  |  |\n  O  |\n /|\\ |_\n / \\ / \\"
    if g > 0:
        print(s[g-1])


"""
   __
  |  |
  O  |
 /|\ |_
 / \ / \
"""


print("Ваша тема - животные")


word = random.choice(thelist)[:-1]
# ugadannye bukvy
guessedletters = []
guesses = 0
print("U vas est 15 popytok chtoby ugadat slovo iz "+str(len(word))+" bukv")
while guesses < 15:
    drawthehuman(guesses)
    aol = printtheword(word, guessedletters)
    if aol == len(word):
        break
    newletter = input("Vvedite bukvu: ")
    print("")
    if newletter.lower() in guessedletters:
        print("Etu bukva uzhe byla nazvana")
    elif len(newletter) == 1 and newletter.isalpha():
        if newletter.lower() in word:
            print("Kruto!")
            guessedletters.append(newletter.lower())
        else:
            print("Nekruto!")
            guesses += 1
    else:
        print("Eto ne bukva")
if newletter.lower() in guessedletters:
    print("")
    print("Wow krasava!")
else:
    drawthehuman(guesses)
    print("Ty proigral haha!")
