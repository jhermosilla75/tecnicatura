"""Escribir una función que permita crear un archivo de texto con algún contenido. La ruta de acceso al archivo 
y su contenido deben ser pasados por parámetro. Si el archivo ya existía, sobrescribirlo."""

# def crear_archivo(ruta, contenido):
#     """la funcion open tiene como desventaja tener que acordarse de cerrar el archivo despues de trabajarlo"""
#     archivo= open(ruta,"w")
#     archivo.write(contenido)
#     archivo.close()
# ruta= "c:/proyecto/prueba.txt"
# contenido = "Y si viene un rio gris Que separe al mundo en dos Quisiera quedar del mismo Lado, nena, que vos"
# crear_archivo(ruta, contenido)

def crea_archivo(ruta, contenido):
    """"Con with este se encarga de cerrar el archivo, es mejor abrir los archivo con with"""
    with open(ruta, "w") as priarch:  # tambien lo podría abrir con "a" en este caso no sobrescribe si no que agrega al final
        priarch.write(contenido)
ruta= "C:/PYTHON/MODULO 4/TP4/prueba_with.txt"
contenido = "Hay algo que está sonando Seguro que ya lo oías La tierra está vibrando Con distinta melodía"
crea_archivo(ruta, contenido)
# hgvklh
