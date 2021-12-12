"""Este modulo se encargar del enum de tipos de colas"""

from enum import Enum


class TiposTurnos(Enum):
    """
    Clase enum que representa los tipos de colas permitidos.
    """
    Pescaderia = 1
    Fruteria = 2
    Carniceria = 3
