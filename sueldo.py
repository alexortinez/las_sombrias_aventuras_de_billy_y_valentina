Sueldo = float(input("introduce tu sueldo porfavor"))
horas = float(input("cuantas horas trabajas"))

Pago = Sueldo / horas
semana = Pago * 7
mes = Pago * 30
año = Pago * 360

def mostrar_menu():
    print("OPciones ")
    print("1.-Sueldo al dia")
    print("2.-conocer sueldo semanal: ")
    print("3.-conocer sueldo mensual: ")
    print("4.-sueldo anual: ")


def mostrar_dia():
    print(f"tu sueldo al dia es de: {Pago}")
def mostrar_semana():
    print(f"tu sueldo a la semana es de: {semana}")
def mostrar_mes():
    print(f"tu sueldo al mes es de: {mes}")
def  mostrar_año():
    print(f"tu sueldo al año es de: {año}")

while True:
    mostrar_menu()
    opcion = input("introduce una opcion")

    if opcion == "1":
        mostrar_dia()
    elif opcion == "2":
        mostrar_semana()
    elif opcion == "3":
        mostrar_mes()
    elif opcion == "4":
        mostrar_año()
    else:
        print("opcion no valida")


