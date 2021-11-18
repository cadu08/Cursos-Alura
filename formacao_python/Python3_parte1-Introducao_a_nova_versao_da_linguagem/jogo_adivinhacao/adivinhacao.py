import random

def play():
    print("*********************************")
    print("Welcome to the guessing game!")
    print("*********************************")

    secret_number = random.randrange(1,101)  #Generates a random number between 1 and 100
    total_trials = 0
    score = 1000

    print("What difficulty level do you wish?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Type the dificult level: "))

    if level == 1:
        total_trials = 20
    elif level == 2:
        total_trials = 10
    else:
        total_trials = 5

    for round in range(1, total_trials+1):

        print("Trial {} of {}".format(round, total_trials))

        trial_value = int(input("Type a number between 1 and 100: "))

        if trial_value < 1 or trial_value > 100:
            print("You must type a number between 1 and 100!")
            continue

        print("You typed ", trial_value)

        right = trial_value == secret_number
        higher = trial_value > secret_number
        less = trial_value < secret_number

        if right:
            print(f"You got it right! Your score is {score} ")
            break
        elif higher:
            print("You missed. The value of your bet is higher than the secret number!")
        elif less:
            print("You missed. The value of your bet is less than the secret number!")
        lost_score = abs(secret_number - trial_value)
        score = score - lost_score

    print("Game Over")

if __name__ == '__main__':
    play()