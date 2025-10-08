import random  
import sys

secreto = random.randint(0, 50)


vidas = 3

print("\nAdivina el número en el que estoy pensando.")
print("Tienes 3 vidas para lograrlo.\n")

sys.stdout.flush()


while vidas > 0:
    
    intento = input(f"Escribe tu número (del 0 hasta 50): ")

    
    if not intento.isdigit():
        print("Error: escribe solo números enteros.")
        continue  

    #
    numero = int(intento)

    
    if numero < 0 or numero > 50:
        print("El número debe estar entre 0 y 50. Intenta otra vez.")
        continue

    
    if numero == secreto:
        print(f"¡MUY BIEN! Adivinaste el número secreto: {secreto}")
        break  

    
    diferencia = abs(numero - secreto)

    if numero < secreto:
        print("Muy bajo.")
    else:
        print("Muy alto.")

    
    if diferencia <= 3:
        print("¡Estás muy cerca!")
    elif diferencia <= 10:
        print("Te estás acercando.")
    else:
        print("Estás lejos, sigue intentando.")

    
    vidas -= 1


if vidas == 0:
    print("\nSe terminaron tus vidas.")
    print(f"El número secreto era: {secreto}")

input("\nPresiona Enter para salir...")