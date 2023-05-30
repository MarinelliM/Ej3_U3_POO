class Persona:
    __nombre: str
    __direccion: str
    __dni: int

    def __init__(self,nombre,direccion,dni) -> None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
        pass

    def getnombre(self):
        return self.__nombre
    
    def getdireccion(self):
        return self.__direccion
    
    def getdni(self):
        return self.__dni
    
    def mostrar(self):
        return print('Nombre: {}, Direccion: {}, Dni: {}' .format(self.getnombre(),self.getdireccion(),self.getdni()))
    