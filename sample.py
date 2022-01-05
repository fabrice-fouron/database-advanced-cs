import json

def expense_all_customers():
    with open("sample.json", "r+") as f:
        file = json.loads(f.read())

    for i in file['customer info']:
        print(i['name'] + ": $" + str(spent_on_product(i['id'])))


def spent_on_product(customerId):
    spent = 0

    with open("sample.json", "r+") as f:
        file = json.loads(f.read())

    for i in file['order info']:
        if customerId == i['customerId']:
            product = i['product']
            for j in file['products']:
                if product == j['name']:
                    spent += i['quantity'] * j['cost']
    return spent


def login(name):
    '''Login process of a user'''
    with open("sample.json", "r") as f:
        temp = json.load(f)

    for i in temp["customer info"]:
        # If the name provided is in already registered
        if name == i["name"]:
            print("You are logged in!")
            return name, i["id"]

    entername = input("Name: ")
    enteraddress = input("Address: ")
    temp["customer info"].append({
        "id": len(temp["customer info"]) + 1,
        "name": entername,
        "address": enteraddress
    })
    with open("sample.json", "w") as f:
        json.dump(temp, f, indent=4, separators=(",", ": "))
    name = entername
    return len(temp["customer info"])


def history(idVar):
    '''Display the history of order of a user'''
    with open("sample.json", "r") as f:
        temp = json.load(f)

    for i in temp["order info"]:
        if i["customerId"] == idVar:
            print(f"Order ID: {i['id']}")
            receipt(i["id"])


def new_order(idvar, amount):
    '''Placing a new order'''
    with open("sample.json", "r") as f:
        temp = json.load(f)

    def new_item():
        """A new item to add to the cart"""
        name = input("Product: ").capitalize()
        quantity = int(input("Quantity: "))
        return name, quantity
    count = 0
    cart = []

    while count < amount:
        cart.append(new_item())
        count += 1

    temp["order info"].append({
        "id": len(temp["order info"]) + 1,
        "product": [i[0] for i in cart],
        "quantity": [i[1] for i in cart],
        "customerId": idvar
    })

    with open("sample.json", "w") as f:
        json.dump(temp, f, indent=4, separators=(",", ": "))

    receipt(len(temp["order info"]))


def new_customer():
    """Create a new account for a user"""
    name = input("Name: ")
    address = input("Address: ")

    with open("sample.json", "r") as f:
       temp = json.load(f)

    temp["customer info"].append({
        "id": len(temp["customer info"]) + 1,
        "name": name,
        "address": address
    })

    with open("sample.json", "w") as f:
        json.dump(temp, f, indent=4, separators=(",", ": "))


def receipt(idVar):
    '''Display a receipt of the order'''
    with open("sample.json", "r") as f:
        temp = json.load(f)

    total = 0
    for i in temp["order info"]:
        if i["id"] == idVar:
            # Multiple Items
            if isinstance(i["product"], list):
                print("Quantity\t Name\t SubTotal($)")
                for a in range(len(i["product"])):
                    total += i["quantity"][a] * find_item(i["product"][a])

                    print(i["quantity"][a], "\t\t\t", i["product"][a], "\t", i["quantity"][a] * find_item(i["product"][a]))
                print("-----------------------------\n")

            # Single Item
            else:
                total += i["quantity"] * find_item(i["product"])
                print("Quantity\t Name\t SubTotal($)")
                print(i["quantity"],"\t\t\t", i["product"], "\t", total)
                print("-----------------------------\n")
    print("Total: ", total)


def find_item(item):
    with open("sample.json", "r") as f:
        temp = json.load(f)

    for i in temp["products"]:
        if i["name"] == item:
            return i["cost"]


def delete_account(name):
    '''Delete all data related to this account'''
    with open("sample.json", "r") as f:
        temp = json.load(f)

    idvar = None

    # Remove any customer info about this account
    for i in temp["customer info"]:
        if i["name"] == name:
            idvar = i["id"]
            temp["customer info"].remove(i)
    # Remove any order info about this account
    for a in temp["order info"]:
        if a["customerId"] == idvar:
            temp["order info"].remove(a)

    with open("sample.json", "w") as f:
        json.dump(temp, f, separators=[", ", ": "], indent=4)
