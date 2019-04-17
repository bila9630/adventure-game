import time
import random


human_you_meet_at_McDonald = ["cashier", "pirate", "elve", "dinosaur"]

food = ["McDonald Menu", "ice cream", "chicken nugget", "salat"]

template_for_food = ["You ordered {{food}}",
                     "You screamed {{food}}",
                     "You whisper {{food}}"]


# This will define what you will order at McDonald
def random_sentence_in_McDonald(food, template_for_food):
    template = random.choice(template_for_food)
    output = []
    index = 0

    while index < len(template):
        if template[index:index+8] == "{{food}}":
            output.append(random.choice(food))
            index += 8
        else:
            output.append(template[index])
            index += 1

    output = "".join(output)
    return output


# This will define who you meet at Mcdonald
def random_person_in_McDonald(human_you_meet_at_McDonald):
    sentence = "You go to the {{person}}, one of the McDonalds staff"
    output = []
    index = 0

    while index < len(sentence):
        if sentence[index:index+10] == "{{person}}":
            output.append(random.choice(human_you_meet_at_McDonald))
            index += 10
        else:
            output.append(sentence[index])
            index += 1

    output = "".join(output)
    return output


# It is just a normal print method but with
# the exception that it will pause for 2 sec before it continues
def print_pause(words_you_want_to_print):
    print(words_you_want_to_print)
    time.sleep(2)


# Here is the intro at the start of the game.
def intro():
    print_pause("You find yourself in a city corner in New York")
    print_pause("In front of you are two passageways")


# checking the input of the player.
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


# The bank, one of two places where the player can go
def bank(items):
    print_pause("You are now in the bank")
    # if the player already has the money, they player will return to the city
    if "money" in items:
        print_pause("You already have the money\n"
                    "There is nothing more to do here!")
        print_pause("You go out of the bank")
        city(items)
    # If the player dont have the money, he will get it here
    else:
        print_pause("You go to the bank machine and withdraw 15€")
        items.append("money")
        print_pause("Now you feel like a rich man!")
        print_pause("You go out of the bank")
        city(items)


# the end where the player can choose if they want to play the game again.
def the_end():
    play_again = valid_input("Do you want to play again?y/n \n", "y", "n")
    if "y" in play_again:
        the_game_begins()
    elif "n" in play_again:
        print_pause("Thanks for playing the game!")


# the restaurant
def McDonald(items):
    print_pause(
        "You are now in McDonald, one of the happiest place in the world")
    print_pause(random_person_in_McDonald(human_you_meet_at_McDonald))
    print_pause(random_sentence_in_McDonald(food, template_for_food))
    print_pause("Then you need to pay")
    if "money" in items:
        print_pause(
            "Luckily you just withdrawed some money and you can pay your meal")
        print_pause("You won the game")
        the_end()
    # The player decides what to do after
    # they found out that they dont have the money
    else:
        Donald_decision = valid_input(
            "You didn't have any money with you. Now you have two options\n"
            "1. run out of the restaurant\n"
            "2. threat the cashier with a bad rating?",
            "1", "2")
        if Donald_decision == "1":
            print_pause("You panic and run out of the restaurant.")
            city(items)
        elif Donald_decision == "2":
            print_pause(
                "You threated the cashier."
                " Unfortunately the cashier is an underground police")
            print_pause("He arrested you.")
            print_pause("You lose the game")
            the_end()


# The place where the player can choose if they want to McDonald or the bank
def city(items):
    response = valid_input("You are in the city\n"
                           "Please choose your path!\n"
                           "Would you like to go to the bank or McDonald?\n",
                           "bank", "mcdonald")
    if "bank" in response:
        print_pause("You go to the bank!")
        bank(items)
    elif "mcdonald" in response:
        print_pause("Good choice! You go to the McDonald")
        McDonald(items)


# Here is the game. When you call it, the game will start
def the_game_begins():
    items = []
    intro()
    city(items)


the_game_begins()
