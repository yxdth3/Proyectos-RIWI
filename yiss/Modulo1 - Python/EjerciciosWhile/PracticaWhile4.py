#Adivina el numero
try:
    while True:

        numeroSecreto = 3
        print("Adivine el número secreto: ")
        
        pregunta = int(input())
        
        if pregunta == 3:
            print("Ha adivinado el número.")
            break
        elif pregunta < 3:
            print(f"El número secreto es mayor {pregunta}, intente de nuevo.")
        elif pregunta > 3:
            print(f"El numero secreo es menor que {pregunta}, intente de nuevo")
        else: 
            print("Numero invalido.")
except ValueError:
    print("Error, carácter no reconocido como número. ")