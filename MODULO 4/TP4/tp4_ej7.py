# Ejercicio 7
# Definir una clase que maneje un archivo. El nombre (ruta) del archivo debe establecerse 
# al crear un objeto de la clase.

# La clase debe implementar:

# Un método que cree el archivo. Si el archivo ya existe lo sobrescribe. 
# Opcionalmente puede recibir un parámetro con contenido para incluir en el archivo.
# Un método que permita agregar contenido al archivo.
# Un método que muestre todo el contenido del archivo por pantalla.
# Un método que devuelva la cantidad total de caracteres del archivo, sin contar el caracter \n. 
#     Extra: hacer que este sea el método especial __len__().
# Una propiedad de solo lectura que devuelva la cantidad total de líneas del archivo.
# Instancie un objeto de la clase y utilice sus métodos.

class ManejaArchivo:
    """Definimos una clase que contendra la estructura de un archivo de texto"""
    def __init__(self, nombre):
        self.nombre= nombre

    def creara(self, contenido= ""):
        """Este metodo sirve para crear un archivo txt y agregar contenido al mismo si es que le dieramos el parametro"""
        with open(self.nombre, "w") as marchivo:
            marchivo.write(contenido)

    def agrega(self, agregado):
        """"Con este metodo vamos a agregar una linea al archivo"""
        with open(self.nombre, "a") as marchivo:
            marchivo.write(agregado)

    def leer(self):
        """"Con este metodo vamos a leer y mostrar todo el contenido de un archivo"""
        with open(self.nombre, "r") as marchivo:
            completo= marchivo.read()
        return completo
    def __len__(self):
        """"Con este metodo vamos a contar la cantidad de caracteres que tiene el archivo sin incluir los saltos de linea"""
        with open(self.nombre, "r") as marchivo:
            todo= marchivo.read()
            salto= todo.count("\n")
            can= marchivo.tell()- salto
            return can
    @property
    def can_lin(self):
        """Con esta propiedad vamos a devolver la cantidad de lineas que tiene el archivo txt pero de solo lectura"""
        with open(self.nombre, "r") as marchivo:
            todo= marchivo.readlines()
            return len(todo)

archivo= "C:/Python/JHermosilla/MODULO 4/TP4/ejercicio_7.txt"
contenido= "osbreescribe no agrega Esto es solo una prueba de crear un archivo txt usando un metodo dentro de una clase"
agregado= "\n Seguimos agregando Agregamos una segunda linea al archivo txt, se agrega una nueva linea porque al principio tengo un salto de linea"
mi_archivo= ManejaArchivo(archivo)
#mi_archivo.creara(contenido)
mi_archivo.agrega(agregado)
print(mi_archivo.leer())
print(len(mi_archivo))
print(f"el archivo:  {archivo}  tiene  {mi_archivo.can_lin}  lineas")

