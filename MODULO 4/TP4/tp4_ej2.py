# Ejercicio 2
# Escribir una función que permita agregar contenido a un archivo de texto. 
# La ruta de acceso al archivo y el contenido a agregar deben ser pasados por parámetro.
def agrega(ruta, agregado):
    """"Con with este se encarga de cerrar el archivo, es mejor abrir los archivo con with"""
    with open(ruta, "a") as priarch:
        priarch.write(agregado)

ruta= "C:/PYTHON/MODULO 4/TP4/prueba_with.txt"
agregado= "\nY si viene un rio gris Que separe al mundo en dos Quisiera quedar del mismo Lado, nena, que vos"
agrega(ruta, agregado)