# Ejercicio 6
# Escribir una función que devuelva la n-ésima línea de un archivo de texto. 
# La ruta de acceso del archivo y el número de línea deben ser pasados por parámetro.

# Si el archivo tiene menos cantidad de líneas de lo que se pide debe mostrar un mensaje por pantalla informándolo.
def devuelve_can_lineas(ruta,nlinea):
    """Con esta funcion vamos a devolver LA LINEA INGRESADA COMO ARGUMENTO / PARAMETRO tiene el archivo txt"""
    with open(ruta, "r") as priarch:
        todlin= priarch.readlines()
        canlin= len(todlin)
        print(canlin)
        if nlinea > canlin:
            print("el archivo no cuenta con esa linea")
            return
        print(todlin[nlinea-1])

ruta= "C:/PYTHON/MODULO 4/TP4/prueba_with.txt"
devuelve_can_lineas(ruta,4)