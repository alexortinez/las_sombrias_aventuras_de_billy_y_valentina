import os

programas = {
    "1": "multiplicacion.py",
    "2": "numero_azar.py",
    "3": "kaprekar.py",
    "4": "semana_info.py",
    "5": "primos.py",
    "6": "bisiesto.py",
    "7": "salario.py"
}

while True:
    print("\n=== MENÚ DEL PROYECTO ===")
    print("1. Multiplicación del 1 al 100")
    print("2. Número al azar")
    print("3. Kaprekar")
    print("4. Días para Semana de Informática")
    print("5. Números primos")
    print("6. Año bisiesto")
    print("7. Salario por hora")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "8":
        print(" Saliendo del programa...")
        break

    elif opcion in programas:
        archivo = programas[opcion]
        if os.path.exists(archivo):
            os.system(f"python {archivo}")
        else:
            print(f" No se encontró el archivo '{archivo}'. Asegúrate de que esté en la misma carpeta.")
    else:
        print(" Opción no válida. Intenta de nuevo.")
