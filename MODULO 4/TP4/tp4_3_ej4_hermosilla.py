# Ejercicio 4
# Mejorar el ejercicio anterior revisando si la entrada de texto contiene algo antes de
# mostrar. Si no contiene nada (la cadena vacía) mostrar una ventana emergente de
# información con el mensaje: “Debe ingresar algo en la entrada de texto para poder
# mostrarlo.”
import tkinter as tk
from tkinter import ttk, messagebox

class EntradaTexto(ttk.Frame):
    """Creamos una clase heredada, no voy a ocuparme de la grafica por ahora solamente en lo funcional"""
    def __init__(self, parent):
        super().__init__(parent, padding=(10))
        parent.title("MODULO 3 TP 4 EJ 4")
        self.texto = tk.StringVar()
        ttk.Label(self, text="ingrese un texto",).grid(row=0, column=1)
        ttk.Entry(self, textvariable=self.texto).grid(row=0, column=2)
        ttk.Button(self, text="Mostrar",  command=self.mostrar).grid(row=10, column=3)
    
    def mostrar(self, msj='Debe ingresar algo en la entrada de texto para poder mostrarlo'):
        """Esta funcion se ejecuta cuando presionan el boton mostrar y la funcion muestra como str lo que se ingreso
        como texto, si no se ingresa nada lo advertimos por pantalla"""
        if self.texto.get():
            print(f"El texto ingresado es:  {self.texto.get()}")
        else:
            messagebox.showinfo(message= msj)

root = tk.Tk()
EntradaTexto(root).grid()
root.mainloop()