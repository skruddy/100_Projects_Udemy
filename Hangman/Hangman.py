import random

from Hangman_Art import *
from Hangman_Words import *

def get_character_index_mapping(string_to_break):
    character_index_mapping = {}
    for character in string_to_break:
        if character_index_mapping.keys().__contains__(character):
            number_of_occurence = character_index_mapping.get(character)+1
            character_index_mapping[character] = number_of_occurence
        else:
            character_index_mapping.setdefault(character, 1)
    return character_index_mapping;


def generate_blank_string(string_to_mask):
    masked_string = ""
    for character in range(len(string_to_mask)):
        masked_string += "_"
    return masked_string

def is_character_present(character, random_string):
    if random_string.__contains__(character.lower()) or random_string.__contains__(character.capitalize()):
        return True
    else:
        return False

def get_index_for_character(character, random_string):
    index_list = []
    for i in range(0, len(random_string)):
       if random_string[i] == character:
            index_list.append(i)
    return index_list


def replace_blank_string_with_characters(character, blank_string, random_string):
    indices_of_character = get_index_for_character(character, random_string)
    array_blank_string = list(blank_string)
    for i in indices_of_character:
        array_blank_string[i] = character
    return "".join(array_blank_string)

def guessed_entire_string(blank_string):
    if blank_string.count("_") == 0:
        return True
    else:
        return False

def ask_user_for_input():
    input_character = input("Please make a guess!")
    if len(input_character) > 1 or len(input_character) == 0:
        print("You are only allowed to guess 1 character at a time, no less and no more! \nPlease take a fresh guess")
        return ""
    else:
        return input_character

def get_random_word():
    return random.choice(word_list)

def start_game():
    random_string = get_random_word()
    blank_string = generate_blank_string(random_string)
    guessed_entire_word = False;
    remaining_chances = len(stages)
    guesses = []
    print(f"{logo}")

    while guessed_entire_word == False and remaining_chances > 0:
        print(f"\n")
        guessed_character = ask_user_for_input()
        if guessed_character in guesses:
            print("You have already taken that guess, take a fresh one!")
            continue
        else:
            guesses.append(guessed_character)
            if len(guessed_character) >0:
                if is_character_present(guessed_character, random_string):
                    print("Successful guess!, keep going")
                    blank_string = replace_blank_string_with_characters(guessed_character, blank_string, random_string)
                    guessed_entire_word = guessed_entire_string(blank_string)
                    print(f"Current status of guessed string: {blank_string}")
                else:
                    remaining_chances -= 1
                    print(f"Wrong guess, try again!")
                    print(stages[remaining_chances])
                    print(f"Current status of guessed string: {blank_string}")
            else:
                remaining_chances -= 1
                print(stages[remaining_chances])
                print(f"Current status of guessed string: {blank_string}")

    if guessed_entire_word == True:
        print("Congratulations!, you have successfully guessed the entire word!")
    else:
        print("You have consumed all the lives and HAVE KILLED HANGMAN!!")
        print(f"The word to guess was: {random_string}")

start_game()