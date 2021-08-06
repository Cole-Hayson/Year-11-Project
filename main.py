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
