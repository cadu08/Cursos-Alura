import random


def play():

    print_welcome_message()

    secret_word = get_secret_word()

    guesses_letters = initialize_guesses_letters(secret_word)

    hanged = False
    got_right = False
    mistakes = 0

    while not hanged and not got_right:

        trial = ask_guess_trial()

        if trial in secret_word:
            guesses_letters = mark_right_attempt(secret_word, guesses_letters, trial)
        else:
            mistakes += 1
            drawing_gallow(mistakes)

        hanged = mistakes == 7
        got_right = "_" not in guesses_letters
        print(guesses_letters)

    if got_right:
        print_winner_message()
    else:
        print_looser_message(secret_word)


def print_winner_message():
    print("Congrats, you win!")
    print("  ___________   ")
    print(" '._==_==_=_.'  ")
    print(" .-\\:      /-. ")
    print("| (|:.     |) | ")
    print(" '-|:.     |-'  ")
    print("   \\::.    /   ")
    print("    '::. .'     ")
    print("      ) (       ")
    print("    _.' '._     ")
    print("   '-------'    ")


def print_looser_message(secret_word):
    print("You were hanged, what a pity!")
    print("The secret word was {}".format(secret_word))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")


def drawing_gallow(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if mistakes == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if mistakes == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if mistakes == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if mistakes == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if mistakes == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if mistakes == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if mistakes == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def print_welcome_message():
    print('*********************************')
    print('***Welcome to the hangman game***')
    print('*********************************')


def get_secret_word():
    words = []

    with open("words.txt") as file:
        for line in file:
            words.append(line.strip())

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def initialize_guesses_letters(secret_word):
    return ["_" for letter in secret_word]


def ask_guess_trial():
    trial = input(
        "Type a letter: ").strip().upper()  # remove all blank spaces and change the letter to the upper case
    return trial


def mark_right_attempt(secret_word, guesses_letters, trial):
    index = 0
    for letter in secret_word:
        if trial == letter:
            guesses_letters[index] = letter.upper()
        index += 1
    return guesses_letters


if __name__ == '__main__':
    play()