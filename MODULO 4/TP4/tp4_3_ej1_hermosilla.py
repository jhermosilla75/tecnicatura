# Trabajo Práctico 3
# Las interfaces solicitadas en este Trabajo Práctico deben ser
# programadas aplicando POO.
# Ejercicio 1
# Escribir una GUI con un botón con la leyenda “Mostrar fecha” y que al presionarlo
# muestre por consola la fecha del día
import tkinter as tk
from tkinter import ttk
import datetime as dt


class MuestraFecha(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        parent.title("TP 4 EJ 1")
        ttk.Button(self, text="Mostrar fecha", command=lambda: print(dt.datetime.now())).grid()
root = tk.Tk()
MuestraFecha(root).grid()
root.mainloop()


