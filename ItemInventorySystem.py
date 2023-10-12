inventory = {
    'Bacon': {'price': 1.99, 'stock': 10},
    'Sausages': {'price': 0.99, 'stock': 15},
    'Panini': {'price': 2.49, 'stock': 5},
    'croissants' : {'price': 6.49, 'stock': 20},
    'maple pecan': {'price': 5.49, 'stock': 105},}


def display_inventory():
    for item, details in inventory.items():
        print(item + ': $' + str(details['price']) + ' (' + str(details['stock']) + ' left)')


def purchase_item(item, quantity):
    if item in inventory and inventory[item]['stock'] >= quantity:
        inventory[item]['stock'] -= quantity
        print(f"{quantity} {item} purchased")
    else:
        print(f"Cannot purchase {quantity} {item}. Stock too low.")


def add_new_item(item, price, stock):
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    inventory[item] = {'price': price, 'stock': stock}


def update_price(item, price):
    if item in inventory:
        inventory[item]['price'] = price
    else:
        print(f"{item} not found in inventory.")


def delete_item(item):
    if item in inventory:
        del inventory[item]
    else:
        print(f"{item} not found in inventory.")


# Interact with the inventory
#display_inventory()
#purchase_item('Bacon', 5)
#add_new_item('Sourdough', 3.49, 15)
#update_price('Sausages', 2.99)
#delete_item('Panini')

display_inventory()


while True:

    print()
    print("Inventory Managment")
    print("1. Display Inventory")
    print("2. Purchase Item")
    print("3. Add New Item")
    print("4. Update Price")
    print("5. Delete Item")
    print("0. Quit")

    choice = input("Enter choice: ")

    if choice == '1':
        display_inventory()

    elif choice == '2':
        item = input("Enter Item: ")
        quantity = int(input("Enter Quantity: "))

    elif choice == '3':
        item = input("Enter Item Name: ")
        Price = float(input("Enter Price: "))
        add_new_item(item, price, stock)

    elif choice == '4':
        item = input("Enter Item: ")
        quantity = int(input("Enter New Price: "))
        update_price(item, price)

    elif choice == '5':
        item = input("Enter Item to Delete: ")
        delete_item(item)

    elif choice == '0':
        break


    else:
        print("Invalid Choice")

print("Goodbye")
exit(1)


