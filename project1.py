
"""
TAS Cafe Ordering System

Author: Tasneem Mohammed
Purpose:A cafe menu where the user would go to order from
 a set of menu items I have given and it's prices, where in 
 the end it shows their total and what they ordered and customized (like a receipt)


Date: September 22, 2026
"""



menu = {
    "Iced Vanilla Latte": 5.50,
    "Caramel Macchiato": 5.50,
    "Matcha Latte": 5.25,
    "Strawberry Matcha Latte": 5.50,
}


sizes = ("Small", "Medium-$0.25", "Large-$0.50")
milk_choice= ("Whole", "Oat", "Almond")
temp = ("Hot","Iced")


order = []


def display_menu():
    print("\n========== TAS CAFE ==========")

    number = 1

    for item, price in menu.items():
        print(f"{number}. {item} - ${price:.2f}")
        number += 1

    print("0. Finish Order")
    print("==============================")


def choose_drink():
    menu_items = list(menu.keys())

    while True:
        display_menu()

        choice = input("What would you like to order? ")

        if choice == "0":
            return None

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(menu_items):
                return menu_items[choice_number - 1]

        print("Invalid choice. Please choose a number from the menu.")


def choose_size():
    
    while True:
        print("\nChoose your size:")

        for number, size in enumerate(sizes, start=1):
            print(f"{number}. {size}")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(sizes):
                return sizes[choice_number - 1]

        print("Invalid choice. Please try again.")


def choose_milk():
    while True:
        print("\nChoose your milk:")

        for number, milk in enumerate(milk_choice, start=1):
            print(f"{number}. {milk}")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(milk_choice):
                return milk_choice[choice_number - 1]

        print("Invalid choice. Please try again.")

def choose_temp():
    while True:
        print("\nHot or Iced?:")

        for number, temp_choice in enumerate(temp, start=1):
            print(f"{number}. {temp_choice}")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice_number = int(choice)

            if 1 <= choice_number <= len(temp):
                return temp[choice_number - 1]

        print("Invalid choice. Please try again.")


def add_order():
    
    drink = choose_drink()

    if drink is None:
        return False

    size = choose_size()
    milk = choose_milk()
    temp = choose_temp()

    price = menu[drink]

  
    if "Large-$0.50" in size:
        price += 0.50

    if "Medium-$0.25" in size:
        price += 0.25


    drink_order = {
        "drink": drink,
        "size": size,
        "milk": milk,
        "price": price,
        "temp": temp
    }

    order.append(drink_order)

    print(f"\n{drink} added to your order!")
    return True


def display_receipt():
    
    print("\n\n========== RECEIPT ==========")

    if not order:
        print("You did not order anything.")
        return

    total = 0

    for item in order:
        print(f"\n{item['drink']}")
        print(f"Size: {item['size']}")
        print(f"Milk: {item['milk']}")
        print(f"Temp: {item['temp']}")


        print(f"Price: ${item['price']:.2f}")

        total += item["price"]

   
  

    print("\n------------------------------")
    print(f"Total:    ${total:.2f}")
    print("==============================")
    print("Thank you for ordering from TAS Cafe!")


def main():
    print("Welcome to TAS Cafe!")

    while True:
        added_item = add_order()

        if not added_item:
            break

        another = input("\nWould you like to order another item? (yes/no): ").lower()

        if another == "no":
            break

    display_receipt()


main()

