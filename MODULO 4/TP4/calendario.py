import tkinter as tk
from tkinter import ttk, messagebox
import nuevo_evento as n

class ProyectoCalendario(tk.Frame):
    def __init__(self, ventana, padding = 10):
        super().__init__(ventana)
        ventana.title("EL PROYECTO")
        ventana.geometry("800x600")
        ttk.Button(self, text="Nuevo",  command= n.evento).grid(row=10, column=3)
        
    def guardar(self):
        print("tengo que guardar el evento")

 
root = tk.Tk()
ProyectoCalendario(root).grid()
root.mainloop()


       # # Crear widgets
        # self.calendar_label = tk.Label(self.master, text="Calendario de Eventos", font=("Arial", 20))
        # self.calendar_label.grid()
        
        # self.calendar = tk.Frame(self.master)
        # self.calendar.grid()
        
        # self.prev_button = tk.Button(self.master, text="Anterior", command=self.prev_week)
        # self.prev_button.grid(side="left")
        
        # self.next_button = tk.Button(self.master, text="Siguiente", command=self.next_week)
        # self.next_button.grid(side="right")
