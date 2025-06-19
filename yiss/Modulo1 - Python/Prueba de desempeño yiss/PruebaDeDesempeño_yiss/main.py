from source import *

print(""" 
      ✨ Welcome to Makeup By Rose ✨
Inventory System

Inventory cannot contain fewer than 10 products. We'll add some products to the inventory next.
With product name, value, and quantity.
      """)

inventory = {}  # Debería ser un diccionario, no una lista

option_switch = True  # Corregido el nombre de la variable (antes era election_switch)

try:
    quantity_product = int(input("Enter the number of products to add: "))
    if quantity_product < 10:
        print("Warning: Inventory should contain at least 10 products. Adding 10 by default.")
        quantity_product = 10
        
    for i in range(1, quantity_product + 1):
        product = input(f"Enter the name of product {i}: ").title()
        while not product.replace(" ", "").isalpha():
            print("Product name can only contain letters and spaces.")
            product = input(f"Enter the name of product {i}: ").title()
            
        price = float(input("Enter the product price to add: $"))
        while price <= 0:
            print("Price must be a positive value")
            price = float(input("Enter the product price to add: $"))
            
        quantity = int(input("Enter the quantity of products to inventory: "))
        while quantity <= 0:
            print("Quantity must be a positive value")
            quantity = int(input("Enter the quantity of products to inventory: "))
            
        inventory[product] = {'price': price, 'quantity': quantity}
        
except ValueError:
    print("Invalid character.")

while option_switch:
    print("""\nWhat you will do today:
1. Add products to inventory.
2. Check availability and prices of existing products in inventory.
3. Update the price of a product in inventory.
4. Delete products.
5. Calculate the total value of the products in inventory.
6. Display inventory.
7. Exit.

Reminder: There are two ways to select an option:
1. By number ("1" to add products, "3" to update a price, etc.)
2. By keyword ("Add," "Delete," etc.)
      """)
    
    option = input("\nSelect an option:👉 ").lower()
    
    if option == "add" or option == "1":
        name_product = input("Enter the name of the product to add:👉 ").title()
        if not name_product.replace(" ", "").isalpha():
            print("❌ The product name can only contain letters and spaces.❌")
        else:
            try:
                price = float(input("Enter the price:👉 $"))
                quantity = int(input("Enter the amount:👉 "))
                if price <= 0 or quantity <= 0:
                    print("Price and quantity must be positive❗")
                else:
                    add_product(inventory, name_product, price, quantity)
            except ValueError:
                print("❌Invalid character, please try again❌")
            
    elif option == "search" or option == "2":
        name_product = input("Enter the name of the product you want to check in the inventory:👉 ").title()
        product = search_product(inventory, name_product)
        if product:
            print(f"\nProduct found🥳: {name_product} - Price: ${product['price']:.2f}, Quantity: {product['quantity']}")
        else:
            print("Product not found in inventory.")
            
    elif option == "update" or option == "3":
        name_product = input("Enter the product name to update its price:👉 ").title()
        if not name_product.replace(" ", "").isalpha():
            print("❌ The product name can only contain letters and spaces.❌")
        else:
            try:
                update_price = float(input("Enter the new price:👉 $"))
                if update_price <= 0:
                    print("\nTo update the product price, it must be positive❗")
                else:
                    update_product(inventory, name_product, update_price)
            except ValueError:
                print("❌The entered price is invalid❌")
            
    elif option == "delete" or option == "4":
        name_product = input("Enter the name of the product you want to delete from inventory:👉 ").title()
        delete_product(inventory, name_product)
        
    elif option == "calculate" or option == "5": 
        calculate_stock(inventory)
        
    elif option == "display" or option == "6":
        print("\n✨ Current Inventory ✨")
        for name_product, product in inventory.items():
            print(f"Product: {name_product} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}") 
    
    elif option == "exit" or option == "7":
        print("\n✨It was a pleasure to assist you, come back soon🥳✨!")
        option_switch = False
        
    else:
        print("\n❌ Invalid option, please try again ❌")