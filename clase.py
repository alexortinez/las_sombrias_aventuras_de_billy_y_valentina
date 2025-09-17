numeros = [5, 8, 3, 9, 5.2, 4, 8, 3, 6, 10, 2, 6, 8, 10.1, 11, 4, 3, 5, 6, 7, 2, 1, 8, 2, 6, 7]

n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] < numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("tamaños ordenados de mayor a menor")
print(numeros)
