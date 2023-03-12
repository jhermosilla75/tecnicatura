# Ejercicio 3
# Escribir una GUI con una entrada de texto y un botón con la leyenda “Mostrar”. Al hacer
# click en el botón se debe mostrar el contenido de la entrada de texto por consola.
import tkinter as tk
from tkinter import ttk


class EntradaTexto(ttk.Frame):
    """Creamos una clase heredada, no voy a ocuparme de la grafica por ahora solamente en lo funcional"""
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        parent.title("MODULO 3 TP 4 EJ 3")
        self.texto = tk.StringVar()
        ttk.Label(self, text="ingrese un texto",).grid(row=0, column=1)
        ttk.Entry(self, textvariable=self.texto).grid(row=0, column=2)
        ttk.Button(self, text="Mostrar",  command=self.mostrar).grid(row=10, column=3)
    
    def mostrar(self):
        """Esta funcion se ejecuta cuando presionan el boton mostrar y la funcion muestra como str lo que se ingreso como texto """
        print(f"El texto ingresado es:  {self.texto.get()}")

root = tk.Tk()
EntradaTexto(root).grid()
root.mainloop()