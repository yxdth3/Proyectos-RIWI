    
#Clasificar la calificacion ingresada

calificacion = float(input ("Ingrese la calificación del estudiante (Entre 0 a 10)."))
if calificacion < 5:
    print("Su calificación es F.")
else: 
    if calificacion == 5 and calificacion <= 6.5:
        print("Su calificación es C.")
    else:
        if calificacion == 7 and calificacion <= 8.9:
            print("Su calificación es B.")
        else:
            if calificacion == 9 and calificacion == 10:
                print("Su calificación es A.")
            else: print("La calificación ingresada es inválida.")