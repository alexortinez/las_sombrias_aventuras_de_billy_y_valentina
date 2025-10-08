#Zury de Zaldo
num = int(input("Ingresa un valor y se determinará si es primo o no: "))

while True:
    num = int(input("Ingresa un valor y se determinará si es primo o no: "))

    if num <= 1:
        print(f"{num} no es primo")
    else:
        contador = 0
        for i in range(1, num + 1):
            if num % i == 0:
                contador += 1

        if contador == 2:
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")

    res = int(input("¿Deseas preguntar otro número? 1. Sí  2. No: "))

    if res == 1:
        continue
    elif res == 2:
        print("Hasta luego.")
        break
    else:
        print("Ingresa un valor válido (1 o 2).")
