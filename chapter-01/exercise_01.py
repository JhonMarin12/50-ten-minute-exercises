# Number guessing name

from random import randint

def guessing_game():
    "Función que simula un juego de adivinar el numero correcto"
    guess_number = randint(0,100)
    while True:
        answer = int(input("Type a number between 0 and 100: "))
        if guess_number == answer:
            print(f"Just right, the answer is {answer}")
            break
        elif guess_number < answer:
            print("Too high")
        else:
            print("Too low")
    print("Exit program...")

guessing_game()

