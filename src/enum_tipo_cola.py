"""Este modulo se encargar del enum de tipos de colas"""

from enum import Enum


class TiposTurnos(Enum):
    """
    Clase enum que representa los tipos de colas permitidos.
    """
    Pescaderia = 1
    Fruteria = 2
    Carniceria = 3

    def check_valid_enum(enum_cola):
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
        if not hasattr(TiposTurnos, enum_cola):
            raise TypeError('El tipo de cola no es válido')
