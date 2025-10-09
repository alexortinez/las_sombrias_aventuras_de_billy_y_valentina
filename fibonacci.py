a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
n = int(input("¿Cuántos términos quieres? "))

print("\nSecuencia de Fibonacci:")
print(a, b, end=" ")

for i in range(n - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c