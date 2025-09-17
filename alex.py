
valerina = 0
metro = 5
metrobus = 7

opcion = int(input(
    "Usuario, dime qué opción quieres ver:\n"
    "1.- Ir en metro\n"
    "2.- Ir en metrobus\n"
    "3.- Ir caminando\n"
    "Elige 1, 2 o 3: "
))


if opcion == 1:
    total = valerina + metro
    print(f"Val tomó el metro, recorrió 5 estaciones sin transbordo y gastó: ${total}")
    print("val abrio la puerta")
    print("val bajo las escaleras")
    print("giro a la izquierda")
    print("se fue hasta la esquina")
    print ("giro hacia  la izquierda")
    print("salio hasta el esacionamiento")
    print("salio a la caferteria")
    print("giro a la izquierda")
    print("fue a la entrada")
    print("salio")
    print("giro a a derecha ")
    print("giro a la izquierda y camino todo derecho")
    print("luego")
elif opcion == 2:
    total = valerina + metrobus * 2  
    print(f"Val viajó en metrobus, hizo un transbordo, y pagó dos veces. Total gastado: ${total}")

elif opcion == 3:
    print(f"Val decidió caminar. No gastó ni un peso. Total: ${valerina}")

