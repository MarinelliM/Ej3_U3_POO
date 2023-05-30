from ManejadorTalleres import ManejaTaller
from ManejadorPersonas import ManejaPersonas
from ManeadorInscripciones import ManejaInscripcion
if __name__ == '__main__':
    manejadortalleres = ManejaTaller()
    manejadortalleres.initmt()
    manejadortalleres.mostrar()
    persona = ManejaPersonas()
    persona.agregarpersona(manejadortalleres)
    manejadortalleres.mostrar()
    manejadorinscripciones = ManejaInscripcion()
    a = input('ingresa valor:')
    dimension = manejadortalleres.obtenerdi()
    a = input('ingresa valor:')
    incripciones = manejadortalleres.obtinscripciones()
    manejadorinscripciones.setdimension(dimension)
    a = input('ingrese valor:')
    manejadorinscripciones.agregarinscripciones(incripciones)
    a = input('ingrese valor:')
    manejadorinscripciones.mostrar()
