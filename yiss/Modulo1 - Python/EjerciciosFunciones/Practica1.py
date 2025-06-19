
#Eres parte del equipo de tecnología de una academia en línea.
#Te han encargado desarrollar un sistema para calcular el promedio final de un estudiante. 
#El programa debe pedir nombre del estudiante, el número de materias cursadas, y por cada materia: el nombre y la nota obtenida (entre 0 y 5). 
#alcula el promedio, indica si pasó o no (>=3), y muestra un resumen de resultados. 
#Usa funciones, condicionales y validaciones de tipo.

#Damos la bienvenida
print("""
      Bienvenid@s al sistema 
      
    A continuación, calcularemos el promedio de sus notas.
      """)

def calculator_average(notes):
  if len(notes) == 0:
    return
  return sum(notes)/len(notes)

def determine_aprobation(average):
  if average >= 3:
    return "Felicidades, aprobó."
  else:
    return "Ops, mejor suerte la próxima. Reprobó"

name_student = input("Ingrese el nombre del estudiante: ")
subjects = int(input("Ingrese el número de materias cursadas: "))
notes = []

for i in range(subjects):
  name_subjects = input(f"Ingrese el nombre de la materia {i+1}: ")
  note = float(input(f"Ingrese la nota obtenida en {name_subjects} (de 0-5): "))
  
  while note < 0 or note > 5:
    print("Nota inválida, debe estar entre 0 y 5. Intente de nuevo. ")
  notes.append(note)


average = calculator_average(notes)
aprobation = determine_aprobation(average)
