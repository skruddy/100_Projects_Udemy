import random

number_to_guess = random.randint(1,101)
was_number_guessed = False
guesses_remaining = 0


def assess_guess(guess):
    global guesses_remaining
    if guess == number_to_guess:
        print("You have successfully guessed the number!")
        return 100
    elif guess < number_to_guess:
        print("You have guessed too low!")
        guesses_remaining -= 1
        if guesses_remaining == 0:
            print(f"You have exhausted all your guesses! Number to guess was: {number_to_guess}")
            return -2
        else:
            print(f"Please take another guess! \t Atempts remaining : {guesses_remaining}")
            return -1
    elif guess > number_to_guess:
        print("You have guessed too high!")
        guesses_remaining -= 1
        if guesses_remaining == 0:
            print(f"You have exhausted all your guesses! Number to guess was: {number_to_guess}")
            return -2
        else:
            print(f"Please take another guess! \t Atempts remaining : {guesses_remaining}")
            return -1


def begin_game():
    global was_number_guessed
    global guesses_remaining
    print("Welcome to number guessing game!")
    mode = input("Please select mode. Enter 'easy' for 10 attempts, Enter 'hard' for 5 attempts \n")
    guesses_remaining = 10 if mode == 'easy' else 5
    print("Please take a guess")

    while not was_number_guessed:
        guess = int(input())
        guess_assessment = assess_guess(guess=guess)
        if guess_assessment == 100:
            was_number_guessed = True
            break
        elif guess_assessment == -2:
            break
        else:
            continue


begin_game()
print("Thank you for playing!")