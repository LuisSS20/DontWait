"""Modulo de la clase turno"""


import enum_tipo_cola as enum


class Turno:
    """
    Clase que representa un turno.
    """

    def __init__(self, id, enum_cola):
        """
            Constructor de la clase Turno.

            Parameters
            ----------
            id : int
                Identificador de un turno.
            enum_cola : Enum
                Enum que indica a que cola pertenece el turno.
        """
        self.id_turno = id
        enum.TiposTurnos.check_valid_enum(enum_cola)
        self.enum_turno = enum_cola
        self.tiempo_turno = 0

    @property
    def id(self):
        """
            Getter del id del turno.
        """
        return self.id_turno

    @id.setter
    def id(self, id):
        """
            Setter del id del turno.
        """
        if not isinstance(id, int):
            raise TypeError('El id no es un entero')

        self.id_turno = id

    @property
    def tipo_turno(self):
        """
            Getter del tipo de turno.
        """
        return self.enum_turno

    @tipo_turno.setter
    def tipo_turno(self, tipo_turno):
        """
            Setter del id del turno.
        """
        if enum.TiposTurnos.check_valid_enum(tipo_turno):
            raise TypeError('El tipo de cola no es válido')

        self.enum_turno = tipo_turno
