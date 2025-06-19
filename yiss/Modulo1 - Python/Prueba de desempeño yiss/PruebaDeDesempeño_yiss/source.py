#In this code you find the sources used for the operation of the program.

# This module contains all the inventory management functions for the Makeup By Rose system

def inventorys():
    """
    Initialize and return the default inventory dictionary
    Returns:
        dict: Dictionary containing products with their prices and quantities
    """
    return {
        "Agua De Rosas": {"price": 10.600, "quantity": 15},
        "Poms Desmaquillantes": {"price": 3.000, "quantity": 10},
        "Pestañina Prosa Tapa Fucsia": {"price": 15.500, "quantity": 20},
        "Fijador Fix": {"price": 20.000, "quantity": 7},
        "Balaca Pompompurin": {"price": 9.700, "quantity": 15}
    }

def add_product(inventory, product, price, quantity):
    """
    Add a new product to the inventory
    Args:
        inventory (dict): Current inventory dictionary
        product (str): Name of product to add
        price (float): Price of the product
        quantity (int): Quantity in stock
    """
    # Convert product name to title case (first letter of each word capitalized)
    product = product.title()
    
    # Check if product already exists
    if product in inventory:
        print(f"\nThe product {product} already exists in inventory. 😪")
    else:
        # Add new product to inventory
        inventory[product] = {"price": price, "quantity": quantity}
        print(f"\n✨The product {product} was successfully added to inventory🥳✨")

def search_product(inventory, product):
    """
    Search for a product in inventory
    Args:
        inventory (dict): Current inventory dictionary
        product (str): Name of product to search for
    Returns:
        dict/None: Product info if found, None if not found
    """
    # Convert product name to title case
    product = product.title()
    
    # Return product if found, otherwise show message
    if product in inventory:
        return inventory[product]
    print("\n😓 Product not available in inventory. 😓")
    return None

def update_product(inventory, product, price_updated):
    """
    Update the price of an existing product
    Args:
        inventory (dict): Current inventory dictionary
        product (str): Name of product to update
        price_updated (float): New price for the product
    """
    # Convert product name to title case
    product = product.title()
    
    if product in inventory:
        # Update the price
        inventory[product]["price"] = price_updated
        print(f"\n✨ The price of {product} was successfully updated 🥳, and its new price is ${price_updated:.2f}.✨")
    else:
        print(f"\n😓 The product {product} is not available in inventory. 😓")

def delete_product(inventory, product):
    """
    Remove a product from inventory
    Args:
        inventory (dict): Current inventory dictionary
        product (str): Name of product to remove
    """
    # Convert product name to title case
    product = product.title()
    
    if product in inventory:
        # Delete the product
        del inventory[product]
        print(f"\n✨ The product {product} was successfully deleted. 🥳✨")
    else:
        print(f"\n😓 The product {product} is not available in inventory. 😓")

def calculate_stock(inventory):
    """
    Calculate the total value of all inventory
    Args:
        inventory (dict): Current inventory dictionary
    Returns:
        float: Total value of all inventory
    """
    # Calculate sum of (price * quantity) for all products
    total_inventory = sum(item['price'] * item['quantity'] for item in inventory.values())
    print(f"\n✨ The total value of the inventory is: ${total_inventory:.2f}. ✨")
    return total_inventory

def validation_name(product):
    """
    Validate that product name contains only letters and spaces
    Args:
        product (str): Product name to validate
    Returns:
        bool: True if valid, False if invalid
    """
    # Check if product contains only letters and spaces
    if not product.replace(" ", "").isalpha():
        print("\n❌ The product name can only contain letters and spaces.❌")
        return False
    return True