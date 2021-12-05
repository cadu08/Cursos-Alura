def play():
    print ('***************************')
    print ('Welcome to the hangman game')
    print ('***************************')

    secret_word = 'banana'.upper()
    guesses_letters = ["_" for letter in secret_word]

    hanged = False
    got_right = False
    mistakes = 0

    while(not hanged and not got_right):

        trial = input("Type a letter: ").strip().upper() #remove all blank spaces and change the letter to the upper case

        if trial in secret_word:
            index = 0
            for letter in secret_word:
                if trial == letter:
                    print("The letter {} was found at index {}.".format(letter, index))
                    guesses_letters[index] = letter.upper()
                index += 1
        else:
            mistakes += 1
            print("The letter you tipped is not on the word.")
            print("You have {} trials yet.".format(len(secret_word) - mistakes))

        hanged = mistakes == 6
        got_right = "_" not in guesses_letters
        print(guesses_letters)

    if got_right:
        print("You win!")
    else:
        print('Game over')

if __name__ == '__main__':
    play()