# #HOLA SOY LIMON NUM PARES MUL del 1 al 100 solo pare
# CAMBIO QUE PREGUNTE PARES O IMPARES SI QUIERE
num = int(input("Dame un número porfa del 1 al 100 no mas no menos pls: "))
impares_si_no = input("¿Quieres múltiplos IMPARES en lugar de PARES? (S/N): ")
if impares_si_no == 'S':
    inicio = 1
    etiqueta = "IMPARES"
else:
    inicio = 2
    etiqueta = "PARES"
print("Tabla del", num, "con múltiplos", etiqueta, "del 1 al 100:")
for i in range(inicio, 101, 2):
    resultado = num * i
    print(num, "x", i, "=", resultado)