
#Para acceder al valor de la clave
coder = {
    "nombre" : "Isa",
    "apellido" : "Fernández",
    "edad" : 20,
    "peso" : 46.5
}

print(f"Hola {coder["nombre"]} {coder['apellido']}!!!!")


#Añadir llaves
coder["genero"] = "Femenino"
coder["estado"] = "viva"
coder["ciudad"] = "bogota"

print(coder)

#eliminar un valor
del(coder["estado"])
print(coder)

#Listas en diccionarios
coders = [{
    "nombre" : "Isa",
    "apellido" : "Fernández",
    "edad" : 20,
    "peso" : 46.5
},
{
    "nombre" : "Juan",
    "apellido" : "Hernández",
    "edad" : 30,
    "peso" : 86.5
}]

for i in range (len(coders)):
    print(coders[i])