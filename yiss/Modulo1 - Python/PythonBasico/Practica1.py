
#Sacar el factorial de un numero
numero = int(input("Ingrese un número para calcular su factorial: "))
factorial= 1
for i in range (1,numero+1):
    factorial = i * factorial
print(f"el factorial de {numero} es {factorial}")