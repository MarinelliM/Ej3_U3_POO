import numpy as np
from Inscripciones import Inscripcion
class ManejaInscripcion:
    __dimension: int
    __cantidad: int
    __inscripciones: object
    __incremento = 5

    def __init__(self,dimension = 10) -> None:
        self.__inscripciones = np.array(dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        pass

    def agregarinscripciones(self,inscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscripciones = np.resize(self.__inscripciones, self.__dimension)
        self.__inscripciones[self.__cantidad] = inscripcion
        self.__cantidad += 1

    def setdimension(self, dimension):
        self.__dimension = dimension
        self.__inscripciones = np.resize(self.__inscripciones, dimension)

    def mostrar(self):
        for e in self.__inscripciones:
            e.mostrarinscripto()
