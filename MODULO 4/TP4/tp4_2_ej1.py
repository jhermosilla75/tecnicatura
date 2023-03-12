# Ejercicio 1
# Crear una función que permita al usuario ingresar por teclado cuantas cadenas quiera e ir almacenándolas 
# como líneas en un archivo de texto. La ruta de acceso del archivo se debe pasar por parámetro. 
# El archivo debe crearse si no existe y cada nueva línea debe agregarse al final del archivo.

# Solicitar reiteradamente al usuario por una nueva cadena hasta que decida no continuar.

def agrega_lineas(ruta):
    cadena= input("El texto que Ud. ingrese aqui se va a guardar en un txt. Ingrese (ENTER PARA SALIR):  ")
    while cadena !="":
        with open(ruta, "a") as archivo:
            archivo.write(cadena+"\n")
        cadena= input("El texto que Ud. ingrese aqui se va a guardar en un txt. Ingrese (ENTER PARA SALIR):  ")

ruta="C:/Python/JHermosilla/MODULO 4/TP4/tp4_2_ej1.txt"

agregamos=agrega_lineas(ruta)
