#Validar una contraseña

contraseña = input("Ingrese la contraseña: ")

if contraseña == "admin12345":
    print("Contraseña correcta")
    
    
#Validar una contraseña doble

contraseña = input("Ingrese su contraseña: ")
validacionContraseña = input("Por favor, ingrese de nuevo su contraseña: ")

if contraseña == validacionContraseña:
    print("Acceso admitido. ")
else: 
    print("Contraseña incorrecta. ")