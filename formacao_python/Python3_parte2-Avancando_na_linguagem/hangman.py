def play():
    print ('***************************')
    print ('Welcome to the hangman game')
    print ('***************************')

    secret_word = 'banana'
    guesses_letters = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    got_right = False

    while(not hanged and not got_right):

        trial = input("Type a letter: ").strip() #remove all blank spaces

        index = 0
        for letter in secret_word:
            if trial.upper() == letter.upper():
                print("The letter {} was found at index {}.".format(letter, index))
                guesses_letters[index] = letter.upper()
            index = index + 1

        print('hangman')
        print(guesses_letters)

    print('Game over')

if __name__ == '__main__':
    play()