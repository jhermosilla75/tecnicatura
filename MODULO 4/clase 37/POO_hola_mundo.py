# import tkinter as tk
# from tkinter import ttk, messagebox

# class App(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         ttk.Button(self, text="Hola", command=self.mensaje).grid()
#     def mensaje(self):
#         print("mundo")

# root = tk.Tk()
# App(root).grid()
# root.mainloop()

#mejorado

import tkinter as tk
from tkinter import ttk, messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Button(self, text="Hola", command=self.mensaje).grid()
    @staticmethod
    def mensaje(msj='mundo!'):
        messagebox.showinfo(message=msj)

root = tk.Tk()
App(root).grid()
root.mainloop()