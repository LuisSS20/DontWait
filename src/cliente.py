from datetime import datetime

class Cliente():
    # Clase cliente
    nombre: str
    correo: str
    fechaNac: datetime
    turnoActual: datetime


    def __init__(self, nombre,correo,fechaNac):
        self.nombre = nombre
        self.correo = correo
        self.fechaNac = fechaNac


    def get_cliente(self):
        cliente = {"Nombre",self.nombre,
        "Correo",self.correo,
        "FechaNac",self.fechaNac}
        return cliente

    def set_nombre_cliente(self, nombre):
        self.nombre = nombre

    def set_fechaNac(self,fecha):
        self.fechaNac = fecha

    def set_correo(self,correo):
        self.correo = correo
