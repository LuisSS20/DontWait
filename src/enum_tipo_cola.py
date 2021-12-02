from enum import Enum


"""Este modulo se encargar del enum de tipos de colas"""


class TiposTurnos(Enum):
    """
    Clase enum que representa los tipos de colas permitidos.
    """
    PESCADERIA = 1
    FRUTERIA = 2
    CARNICERIA = 3
