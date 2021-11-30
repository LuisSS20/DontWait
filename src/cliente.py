from datetime import datetime

class Cliente():
    # Clase cliente
    nombre: str
    correo: str
    direccion: str


    def __init__(self, nombre,correo,direccion):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
