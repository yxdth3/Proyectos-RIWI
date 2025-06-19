#Cambiar las vocales de una palabra ingresada por simbolos.
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