# Damos la bienvenida al programa
note_entrance = 0
print(""" 
             🥸  Bienvenido a la calculadora de notas 🥸
        ❕Recuerde que se evalúa como aprobada con una calificación igual o por encima de 60❕.
      """)
validation_initial = True
# Pedimos que el usuario ingrese una nota y evaluamos en reprobada o aprobada según ésta.
while validation_initial :

    try:
        note_entrance = float(input("\nIngrese una calificación a ser evaluada:  "))
        if 0 <= note_entrance <= 60:
            print(f"\nEl estudiante ha sido reprobado con una calificación de {note_entrance:.1f} / 100.0, ya que se encuentra por debajo del rango establecido 😭.")
            break
        elif 60 < note_entrance <= 100:
            print(f"\nEl estudiante ha sido aprobado con una calificación de {note_entrance:.1f} / 100.0, ya que se encuentra dentro del rango establecido 😄.")
            validation_initial = False
            break
        else:
            print("\n❌ Calificación inválida, la calificación debe estar entre 0 y 100. Intente de nuevo ❌.")
    except ValueError:
        print("\n❌ Error, carácter no reconocido como número. Intente de nuevo ❌.")
        

# Pedir al usuario una lista de notas (separadas por coma)
list_notes = []
notes = 0
while validation_initial:
    
    notes = input("\nIngrese las calificaciones separadas por comas (Ejemplo:80, 65.5, 100) : ")
    if " " in notes:
        print("\n ❌ Solo ingrese las notas separadas por comas, no incluya espacios. Intente de nuevo ❌.")
        validation_notes = False
    else:

        try:
            list_notes = [float(note.strip()) for note  in notes.split(",")] #usamos .strip() para eliminar espacios o carateres iniciales y finales, y usamos .split() para separar por comas 
            validation_notes = True # Definimos que las notas ingresadas serán todas correctas o válidas (en este caso, positivas)
            for note in list_notes:
                if note < 0 or note > 100:
                    print("\n❌ Todas las calificaciones deben estar entre 0 y 100, Intente de nuevo ❌.")
                    validation_notes = False # Al encontrar notas en negativo que cambie la variable a False para saber que hay notas inválidas.
                    break    
            # Calcular el promedio de las notas en la lista
            if validation_notes:
                total = 0
                for note in list_notes:
                    total += note
                average = total /len(list_notes)  #Usamos len para devolver la cantidad de notas ingresadas
                print("\n📋 Lista de calificaciones ingresadas:")
                print(" " + ", ".join([f"{note}" for note in list_notes])) # Usamos .join() para unir o agrupar cada uno de los elementos de listaNotas con ", "
                print(f"\n El promedio de las calificaciones ingresadas es {average:.1f}")
                validation_initial = False
                break
        except ValueError:
            print("\n❌ Error, carácter no reconocido como número. Intente de nuevo ❌. ")
            notes = 0

# Contar cuántas calificaciones en la lista son mayores al valor ingresado por el usuario
note_high = float(input("\nIngrese una nota específica para saber cuántas notas son iguales o mayores a ésta: "))
counter = 0  #Inicializamos el contador en 0
for note in list_notes:
    if note > note_high:
        counter += 1

# Verificar la presencia de una calificación específica y contar cuántas veces aparece
note_equal = 0 #Inicializamos en 0
for i in range(len(list_notes)):
    if list_notes[i] == note_high:
        note_equal += 1

print(f"""\n El número de calificaciones mayores a {note_high} es 👉 {counter} 
      \n El número de calificaciones igual a {note_high} es 👉 {note_equal}""")
