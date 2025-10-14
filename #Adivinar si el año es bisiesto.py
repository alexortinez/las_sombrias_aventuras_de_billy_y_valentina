#Adivinar si el año es bisiesto
#se añadio el def
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

entrada = input("Ingrese un año: ")
if entrada.isdigit():
    anio = int(entrada)
    if 1000 <= anio <= 1_000_000:
        print("El año es válido")
        if is_leap(anio):
            print("El año es bisiesto")
            print("Faltan 0 años para el año bisiesto")
            print(f"El próximo año bisiesto es {anio}")
        else:
            next_year = anio + 1
            while not is_leap(next_year):
                next_year += 1
            faltan = next_year - anio
            print(f"El próximo año bisiesto es {next_year}")
            print(f"Faltan {faltan} años para el próximo año bisiesto")
    else:
        print("El año debe estar entre 1000 y 1,000,000")
else:
    print("El año no es válido")