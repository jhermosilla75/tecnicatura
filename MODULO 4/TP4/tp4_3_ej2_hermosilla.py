# Ejercicio 2
# Escribir una GUI con dos botones, uno con la leyenda “Info” y otro con la leyenda
# “Advertencia”. Al hacer click a uno, debe mostrar una ventana emergente de
# información con el mensaje que Ud. quiera. Y el otro debe mostrar una ventana
# emergente de advertencia, también, con el mensaje que Ud. quiera.

import tkinter as tk
from tkinter import ttk, messagebox

class DosBotones(ttk.Frame):
    """Defino una clase heredada de tkinter donde voy a definir un contructor y 2 botones"""
    
    def __init__(self, parent):
        super().__init__(parent, padding=(100))
        parent.title("MODULO 3 TP 4 EJ 2")
        ttk.Button(self, text="Info", command=self.mensajei).grid()
        ttk.Button(self, text="Advertencia", command=self.mensajea).grid()

    @staticmethod
    def mensajei(msj='este boton mostrara informacion'):
            """Este metodo estatico se ejecuta cuando apretamos el boton Info"""
            messagebox.showinfo(message=msj)
    @staticmethod
    def mensajea(msj='este es un mensaje de advertencia'):
            """Este metodo estatico se ejecuta cuando apretamos el boton Advertencia"""
            messagebox.showwarning(message=msj)

root = tk.Tk()
DosBotones(root).grid()
root.mainloop()