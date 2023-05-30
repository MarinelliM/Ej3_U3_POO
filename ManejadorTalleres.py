import numpy as np
from Talleres import TallerCapacitacion
import csv
class ManejaTaller:
    __dimension: int
    __actual = 0
    __talleres: object
    def __init__(self, dimension=10):
        self.__talleres = np.empty(dimension, dtype=TallerCapacitacion)
        self.__dimension=dimension
        self.__cantidad=0

    def agregarTaller(self, unTaller):
        self.__talleres[self.__actual]=unTaller
        self.__actual+=1

    def initmt(self):
        with open('Talleres.csv','r',encoding='utf8') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader)
            bandera = False
            for fila in reader:
                if bandera == False:
                    bandera = True
                    dimension = int(fila[0])
                    self.setdimension(dimension)
                else:
                    idtaller = int(fila[0])
                    nombre = str(fila[1])
                    vacante = int(fila[2])
                    monto = int(fila[3])
                    taller = TallerCapacitacion(idtaller,nombre,vacante,monto)
                    self.agregarTaller(taller)
    
    def mostrar(self):
        for e in self.__talleres:
            e.mostrartaller()

    def agregarinscripcion(self, taller,fecha, persona):
        i = 0
        while i < len(self.__talleres):
            if taller == self.__talleres[i].getnombre():
                if self.__talleres[i].getvacantes() > 0:
                    self.__talleres[i].setvacantes()
                    self.__talleres[i].inscribirPersona(fecha,persona)
                    i = len(self.__talleres)
                else: print('No se encuentran vacantes para el taller')
            else: i+=1

    def setdimension(self,dimension):
        self.__dimension = dimension
        self.__talleres = np.resize(self.__talleres, self.__dimension)

    def obtenerdi(self):
       dimension = 0
       for e in self.__talleres:
           dimension += e.getins()
       return dimension
    
    def obtinscripciones(self):
        inscripciones = []
        for e in self.__talleres:
            a = e.getinscripciones()
            inscripciones.append(a)
        return inscripciones
