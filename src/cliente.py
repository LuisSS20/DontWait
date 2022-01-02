"""Modulo de la clase cliente"""


import re
from datetime import date, datetime
from src.turno import Turno


class Cliente:
    """
    Clase que representa un cliente.
    """

    def __init__(self, nombre):
        """
            Constructor de la clase Cliente.

            Parameters
            ----------
            nombre : String
                Nombre del cliente.
        """
        self._nombre = nombre
        self._turno = None


    @property
    def turno(self):
        """
            Getter del turno del cliente
        """
        if not self._turno:
            raise TypeError('El cliente no tiene un turno asociado')
        return self._turno

    @turno.setter
    def turno(self, turn):
        """
            Setter del turno del cliente
        """
        self._turno = turn

    def turno_atendido(self):
        """
        Una vez se ha atendido el turno del cliente, el turno se establece
        como nulo, hasta que pida otro de nuevo.
        """
        self._turno = None
