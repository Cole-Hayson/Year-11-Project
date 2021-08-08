print("Welcome, to Random Compliment Generator!")
start = input('To start the program please type "S"')
while True:
    if start.upper() == "S":
        user_name = input("\nHello! What is your name?")
        print(user_name + "! That's a nice name :)")
        break
    if start.upper() != "S":
        print('That input is invalid')
        start = input('To start the program please type "S"')


def users_day():
    good_day = input("\nAre you having a good day today?")
    while True:
        if good_day.lower() == "yes":
            print("\nThat's very good to hear!")
            break
        if good_day.lower() == "no":
            print("\nOh no, that's not very good")
            break
        if good_day.lower() != "yes" or "no":
            print('\nPlease answer with "yes" or "no"')
            good_day = input("\nAre you having a good day today?")


users_day()
