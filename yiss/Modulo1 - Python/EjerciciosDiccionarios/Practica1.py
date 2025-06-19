
# #VERSION 1
# def sumar(a,b):
#     print(f"la suma es {a+b}")
#     sumar(2,5)
#     sumar(7,3)
# def calculator(a:int,b:int):
#     plus = a+b
#     less = a - b
#     multi = a*b
#     if b != 0:
#         div = a/b
#     else:
#         div = "No se puede dividir por 0"
#     print(f"La suma es: {plus}")
#     print(f"La resta es: {less}")
#     print(f"La multiplicacion es: {multi}")
#     print(f"La division es: {div}")
# number_one = int(input("Ingrese el primer numero -> "))
# number_two = int(input("Ingrese el segundo numero -> "))
# calculator(number_one,number_two)


# #VERSION 2
# #calculator pero usando el return en lugar del print. version 1.2
# def calculadora(a: int, b: int):
#     plus = a + b
#     subs = a - b
#     multi = a * b
#     if b != 0:
#         div = a / b
#     else:
#         div = "No se puede dividir entre 0"
#     return plus, subs, multi, div
# number_1 = int(input("Ingrese el primer número -> "))
# number_2 = int(input("Ingrese el segundo número -> "))
# suma, resta, multi, division = calculadora(number_1, number_2)#los valores se asignan en el orden que los opera la funcion
# print(f"""
# La suma es: {suma}
# La resta es: {resta}
# La multiplicación es: {multi}
# La división es: {division}
# """)


#VERSION 3
#calculadora con return y alguna que otra mejora. version 1.3
def calculadora(a:int,b:int, operacion:str):
    if operacion == "suma":
        return a+b
    elif operacion == "resta":
        return a-b
    elif operacion == "multiplicacion":
        return a*b
    elif operacion == "division":
        if b != 0:
            return a/b
        else:
            return "No se puede dividir entre 0"
    else:
        return "Operacion invalida"

number_1 = int(input("Ingrese el primer numero -> "))
number_2 = int(input("Ingrese el segundo numero -> "))

print("Operaciones disponibles -> suma, resta, division y multiplicación")
operacion = input("¿Que operación desea realizar? -> ").lower()

resultado = calculadora(number_1,number_2, operacion)#lo que devuelve la función se guarda aqui la diferencia entre usar el return o no usarlo
print(f"""
    El resultado es -> {resultado}
    """)


#ULTIMA VERSION
def calculadora(a:int,b:int, operacion:str):
    if operacion == "suma":
        return a+b
    elif operacion == "resta":
        return a-b
    elif operacion == "multiplicacion":
        return a*b
    elif operacion == "division":
        if b != 0:
            return a/b
        else:
            return "No se puede dividir entre 0"
    else:
        return "Operacion invalida"

operacion = ""

while operacion != "salir":
    print("""\n---Calculadora---
    operaciones disponibles: suma, resta, multiplicación y división
    Escribe 'salir' para terminar. \n """)

    operacion = input("¿Que operación desea realizar? -> ").lower()

    if operacion == "salir":
        print("Gracias por usar la calculadora")
        break
    try:
        number_1 = int(input("Ingrese el primer numero -> "))
        number_2 = int(input("Ingrese el segundo numero -> "))
    except ValueError:
        print("Ingrese valores numericos validos")
        continue

    resultado = calculadora(number_1,number_2,operacion)
    print(f"El resultado es: {resultado}")