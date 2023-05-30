from Inscripciones import Inscripcion
class TallerCapacitacion:
    __idTaller: int
    __nombre: str
    __vacantes: int
    __montoInscripcion: int
    __inscripciones: list
    def __init__(self,id,nombre,vacantes,monto) -> None:
        self.__idTaller = id
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = monto
        self.__inscripciones = []
        pass

    def inscribirPersona(self, fecha,persona):
        inscripcion = Inscripcion(fecha, False,persona, self)
        self.__inscripciones.append(inscripcion)

    def getnombre(self):
        return self.__nombre
    
    def getvacantes(self):
        return self.__vacantes
    
    def setvacantes(self):
        self.__vacantes -= 1

    def getmonto(self):
        return self.__montoInscripcion
    
    def mostrartaller(self):
        print('\n')
        print('Nombre del Taller: {}, Id del taller: {}, Vacantes: {}, Monto a pagar: {}' .format(self.getnombre(),self.__idTaller,self.getvacantes(),self.getmonto()))
        print('Inscriptos:')
        for e in self.__inscripciones:
            e.mostrarinscripto()
        print('\n')

    def getinscripciones(self):
            return self.__inscripciones
    
    def getins(self):
        i = 0
        for e in self.__inscripciones:
            i +=1
        return i