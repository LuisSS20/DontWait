"""Modulo de la clase cliente"""


import re
from datetime import date, datetime
from src.turno import Turno


class Cliente:
    """
    Clase que representa un cliente.
    """

    def __init__(self, nombre, correo, fechaNac):
        """
            Constructor de la clase Cliente.

            Parameters
            ----------
            nombre : String
                Nombre del cliente.
            correo : String
                Correo del cliente.
            fechaNac : date
                Fecha de nacimiento del cliente.

            Raises
            ------
            ValueError
                Si el correo pasado no es uno válido.
        """
        self._nombre = nombre
        self.check_email(correo)
        self._correo = correo
        self.check_fecha(fechaNac)
        self._fechaNac = fechaNac
        self._turno = None

    def check_email(self, correo):
        """
            Comprobar sintaxis válida de correo.

            Parameters
            ----------
            correo : String
                Correo electronico el cual va a ser comprobado.

            Raises
            ------
            ValueError
                Si el correo pasado no es uno válido.
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, correo):
            raise TypeError('El correo introducido no es válido')

    def check_fecha(self, fecha):
        """
            Comprobar fecha válida.

            Parameters
            ----------
            fecha : String
                Fecha la cual va a ser comprobado.

            Raises
            ------
            ValueError
                Si la fecha pasada no es una válida.
        """
        if not datetime.strptime(fecha, '%d/%m/%Y'):
            raise TypeError('El formato de la fecha debe ser dd/mm/aa')

    @property
    def nombre(self):
        """
            Getter del nombre del cliente
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nom):
        """
            Setter del nombre del cliente
        """
        self._nombre = nom

    @property
    def correo(self):
        """
            Getter del correo del cliente
        """
        return self._correo

    @correo.setter
    def correo(self, mail):
        """
            Setter del nombre del cliente
        """
        if self.check_email(mail):
            self._correo = mail

    @property
    def turno(self):
        """
            Getter del turno del cliente
        """
        if not self._turno:
            raise TypeError('El cliente no tiene un turno asociado')
        return self._turno.id

    @turno.setter
    def turno(self, turn):
        """
            Setter del nombre del cliente
        """
        self._turno = Turno(turn.id, turn.tipo_turno)
