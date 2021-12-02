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
        self.id = id
        self._check_valid_cola(enum_cola)
        self.tipo_cola = enum_cola

    def _check_valid_enum(self, enum_cola):
        """
            Validar el tipo de cola que se le esta pasando al enum.

            Parameters
            ----------
            enum_cola : Enum
                Enum que indica a que cola pertenece el turno.
            Raises
            ------
            ValueError
                Si el enum pasado por no es uno válido.
        """
        if enum_cola not in enum.TiposTurnos:
            raise TypeError('El tipo de cola no es válido')
