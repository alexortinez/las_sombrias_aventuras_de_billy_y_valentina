import customtkinter

def accion_boton(numero):
    print(f"Presionaste el Programa {numero}")

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

ventana = customtkinter.CTk()
ventana.title("Panel Estilizado")
ventana.geometry("300x400")

fuente_bonita = ("Arial", 16, "bold")
borde_redondo = 10

boton1 = customtkinter.CTkButton(ventana, 
                                 text="Programa 1", 
                                 command=lambda: accion_boton(1),
                                 font=fuente_bonita,
                                 corner_radius=borde_redondo)
boton1.pack(pady=10, ipadx=30, ipady=10)

boton2 = customtkinter.CTkButton(ventana, 
                                 text="Programa 2", 
                                 command=lambda: accion_boton(2),
                                 font=fuente_bonita,
                                 corner_radius=borde_redondo)
boton2.pack(pady=10, ipadx=30, ipady=10)

boton3 = customtkinter.CTkButton(ventana, 
                                 text="Programa 3", 
                                 command=lambda: accion_boton(3),
                                 font=fuente_bonita,
                                 corner_radius=borde_redondo)
boton3.pack(pady=10, ipadx=30, ipady=10)

boton4 = customtkinter.CTkButton(ventana, 
                                 text="Programa 4", 
                                 command=lambda: accion_boton(4),
                                 font=fuente_bonita,
                                 corner_radius=borde_redondo)
boton4.pack(pady=10, ipadx=30, ipady=10)

boton5 = customtkinter.CTkButton(ventana, 
                                 text="Programa 5", 
                                 command=lambda: accion_boton(5),
                                 font=fuente_bonita,
                                 corner_radius=borde_redondo)
boton5.pack(pady=10, ipadx=30, ipady=10)

ventana.mainloop()