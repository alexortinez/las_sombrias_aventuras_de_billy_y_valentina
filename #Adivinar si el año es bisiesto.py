#Adivinar si el año es bisiesto
entrada = input("Ingrese un año: ")
if entrada.isdigit():
    anio = int(entrada)
    if 1000 <= anio <= 1_000_000:
        print("El año es válido")
        if (anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año debe estar entre 1000 y 1,000,000")
else:
    print("El año no es válido")