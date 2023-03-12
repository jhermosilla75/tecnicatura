# Ejercicio 5
# Escribir una función que devuelva la cantidad de líneas que tiene un archivo de texto. 
# La ruta de acceso del archivo debe ser pasada por parámetro.
def can_lin(ruta):
    """Con esta función vamos a devolver la cantidad de lineas que tiene el archivo txt"""
    with open(ruta, "r") as priarch:
        todo= priarch.readlines()
        return len(todo)

ruta= "C:/PYTHON/MODULO 4/TP4/prueba_with.txt"
print(f"El archivo txt tiene:  {can_lin(ruta)} lineas")