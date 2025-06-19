
numeros = []
contador = 0
i=0
str_numeros = ''
print("\n---------------------------------------------")

while len(numeros) < 5:
    numero = int(input(f"Ingrese el número {i+1}. "))
    numeros.append(numero)
    i+=1

for valor in numeros:
    if valor > 0:
        contador += 1

for numero in numeros:
    str_numeros += f"{str(numero)+', ' if numero != numeros[-1] else str(numero)+'.'}"


print (f"\nLos números ingresados son: {str_numeros}") 
print(f"Cantidad de números positivos : {contador}") 


print("\n---------------------------------------------")

