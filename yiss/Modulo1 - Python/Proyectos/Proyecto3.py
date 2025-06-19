#INVENTARIO
#Cada producto debe estar definido por su nombre, precio y cantidad disponible (debe poder crecer dinámicamente.)
#Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible, si no está disponible se debe notificar. 
#Permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario.
#Permitir al usuario eliminar productos del inventario de manera segura.
#Debe calcular el valor total de los productos en inventario y mostrarlo al usuario (recomendación: usar lambda). 

#Damos la bienvenida al inventario
print("\n 🧾 Bienvenid@s a su sistema de inventario 🧾")

inventory = {
    "Agua": {"precio": 2.600, "cantidad": 20},
    "Margaritas Flaming hot": {"precio": 4.000, "cantidad": 10},
    "Leche entera": {"precio": 5.500, "cantidad": 20},
    "Leche semidescremada": {"precio": 7.300, "cantidad": 5},
    "Aceite de girasol": {"precio": 6.000, "cantidad": 7},
    "Galletas Chokis": {"precio": 2.400, "cantidad": 15},
    "Chicles Trident Sandia": {"precio": 3.200, "cantidad": 12},
    "Yogurt Coolechera": {"precio": 8.000, "cantidad": 8},
    "Maní Manimoto": {"precio": 1.500, "cantidad": 9},
    "Toallas nosotras Buenas noches": {"precio": 2.300, "cantidad": 7},
    "Papel higiénico familiar": {"precio": 3.000, "cantidad": 8},
    "Suntea Frutos rojos": {"precio": 1.400, "cantidad": 6}
}

#Función para agregar un producto al inventario
def add_products(name,price,quantity):
    name  = name.lower()
    if name in inventory:
        print(f"\nEl producto {name} ya existe en el inventario.")
    else:
        inventory[name] = {"precio": price, "cantidad": quantity}
        print(f"\nEl producto {name} fue agregado con éxito al inventario. 😄")
    
#Función para buscar un producto en el inventario
def search_product(name):
    name = name.lower() #.lower() se usa para que tome name en minusculas
    if name in inventory:
        return inventory[name]
    else:
        print("\nProducto no disponible en inventario❗")
    return None

#Función para ctuzalizar el precio de un producto
def update_product(name,price_updated):
    product = search_product(name)
    if product:
        product["precio"] = price_updated
        print(f"\nEl precio de {name} fue actualizado, y es de {price_updated}")
    else:
        print(f"\nEl producto {name} no se ha encontrado en el inventario❗")
        
#Función para eliminar un producto del inventario
def delete_product(name):
    name = name.lower() #.lower() se usa para que tome name en minusculas
    if name in inventory:
        del inventory[name] #del se usa para eliminar elementos 
        print(f"\nEl producto {name} fue eliminado con éxito.")
    else:
        print(f"\nEl producto {name} no se ha encontrado en el inventario❗")
    
#Función para calcular el valor total de los productos del inventario.
def calculate_stock():
    total = 0
    for name in inventory:
        product = inventory[name]
        total += product["price"] * product["quantity"]
    print(f"\nEl valor total del inventario es: ${total:.2f}")
    return total
    
option_switch= True

while option_switch == True:
    print("""\nQue realizará el día de hoy:
      1. Añadir productos al inventario.
      2. Consultar disponibilidad y precio de productos existentes en el inventario.
      3. Actualizar el precio de algún producto del inventario.
      4. Eliminar productos.
      5. Calcular el valor total de los productos del inventario.
      6. Mostrar inventario.
      7. Salir.
      
      Le recordamos que para seleccionar una opción, tiene 2 maneras.
      1. Por número ("1" para añadir productos, "3" para actualizar algún precio, etc...)
      2. Por medio de una palabra clave ("Añadir", "Eliminar", etc...)
      """)
    
    option = input("\nSelecione una opción: ".lower())
    if option == "añadir" or option == "1":
        name = input("Ingrese el nombre del producto a añadir: ".capitalize())
        try:
            price = float(input("Digite el precio: "))
            quantity = int(input("Ingrese la cantidad: "))
            if price < 0 or quantity < 0:
                print("El precio y la cantidad deben ser positivos❗")
            else:
                add_products(name,price,quantity)
        except ValueError:
            print("❌Carácter inválido, intente de nuevo❌")
            
    elif option == "consultar" or option == "2":
        name = input("Ingrese el nombre del producto que desea consultar en el inventario: ")
        product = search_product(name)
        if product:
            print(f"\nProducto encontrado: {name.lower().title()} - Precio: ${product['precio']}, Cantidad: {product['cantidad']}")
            
    elif option == "actualizar" or option == "3":
        name = input("Ingrese el nombre del producto para actualizar su precio: ")
        try:
            update_price = float(input("Ingrese el nuevo precio: "))
            if  update_price < 0:
                print("Para poder actualizar el precio del producto ingresado, debe ser positivo❗")
            else:
                update_product(name,update_price)
        except ValueError:
            print("❌El precio ingresado es inválido❌")
            
    elif option == "eliminar" or option == "4":
        name = input("Ingrese el nombre del producto que desea eliminar del inventario: ")
        delete_product(name)
        
    elif option == "calcular" or option == "5":
        calculate_stock()
        
    elif option == "mostrar" or option == "6":
        print("\nInventario actual:")
        for name in inventory:
            product = inventory[name]
            print(f"Producto {name.title()} | precio ${product['precio']}| cantidad: {product['cantidad']}.")
    
    elif option == "salir" or option == "6":
        print("Hasta pronto!")
        option_switch = False      
        
    else:
        print("❌Opción inválida❌")  