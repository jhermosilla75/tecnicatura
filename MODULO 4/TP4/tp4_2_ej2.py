# Ejercicio 2
# Defina una función que permita crear un archivo en formato JSON llamado archivo_cumples.
#json y guardar nombre y fecha de nacimiento de distintas personas. 
#El nombre del archivo se debe pasar como parámetro. 
#Los datos de las personas se pasan a la función en una lista de diccionarios. 
#Los diccionarios deben tener la estructura que se muestra en el ejemplo siguiente.

# cumples = [{"nombre": "Juan Perez", "fecha_nac": "15/02/98"},
#            {"nombre": "Esteban Quito","fecha_nac": "08/07/95"}]
# Se debe poder usar de la siguiente forma:

# crear_archivo_cumples("archivo_cumples.json", cumples)

def crea_json(ruta, cumples):
    """Con esta funcion tomamos un objeto phyton lo serializamos y lo guardamos en un archivo json
    usamos dump (sin s)"""
    import json
    with open(ruta, "w") as archivo:
        json.dump(cumples, archivo)


cumples = [{"nombre": "Juan Perez", "fecha_nac": "15/02/98"},
          {"nombre": "Esteban Quito","fecha_nac": "08/07/95"}]

ruta="C:/Python/JHermosilla/MODULO 4/TP4/archivo_cumples.json"
crea_json(ruta, cumples)