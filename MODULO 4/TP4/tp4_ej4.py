# Ejercicio 4
# Escriba una función que devuelva la cantidad de caracteres de un archivo de texto. 
# la ruta de acceso al archivo debe ser pasada por parámetro.

# No se debe tener en cuenta el caracter '\n'.
def cantidad(ruta):
    """"Con esta funcion vamos a contar la cantidad de caracteres que tiene el archivo sin incluir los saltos de linea"""
    with open(ruta, "r") as priarch:
        todo= priarch.read()
        salto= todo.count("\n")
        can= priarch.tell()- salto
        return can

ruta= "C:/PYTHON/MODULO 4/TP4/prueba_with.txt"
print(f"la cantidad de caracteres del archivo txt es de:  {cantidad(ruta)} sin tener en cuenta los saltos de linea")