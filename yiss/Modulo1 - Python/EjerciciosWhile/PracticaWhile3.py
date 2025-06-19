#Lista a elegir
while True:
     print("""Seleccione una opcion a realizar del menu: 
                      1. Saludar
                      2. Despedirse
                      3. Salir""")

     respuesta = int(input())
     
     if respuesta == 1:
        print("Su opción elegida fue saludar.")
     elif respuesta == 2:
        print("Su opciones elegida fue despedirse.")
     elif respuesta == 3:
        print("Su opcion elegida fue salir.")
        break
     else:
        print("Opcion ingresada inválida.")