# Ejercicio 3
# Partiendo del archivo del ejercicio anterior, defina una función que permita agregar el nombre de una persona 
# (y su fecha de nacimiento) al archivo. El nombre del archivo se debe pasar como parámetro, 
# así como los datos de la persona, 
# los cuales deben estar en un diccionario de la misma estructura que el ejercicio anterior.

# Se debe poder usar de la siguiente forma:

# cumple = {"nombre": "Cosme Fulanito", "fecha_nac": "06/12/2001"}
# agregar_cumple("archivo_cumples.json", cumple)
# Ayuda: primero leer el archivo, deserializarlo (se va a crear una lista), 
# luego agregar el nuevo "cumple" y volver a serializarlo 
# (para esto hay que borrar el archivo anterior o abrirlo con 'w' al guardar nuevamente).


def agrega_persona(ruta, cumple):
    """Con esta funcion vamos a tomar un archivo json lo vamos a desearizarlo agregamos una persona y serealizamos
     nuevamente agregando dicha persona"""
    import json
    with open(ruta) as archivo:
        personas = json.load(archivo)
        personas.append(cumple)
    with open(ruta, "w") as archivo:
        json.dump(personas, archivo)


ruta="C:/Python/JHermosilla/MODULO 4/TP4/archivo_cumples.json"
cumple = {"nombre": "Patricia Angel", "fecha_nac": "29-05-77"}
agrega_persona(ruta, cumple)