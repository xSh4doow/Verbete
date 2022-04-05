from random import randint
from verbetes import Verbetes as V
from termcolor import colored
from time import sleep


def selecionar_palavra_a():
    n = randint(0, 8)
    global index
    index = (2 * n)
    palavraa = V[index].lower()
    return palavraa


def significado():
    significad = index + 1
    verbete = V[significad]
    return verbete


def config():
    global palavra
    global t
    global tentativa
    palavra = selecionar_palavra_a()
    t = 0
    tentativa = 0
    inicio()

def inicio():
    print("Seja bem-vindo(a) ao Verbete!")
    print("Você receberá um verbete e deverá adivinhar a palavra através dele")
    print(colored(significado(), 'green', attrs=['bold']))
    print("A sua palavra tem: " + str(len(palavra)) + " letras.")

if __name__ == "__main__":
    config()

while tentativa < 6:
    guess = input("").lower()
    t += 1
    tentativa += 1

    for i in range(min(len(guess), 10)):
        try:
            if guess[i] == palavra[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in palavra:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(colored(guess[i], 'red'), end="")
        except IndexError:
            print("\nVocê colocou letra a mais! Não é essa palavra!")


    if guess == palavra:
        print("\n")
        print(colored("Parabéns! Você acertou o seu vocábulo!", 'green'), end="")
        print("\n")
        print(colored(f"Você acertou seu vocábulo em {t} tentativas!", 'red'), end="")
        print("\n")
        sleep(1)
        config()

    elif tentativa >= 6:
        print(colored("\nPuts, não foi dessa vez!"))
        sleep(.5)
        config()










