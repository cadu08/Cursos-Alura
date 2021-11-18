import adivinhacao
import hangman

print('*******************')
print('*Choose your game!*')
print('*******************')

print('(1) Hangman (2) Guessing')

choice = int(input('Type your choice: '))

if choice == 1:
    hangman.play()
elif choice == 2:
    adivinhacao.play()