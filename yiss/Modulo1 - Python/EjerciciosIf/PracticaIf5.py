    
    
#Sacar el numero divisible por 3 o por 5

try:
    numero = int(input("Ingrese un número: "))

    if numero % 3 == 0 and numero % 5 == 0:
        print("El número es divisible por 3 y por 5.")
    elif numero % 3 == 0:
        print("El número es divisible por 3.")
    elif numero % 5 == 0:
        print("El número es divisible por 5.")
    else:
        print("El número no es divisible por 3 ni por 5.")
except ValueError:
    print("Error, carácter no reconocido como número. ")