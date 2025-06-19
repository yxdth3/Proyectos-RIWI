
#Calculadora

numero1 = int(input("Ingrese el primer número a calcular: "))
numero2 = int(input("Ingrese el segundo número a calcular: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

print(f"La suma de los números es igual a: {suma}")
print(f"La resta de los números es igual a: {resta}")
print(f"La multiplicación de los números es igual a: {multiplicacion}")

try:
  division = numero1 // numero2
  print(f"La división de los números es igual a: {division}")
except:
  print("La división no se puede ejecutar, ya que el divisor no es 0. ******")