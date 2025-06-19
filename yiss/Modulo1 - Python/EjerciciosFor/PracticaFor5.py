#Contar las letras de una palabra
#.lower() convierte a minúsculas todos los caracteres alfabéticos de una cadena de texto
#.upper() convierte a mayúsculas todos los caracteres alfabéticos de una cadena de texto

palabra = input("Escriba una palabra: ")

palabra = [letra.lower() for letra in palabra]  #list comprehension
palabraCantidad = 0

for i in palabra:

     if i == "a":
         palabraCantidad += 1
print(f"La letra a aparece {i} {"vez" if palabraCantidad == 1 else "veces"} en la palabra {palabra}")  #operador ternario
