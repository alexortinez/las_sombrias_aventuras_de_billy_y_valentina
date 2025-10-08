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
        
        #esto solo es una prueba jaja saludos
