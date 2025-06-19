#Reemplazar vocales por un símbolo en una palabra dada

vocales = ["a","e","i","o","u"]
palabra = input("Ingrese una palabra: ".lower())
palabraCambiada = ""
simbolo = "*"

for letra in palabra: 
    if letra in vocales:
        palabraCambiada += simbolo
    else:
        palabraCambiada += letra
        
print(f"La palabra es {palabra} \nCambiando sus vocales por el simbolo + es: {palabraCambiada}")

#Otra opcion
vocales = ["a", "e", "i", "o", "u"]
palabra = input("Ingrese una palabra -> ")
i=0 
palabraCambiada = ""
simbolos = {
    "a":"@",
    "e":"&",
    "i":"%",
    "o":"/",
    "u":"*"
}
for letra in palabra:
    if letra in vocales:
        palabraCambiada += simbolos[letra]
        i+=1
    else:
        palabraCambiada += letra

print(f"Palabra modificada -> {palabraCambiada}")
print(f"Vocales reemplazadas -> {i}")