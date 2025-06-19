# crear un programa que calcule el costo total de una compra en una tienda.


# En las siguientes líneas de código interactuaremos con el usuario.
# Pedimos los 3 datos esenciales para poder calcular el costo total de la compra.

print("\n💰 Bienvenid@ al sistema autoservicio de facturación 💰")


print("\nPor favor, ingrese el nombre del producto: ")
nombreProducto = input()


# Preguntamos por el precio unitario del producto, usamos try para validar que el usuario no ingrese un caracter diferente que no sea numérico.
while True:
    precioUnitario = (input("\nIngrese el precio unitario del producto: $"))
    try:
        precioUnitarioFloat = float(precioUnitario)
        break
    except ValueError:
        print("\n❗Valor incorrecto, el precio debe ser ingresado en números. Intente de nuevo.❗")


# Preguntamos por el precio unitario del producto, usamos try para validar que el usuario no ingrese un caracter diferente que no sea numérico.
while True:
    cantidadProductos = (input("\nIngrese la cantidad a comprar: "))
    try:
        cantidadProductosFloat = float(cantidadProductos)
        break
    except ValueError:
        print("\n❗Valor incorrecto, el precio debe ser ingresado en números. Intente de nuevo.❗")


# Calculamos el costo total de la compra SIN descuento
totalSinDescuento = precioUnitarioFloat * cantidadProductosFloat

# Mostramos el costo total de la compra
print(f"\nEl costo total es de ${totalSinDescuento:.2f}")

# Líneas de código para aplicar descuento a la compra

preguntaDescuento = input("\n¿Desea aplicar un descuento a su valor total a pagar? (Si/No).")


# Aqui colocamos una lista con las maneras en las que el usuario puede escribir "si" para que no haya errores de escritura.
if preguntaDescuento in ["si", "sí", "Si", "Sí", "SI"]:

    # Preguntamos por el precio unitario del producto, usamos try para validar que el usuario no ingrese un caracter diferente que no sea numérico.
    while True:
        descuento = (input("\nIngrese el descuento a aplicar: "))
        try:
            descuentoFloat = int(descuento)
            break
        except ValueError:
            print(
                "\n❗Valor incorrecto, el precio debe ser ingresado en números. Intente de nuevo.❗")

    # Realizamos la operación para saber el valor a pagar con descuento
    
    totalConDescuento = totalSinDescuento - \
(totalSinDescuento * descuentoFloat / 100) 

    # el :.2f es para darle el formato de dos decimales
    print(f"\nEl valor total a pagar con descuento aplicado es de : ${totalConDescuento:.2f}.")
    valorDescontado = totalSinDescuento - totalConDescuento
else:

    print(f"\nEl producto comprado fue {nombreProducto} en {cantidadProductosFloat:.0f} cantidad con el precio unitario de ${precioUnitario}")
    print(f"\nLo cual nos da un total de ${totalSinDescuento:.2f} a pagar en su compra.")

 # Mostramos la facturación completa

print(f"""\n     Total facturación     
      
      Nombre del producto:                      {nombreProducto}
      Cantidad:                                 {cantidadProductosFloat:.0f}
      Precio unitario:                         ${precioUnitarioFloat}
      
      --------------------------------------------------------
      Total:                                   ${totalSinDescuento}
      """)

if preguntaDescuento in ["si", "sí", "Si", "Sí"]:
    print(f"""      Descuento aplicado:                      {descuentoFloat}%
      Valor descontado:                        ${valorDescontado}
      --------------------------------------------------------
      Total con descuento aplicado:            ${totalConDescuento}
                  """)
else:
    print("      Descuento aplicado:                       Ninguno")
