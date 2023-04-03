menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

order = {}

count =0
def print_menu():
    print("*******************************")
    print("    Welcome to the Snakes Cafe!   ")
    print("    Please see our menu below.    ")
    print("                                  ")
    print(" To quit at any time, type 'quit' ")
    print("*********************************")

    for category, items in menu.items():
        print("\n"+category)
        print("------")
        for item in items:
            print(item)

    print("\n" + "*" *20 )
    print(" What would you like to order? ")
    print("*" * 20)

def take_order():
    while True:
        item = input("> ")
        if item.lower() == "quit":
            break
        elif item in order:
            order[item] += 1
        elif item in [item for items in menu.values() for item in items]:
            order[item] = 1
        else:
            print("Sorry, that item is not on the menu.")
        print(f" {order[item]} order(s) of {item} have been added to your meal ")
        print_order()

def print_order():
    if order:
        print("\n" + "-" * 35)
        print("Here is a summary of your order:")
        for item, quantity in order.items():
            print(f"{quantity} order(s) of {item}")
    else:
        print("Your order is empty.")

print_menu()
take_order()