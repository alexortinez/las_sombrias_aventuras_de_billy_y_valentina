#HOLA SOY LIMON NUM PARES MUL  del 1 al 100 solo pare
num = int(input("Dame un número porfa del 1 al 100 no mas no menos pls: "))
print("Tabla del" ,num, "del 1 al 100:")
for i in range(2, 101, 2):
    resultado = num * i
    print(num, "x" ,i, "=", resultado)