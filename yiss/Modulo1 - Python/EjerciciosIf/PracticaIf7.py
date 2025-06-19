#comprobar varias opciones 
dia= input("Ingrese un número del 1 al 7: ")

match dia:
    case "1":
        print("El día ingresado corresponde al lunes.")
    case "2":
        print("El día ingresado corresponde al martes.")
    case "3":
        print("El día ingresado corresponde al miércoles.")
    case "4":
        print("El día ingresado corresponde al jueves.")
    case "5":
        print("El día ingresado corresponde al viernes.")
    case "6":
        print("El día ingresado corresponde al sábado.")
    case "7":
        print("El día ingresado corresponde al domingo.")
    case _:
        print("Día inválido")
        
#otra manera
dias_semana = ["lunes", "martes","miercoles","jueves","viernes","sabado","domingo"]

try:
    dia=int(input("Ingrese un número del 1 al 7: "))
    print(f"el dia de la semana es {dias_semana[dia - 1]}")
    
except ValueError:
    print("Caracter invalido")
except:
    print("numero fuera de rango")