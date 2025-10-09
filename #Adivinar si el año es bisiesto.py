#Adivinar si el año es bisiesto
entrada = input("Ingrese un año: ")
if entrada.isdigit():
    anio = int(entrada)
    if 1000 <= anio <= 1_000_000:
        print("El año es válido")
        if (anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0):
            print("El año es bisiesto")
            # calcular el siguiente año bisiesto distinto al actual
            anio_bisiesto = anio + 1
            while not ((anio_bisiesto % 4 == 0 and anio_bisiesto % 100 != 0) or (anio_bisiesto % 400 == 0)):
                anio_bisiesto += 1
            print("El próximo año bisiesto será", anio_bisiesto)
            print("Faltan", anio_bisiesto - anio, "años para ese año bisiesto")
        else:
            print("El año no es bisiesto")
            anio_bisiesto = anio + 1
            while not ((anio_bisiesto % 4 == 0 and anio_bisiesto % 100 != 0) or (anio_bisiesto % 400 == 0)):
                anio_bisiesto += 1
            print("El próximo año bisiesto es", anio_bisiesto)
            print("Faltan", anio_bisiesto - anio, "años para ese año bisiesto")
    else:
        print("El año debe estar entre 1000 y 1,000,000")
else:
    print("El año no es válido")