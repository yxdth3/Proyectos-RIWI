#Un espacio de coworking quiere una app para manejar las reservas de salas de reunión sin solapamientos y con confirmaciones automáticas.

# REQUERIMIENTOS:
# Crear reserva (nombre, sala, fecha, hora).
# Consultar reservas por sala y fecha.
# Cancelar reserva por nombre y fecha.
# Validar solapamientos.
# Exportar a reservas.csv.
# Formatos correctos de fecha/hora.
# Menú dinámico. 

import csv

# Lista donde se guardan las reservas
reservas = []

# Menú principal
def mostrar_menu():
    print("\n--- MENÚ DE RESERVAS ---")
    print("1. Crear nueva reserva")
    print("2. Consultar reservas por sala y fecha")
    print("3. Cancelar reserva por nombre y fecha")
    print("4. Exportar reservas a CSV")
    print("5. Salir")
    return input("Elige una opción (1-5): ")

# Validar que la fecha tenga formato YYYY-MM-DD
def formato_fecha_valido(fecha):
    partes = fecha.split("-")
    if len(partes) != 3:
        return False
    año, mes, día = partes
    return año.isdigit() and mes.isdigit() and día.isdigit() and len(año) == 4 and len(mes) == 2 and len(día) == 2

# Validar que la hora tenga formato HH:MM
def formato_hora_valido(hora):
    partes = hora.split(":")
    if len(partes) != 2:
        return False
    h, m = partes
    return h.isdigit() and m.isdigit() and 0 <= int(h) < 24 and 0 <= int(m) < 60

# Pedir fecha y hora válidas como strings
def pedir_fecha_hora():
    while True:
        fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
        hora = input("Ingresa la hora (HH:MM en 24h): ")
        if formato_fecha_valido(fecha) and formato_hora_valido(hora):
            return fecha, hora
        else:
            print("❌ Formato inválido. Intenta de nuevo.")

# Verifica si ya hay una reserva en esa sala, fecha y hora
def hay_solapamiento(sala, fecha, hora):
    for r in reservas:
        if r["sala"] == sala and r["fecha"] == fecha and r["hora"] == hora:
            return True
    return False

# Crear nueva reserva
def crear_reserva():
    nombre = input("Nombre del usuario: ")
    sala = input("Nombre de la sala: ")
    fecha, hora = pedir_fecha_hora()
    if hay_solapamiento(sala, fecha, hora):
        print("❌ Ya hay una reserva en esa sala, fecha y hora.")
    else:
        reservas.append({"nombre": nombre, "sala": sala, "fecha": fecha, "hora": hora})
        print("✅ Reserva creada exitosamente.")

# Consultar reservas por sala y fecha
def consultar_reservas():
    sala = input("Sala a consultar: ")
    fecha = input("Fecha a consultar (YYYY-MM-DD): ")
    if not formato_fecha_valido(fecha):
        print("❌ Formato de fecha inválido.")
        return
    print(f"\n📅 Reservas para la sala '{sala}' en {fecha}:")
    encontradas = False
    for r in reservas:
        if r["sala"] == sala and r["fecha"] == fecha:
            print(f" - {r['nombre']} a las {r['hora']}")
            encontradas = True
    if not encontradas:
        print("No hay reservas para esa fecha.")

# Cancelar reserva por nombre y fecha
def cancelar_reserva():
    nombre = input("Nombre del usuario: ")
    fecha, hora = pedir_fecha_hora()
    for r in reservas:
        if r["nombre"] == nombre and r["fecha"] == fecha and r["hora"] == hora:
            reservas.remove(r)
            print("✅ Reserva cancelada.")
            return
    print("❌ No se encontró la reserva.")

# Exportar reservas a un archivo CSV

def exportar_csv():
    with open("reservas.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Sala", "Fecha", "Hora"])
        for r in reservas:
            escritor.writerow([r["nombre"], r["sala"], r["fecha"], r["hora"]])
    print("📁 Reservas exportadas a 'reservas.csv'")

# Bucle principal

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        crear_reserva()
    elif opcion == "2":
        consultar_reservas()
    elif opcion == "3":
        cancelar_reserva()
    elif opcion == "4":
        exportar_csv()
    elif opcion == "5":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida.")
