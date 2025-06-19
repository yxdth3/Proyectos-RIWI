            
#Imprimir el numero mayor negativo, positivo o nulo

try:
    numero = int(input("Ingrese un número: "))

    if numero > 0:
        print(f"El número es {numero} positivo.")
    elif numero < 0:
        print(f"El número es {numero} negativo.")
    elif numero == 0:
        print(f"El número es {numero} cero.")
    else:
        print("Número inválido.")
except ValueError: 
    print("Error, carácter no reconocido como número. ")
    