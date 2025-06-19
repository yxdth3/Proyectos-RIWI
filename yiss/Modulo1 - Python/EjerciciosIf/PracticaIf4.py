#si eldueldo es mayor de 5.000.000 debe declarar renta

sueldo = input("Ingrese su salario: ")

if sueldo >= "5000000":
    print("Usted debe declarar renta.")
else:
    print("Usted esta libre de declarar renta.")
    
    
#Mostrar el número mayor, menor o igual

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    if numero1 > numero2:
        print(f"El número {numero1} es mayor que el número {numero2}.")
    elif numero1 < numero2:
        print(f"El número {numero1} es menor que el número {numero2}.")
    elif numero1 == numero2:
        print(f"El número {numero1} es igual al número {numero2}.")
    else:
        print("Número inválido.")
except ValueError: 
    print("Error, carácter no reconocido como número. ")