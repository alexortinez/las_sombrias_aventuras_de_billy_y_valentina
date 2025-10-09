"""
Interfaz gráfica en Python (Tkinter)
Menú interactivo con 3 áreas:
 - Números primos: comprobar si un número es primo y listar primos hasta N
 - Días restantes: conteo regresivo hasta una fecha ingresada por el usuario
 - Multiplicaciones grandes: multiplicar enteros grandes y mostrar el resultado

Guarda este archivo y ejecútalo con: python interfaz_menu_primos_dias_multiplicaciones.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime, date
import math
import threading
import time

# ----------------- Funciones utilitarias -----------------

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def listar_primos_hasta(n: int):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
        p += 1
    return [i for i, is_p in enumerate(sieve) if is_p]

# ----------------- UI -----------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú interactivo — Primos | Días restantes | Multiplicaciones grandes")
        self.geometry("800x500")
        self.resizable(False, False)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        self.create_menu()
        self.create_frames()
        self.show_frame('Primos')

    def create_menu(self):
        menu_frame = ttk.Frame(self, padding=(10, 10))
        menu_frame.grid(row=0, column=0, sticky='ns')

        ttk.Label(menu_frame, text="Áreas", font=(None, 14, 'bold')).pack(pady=(0,10))

        ttk.Button(menu_frame, text="Números primos", width=20, command=lambda: self.show_frame('Primos')).pack(pady=5)
        ttk.Button(menu_frame, text="Días restantes", width=20, command=lambda: self.show_frame('Dias')).pack(pady=5)
        ttk.Button(menu_frame, text="Multiplicaciones grandes", width=20, command=lambda: self.show_frame('Multiplicaciones')).pack(pady=5)

        ttk.Separator(menu_frame, orient='horizontal').pack(fill='x', pady=10)
        ttk.Label(menu_frame, text="Instrucciones", wraplength=160).pack()
        ttk.Label(menu_frame, text="- Ingresa valores válidos\n- Formato fecha: YYYY-MM-DD\n- Resultado en panel derecho", wraplength=160, foreground='gray').pack(pady=(5,0))

    def create_frames(self):
        container = ttk.Frame(self, padding=(10,10))
        container.grid(row=0, column=1, sticky='nsew')
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        self.frames = {}

        for F in (FramePrimos, FrameDias, FrameMultiplicaciones):
            page_name = F.__name__.replace('Frame', '')
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[page_name] = frame

    def show_frame(self, name):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()

# ----------------- Página: Primos -----------------

class FramePrimos(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Números primos", font=(None, 16, 'bold')).pack(anchor='w')

        frame_check = ttk.LabelFrame(self, text="Comprobar si un número es primo", padding=10)
        frame_check.pack(fill='x', pady=8)

        ttk.Label(frame_check, text="Número:").grid(row=0, column=0, sticky='w')
        self.entry_num = ttk.Entry(frame_check, width=20)
        self.entry_num.grid(row=0, column=1, padx=6, pady=4)
        ttk.Button(frame_check, text="Comprobar", command=self.check_primo).grid(row=0, column=2, padx=6)

        self.label_check_result = ttk.Label(frame_check, text="")
        self.label_check_result.grid(row=1, column=0, columnspan=3, sticky='w')

        frame_list = ttk.LabelFrame(self, text="Listar primos hasta N", padding=10)
        frame_list.pack(fill='both', expand=True, pady=8)

        ttk.Label(frame_list, text="Listar hasta (N):").grid(row=0, column=0, sticky='w')
        self.entry_list_n = ttk.Entry(frame_list, width=20)
        self.entry_list_n.grid(row=0, column=1, padx=6, pady=4)
        ttk.Button(frame_list, text="Listar", command=self.listar_primos).grid(row=0, column=2, padx=6)

        self.text_primos = scrolledtext.ScrolledText(frame_list, height=10, wrap='word')
        self.text_primos.grid(row=1, column=0, columnspan=3, sticky='nsew', pady=(6,0))
        frame_list.columnconfigure(1, weight=1)

    def check_primo(self):
        val = self.entry_num.get().strip()
        try:
            n = int(val)
        except ValueError:
            messagebox.showerror("Error", "Introduce un número entero válido.")
            return
        self.label_check_result.config(text=f"{n} es primo." if es_primo(n) else f"{n} no es primo.")

    def listar_primos(self):
        val = self.entry_list_n.get().strip()
        try:
            n = int(val)
            if n < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Introduce un entero no negativo.")
            return
        primes = listar_primos_hasta(n)
        self.text_primos.delete('1.0', tk.END)
        if not primes:
            self.text_primos.insert(tk.END, "No hay primos hasta ese valor.")
        else:
            lines = []
            chunk_size = 20
            for i in range(0, len(primes), chunk_size):
                chunk = primes[i:i+chunk_size]
                lines.append(', '.join(map(str, chunk)))
            self.text_primos.insert(tk.END, '\n'.join(lines))

# ----------------- Página: Días restantes -----------------

class FrameDias(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.running = False

        ttk.Label(self, text="Días restantes (conteo regresivo)", font=(None, 16, 'bold')).pack(anchor='w')

        frame = ttk.LabelFrame(self, text="Ingresar fecha objetivo (YYYY-MM-DD)", padding=10)
        frame.pack(fill='x', pady=8)

        ttk.Label(frame, text="Fecha:").grid(row=0, column=0, sticky='w')
        self.entry_fecha = ttk.Entry(frame, width=20)
        self.entry_fecha.grid(row=0, column=1, padx=6, pady=4)

        ttk.Button(frame, text="Iniciar conteo", command=self.iniciar_conteo).grid(row=0, column=2, padx=6)

        self.label_result = ttk.Label(frame, text="")
        self.label_result.grid(row=1, column=0, columnspan=3, sticky='w', pady=(6,0))

    def iniciar_conteo(self):
        texto = self.entry_fecha.get().strip()
        try:
            self.fecha_objetivo = datetime.strptime(texto, '%Y-%m-%d').date()
        except Exception:
            messagebox.showerror("Error", "Formato de fecha inválido. Usa YYYY-MM-DD.")
            return
        self.running = True
        hilo = threading.Thread(target=self.actualizar_conteo, daemon=True)
        hilo.start()

    def actualizar_conteo(self):
        while self.running:
            hoy = datetime.now().date()
            diff = (self.fecha_objetivo - hoy).days
            if diff > 0:
                texto = f"Faltan {diff} día(s) para {self.fecha_objetivo}."
            elif diff == 0:
                texto = f"Hoy es la fecha objetivo: {self.fecha_objetivo}."
            else:
                texto = f"La fecha fue hace {-diff} día(s): {self.fecha_objetivo}."

            self.label_result.config(text=texto)
            time.sleep(60)  # Actualiza cada minuto

# ----------------- Página: Multiplicaciones grandes -----------------

class FrameMultiplicaciones(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Multiplicaciones grandes", font=(None, 16, 'bold')).pack(anchor='w')

        frame = ttk.LabelFrame(self, text="Multiplica dos enteros (pueden ser muy grandes)", padding=10)
        frame.pack(fill='x', pady=8)

        ttk.Label(frame, text="Número A:").grid(row=0, column=0, sticky='w')
        self.entry_a = ttk.Entry(frame, width=40)
        self.entry_a.grid(row=0, column=1, padx=6, pady=4)

        ttk.Label(frame, text="Número B:").grid(row=1, column=0, sticky='w')
        self.entry_b = ttk.Entry(frame, width=40)
        self.entry_b.grid(row=1, column=1, padx=6, pady=4)

        ttk.Button(frame, text="Multiplicar", command=self.multiplicar).grid(row=2, column=0, columnspan=2, pady=6)

        ttk.Label(self, text="Resultado:").pack(anchor='w', pady=(8,0))
        self.text_result = scrolledtext.ScrolledText(self, height=10, wrap='word')
        self.text_result.pack(fill='both', expand=True)

    def multiplicar(self):
        a_text = self.entry_a.get().strip()
        b_text = self.entry_b.get().strip()
        if not a_text or not b_text:
            messagebox.showerror("Error", "Introduce ambos números.")
            return
        try:
            a = int(a_text)
            b = int(b_text)
        except ValueError:
            messagebox.showerror("Error", "Ambos valores deben ser enteros (sin separadores).")
            return
        res = a * b
        self.text_result.delete('1.0', tk.END)
        self.text_result.insert(tk.END, f"{a} × {b} =\n\n{res}\n")

# ----------------- Ejecutar app -----------------

if __name__ == '__main__':
    app = App()
    app.mainloop()
