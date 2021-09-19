import random

# functions


def users_day():
    # asks user how their day is going.
    good_day = input("\nAre you having a good day today?")
    while True:
        # program outputs an answer based on how they respond.
        if good_day.lower().strip() == "yes":
            print("\nThat's very good to hear!")
            break
        if good_day.lower().strip() == "no":
            print("\nOh no, that's not very good")
            break
        if good_day.lower().strip() != "yes" or "no":
            # asks the question again if user enters wrong input.
            print('\nPlease answer with "yes" or "no"')
            good_day = input("\nAre you having a good day today?")


def compliment():
    # list of random compliments program will select from
    compliment_list = ["You look good today!", "I like your style.", "That colour is perfect on you.",
                       "You have the best laugh!", "You are making a difference.",
                       "You're the best!", "You're a great listener!", "Your positivity is infectious.",
                       "You're a great example to others!", "You're an incredible friend!"]
    while True:
        # asking user if they would like a compliment
        better_day = input("\nWould you like a random compliment to make your day a little better?\n")
        if better_day.lower().strip() == "yes":
            # if user answers yes program generates a random compliment
            print(random.choice(compliment_list))
            while True:
                # asks user if they would like another compliment
                more_compliments = input("\nWould you like another random compliment\n")
                if more_compliments.lower().strip() == "yes":
                    print(random.choice(compliment_list))
                elif more_compliments.lower().strip() == "no":
                    # if user answers no ends program
                    print("\nOkay, Goodbye! :)")
                    print("\nEnding Program...")
                    break
                else:  # more_compliments.lower() != "yes" or more_compliments.lower() != "no":
                    print('\nPlease answer with "yes" or "no"')
                    # more_compliments = input("\nWould you like another compliment")
            break
        if better_day.lower().strip() == "no":
            # if user answers no program ends
            print("\nOkay, that's alright, Have a good day!")
            print("\nEnding Program...")
            break
        # if better_day.lower().strip() != "yes" or "no":
        else:
            # tells user to input the correct input
            print('\nPlease answer "yes" or "no"')
            # better_day = input("\nWould you like a compliment to make your day a little better?\n")


# code

print("Welcome, to Random Compliment Generator!")
# asks user to type "s" inorder to begin the program.
start = input('To start the program please type "S"')
while True:
    if start.upper().strip() == "S":
        user_name = input("\nHello! What is your name?")
        print(user_name + "! That's a nice name :)")
        break
    if start.upper().strip() != "S":
        # asks the question again if user enters wrong input.
        print('That input is invalid')
        start = input('To start the program please type "S"')

# put functions into code
users_day()
compliment()
