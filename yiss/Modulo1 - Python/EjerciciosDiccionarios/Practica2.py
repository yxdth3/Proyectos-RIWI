#Debes crear un programa para una cafetería que permita al usuario elegir productos 
# de un menú (mínimo 5 ítems), indicar la cantidad de cada uno y calcular el total.
# Si el pedido supera los $50, aplica un 10% de descuento. 
# Implementa funciones, listas, bucles y formato de salida

print("🥳 Bienvenidos a Coffee Scape 🥳")

options = {
    "latte" : 5.600,
    "capuccino" : 8.000,
    "tinto" : 1.500,
    "americano" : 9.300,
    "mocca" : 5.000,
    "expresso" : 6.400
}
print("\nOpciones disponibles: ")
keys = " - ".join(list(options.keys()))
print(keys)
order = input("\nElija el producto que desea el día de hoy: ".lower())

continuar  = True

def product_elected(option:str,price:float,quantities:int):
    while continuar:
        if order in options:
            answer = input(f"El precio del {option} es de {price:.3f}. Desea continuar con la compra? (yes/no)".lower())
        while answer == "yes":
            try: 
                quantities = int(input(f"Ingrese la cantidad de {option} a comprar: "))
                total = price * quantities
                print(f"El total a pagar por {quantities} {option}: {total:.3f}")
                break
            except ValueError:
                print("Respuesta errónea, intente de nuevo.")
        else: 
            print("Escoja otra opción: ")
        

product_elected(order, options.get(order, 0), 0)

    
    