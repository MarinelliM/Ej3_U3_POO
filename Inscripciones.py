class Inscripcion:
    __fechaInscripcion: str
    __pago: bool
    __person: object
    __taller: object

    # def __init__ (self, fecha, pago=False, person, taller) -> None:
    #     self.__fechaInscripcion = fecha
    #     self.__pago = pago
    #     self.__persona = person
    #     self.__taller = taller
    #     pass

    def __init__(self, fecha, pago, person, taller) -> None:
        self.__fechaInscripcion = fecha
        self.__pago = pago
        self.__person = person
        self.__taller = taller
        pass

    def getfecha(self):
        return self.__fechaInscripcion
    
    def getpersona(self):
        self.__person.mostrar()
    
    def mostrarinscripto(self):
        self.getpersona()
        print('Fecha de Inscripcion: {}, Pagado: {}' .format(self.getfecha(),self.__pago))
        print('\n')
        

    