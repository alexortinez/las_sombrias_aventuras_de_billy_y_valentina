#HOLA SOY LIMON NUM PARES MUL  del 1 al 10 solo pare
#Cambio Multiplicación del 1 al 10, pero agregar decimales
def tabla(num, start=2, end=10, step=2, decimals=2):
    print("Tabla del", num, "del", start, "al", end)
    for i in range(start, end + 1, step):
        resultado = num * i
        print (num, "x", i, "=", resultado)
try:
    num = int(input("Dame un número porfa del 1 al 10 no mas no menos pls: "))
except ValueError:
    print("Entrada no válida")
else:
    if 1 <= num <= 100:
        tabla(num, decimals=2)  # cambia decimals si quieres más o menos decimales
    else:
        print("Número fuera de rango (1-10)")