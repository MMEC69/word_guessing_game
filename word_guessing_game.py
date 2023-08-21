#didnt work as intended
import random

print("=====================Word Guessing Game=====================")

#now give your name
user_name = input("What is your name? ")

print("Good Luck {}!".format(user_name))

words = ["nuke", "computer", "python", "cobra", "television", "minecraft", "github"]

random_word = random.choice(words)
#print(random_word)

chances = 12
print("=====================Now the game begins=====================")
print("Start guessing.")


#guessed_word = ""
guesses = ""

while chances > 0:
    failed_times = 0

    for char in random_word:
        if char in guesses:
            print(char, end = "")
        else:
            print(" _ ", end = "")
            failed_times +=1

    print()

    if failed_times == 0:
        print("Your answer is correct, Congrats!!\nThe answer is {}".format(random_word))
        break

    guessed_word = input("Guess the word: ")

    guesses += guessed_word

    if guesses not in random_word:
        chances -=1
        print("Wrong, try again.\nYou have {} chances left".format(chances))

        if chances == 0:
            print("You have failed, better luck next time!")
            break








