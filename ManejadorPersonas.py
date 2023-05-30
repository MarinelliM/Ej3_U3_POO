from Personas import Persona
class ManejaPersonas:
    __lista: list

    def __init__(self) -> None:
        self.__lista = []
        pass

    def agregarpersona(self,mt):
        op = int(input('¿Desea inscribir a una persona? Coloque 1 para si y 0 para no:'))
        while op != 0:
            nombre = str(input('Ingrese el nombre a inscribir:'))
            direccion = str(input('Ingrese la direccion de la vivienda:'))
            dni = int(input('Ingrese el dni sin puntos:'))
            persona = Persona(nombre,direccion,dni)
            self.__lista.append(persona)
            taller = taller = str(input('Ingrese el nombre del taller a inscribirse:'))
            fecha = str(input('Ingrese la fecha del dia de hoy (Debe ser de la forma: dd/mm/aaaa):'))
            mt.agregarinscripcion(taller,fecha,persona)
            op = int(input('¿Desea inscribir a una persona? Coloque 1 para si y 0 para no:'))
        