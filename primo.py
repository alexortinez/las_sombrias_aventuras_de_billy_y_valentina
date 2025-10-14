#primo interesa un numero y te dice si es primo o no agregar que me diga el primo mas cerncano si le dio si es 25 que te diga el mas cercano al rpimo osea 25 no e spero para atras cual si lo es? 
def es_primo(n):
    if n < 2: return 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
num = int(input("Ingresa un número entero: "))
if num <= 1:
    print(f"El número {num} no es primo.")
elif es_primo(num):
    print(f"¡El número {num} SÍ es primo! ")
else:
    print(f"El número {num} NO es primo.")
    distancia = 1
    while True: 
        menor = num - distancia
        mayor = num + distancia
        if menor >= 2 and es_primo(menor):
            primo_cercano = menor
            break
        if es_primo(mayor):
            primo_cercano = mayor
            break    
        distancia += 1
    print(f"El primo más cercano a {num} es {primo_cercano}.")