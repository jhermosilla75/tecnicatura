# Ejercicio 3
# Escribir una función que permita mostrar todo el contenido de un archivo de texto. 
# La ruta de acceso al archivo debe ser pasada por parámetro.
def leer(ruta):
    """"Con esta funcion vamos a leer el contenido del archivo txt que pasamos como parametro"""
    with open(ruta, "r") as priarch:
        completo= priarch.read()
        return completo

ruta= "C:/PYTHON/MODULO 4/TP4/prueba_with.txt"
print(leer(ruta))