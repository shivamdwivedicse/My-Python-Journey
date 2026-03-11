import random

def guess_game():
    number = random.randint(1, 20)
    print("🎲 Guess the number between 1 and 20!")

    while True:
        guess = int(input("Your guess: "))
        if guess == number:
            print("🔥 Wah bhai! Sahi pakde hai 😎")
            break
        elif guess < number:
            print("Too low... Upar jaa thoda! ⬆️")
        else:
            print("Zyada ho gaya! Neeche jaa! ⬇️")

guess_game()
