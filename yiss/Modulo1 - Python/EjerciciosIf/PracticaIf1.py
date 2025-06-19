#retirar dinero, ingresar, hacer una transaccion o cambiar la clave.
print("""Seleccione una operación bancaria a realizar: 
        1. Ingresar dinero.
        2. Retirar dinero.
        3. Hacer una transacción.
        4. Cambiar la clave.""")
preguntaUsuario = input()
if preguntaUsuario == "Ingresar dinero":
    print("Cuánto dinero quiere ingresar:")
elif preguntaUsuario == "Retirar dinero":
    print("Cuánto dinero quiere retirar: ")
elif preguntaUsuario == "Hacer una transaccion":
    print("Seleccione la persona a la cuál hará transferir su dinero: ")
elif preguntaUsuario == "Cambiar la clave":
    print("Digite su nueva clave:")
else:
    print("Operación inválida.")