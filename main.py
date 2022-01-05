import sample

name = None
ID = None

print("Welcome!\nType in a command")
command = input("login, logout, new account, buy, logout, history:\n")

while command != "exit":
    if command == "login":
        ID = sample.login(name)
    elif command == "logout":
        print("Goodbye!")
    elif command == "new account":
        sample.new_customer()
    elif command == "buy":
        if ID is None:
            print("You have to login first!")
            ID = sample.login(name)

        amount = int(input("Amount of Items to buy: "))
        sample.new_order(ID, amount)
    elif command == "history":
        sample.history(ID)
