import random
print("Welcome, to Random Compliment Generator!")
# asks user to type "s" inorder to begin the program.
start = input('To start the program please type "S"')
while True:
    if start.upper() == "S":
        user_name = input("\nHello! What is your name?")
        print(user_name + "! That's a nice name :)")
        break
    if start.upper() != "S":
        # asks the question again if user enters wrong input.
        print('That input is invalid')
        start = input('To start the program please type "S"')


def users_day():
    # asks user how their day is going.
    good_day = input("\nAre you having a good day today?")
    while True:
        # program outputs an answer based on how they respond.
        if good_day.lower() == "yes":
            print("\nThat's very good to hear!")
            break
        if good_day.lower() == "no":
            print("\nOh no, that's not very good")
            break
        if good_day.lower() != "yes" or "no":
            # asks the question again if user enters wrong input.
            print('\nPlease answer with "yes" or "no"')
            good_day = input("\nAre you having a good day today?")


users_day()


def compliment():
    compliment_list = ["You look good today!", "I like your style", "That color is perfect on you",
                       "You have the best laugh!", "You are making a difference",
                       "You're the best!", "You're a great listener!",
                       "You're a great example to others!"]
    while True:
        better_day = input("Can I try make your day a little better?")
        if better_day.lower() == "yes":
            print(random.choice(compliment_list))
