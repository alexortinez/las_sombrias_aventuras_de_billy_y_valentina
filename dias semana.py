from datetime import datetime

def dias_hasta_diciembre10(fecha_str):
    try:
        
        fecha_ingresada = datetime.strptime(fecha_str, "%Y-%m-%d")
        anio = fecha_ingresada.year

        fecha_objetivo = datetime(anio, 12, 10)

        diferencia = (fecha_objetivo - fecha_ingresada).days

        if diferencia < 0:
            print("El 10 de diciembre ya pasó en ese año.")
        elif diferencia == 0:
            print("¡Hoy es 10 de diciembre!")
        else:
            print(f"Faltan {diferencia} días para el 10 de diciembre de {anio}.")
    except ValueError:
        print("Formato de fecha inválido. Usa el formato AAAA-MM-DD (ej: 2025-10-08)")


fecha_usuario = input("Ingresa una fecha (formato AAAA-MM-DD): ")
dias_hasta_diciembre10(fecha_usuario)

