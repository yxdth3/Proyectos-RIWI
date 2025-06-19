#Explicacion de funciones 
def saludar(nombre:str, edad:int=18)-> str:
    #Documentacion de la función 
    """
    nombre debe ser str
    edad debe ser int
    Recibe un formulario y lo retorna validado
    """
    print(f"Hola {nombre}! tienes {edad} años.") #interpolación
    
saludar(edad = 24,nombre = "Carlos")

# *args = 
# **kwargs = se usa para tokens, verificar acceso a la url
# import * importa todo 