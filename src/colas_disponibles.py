import enum_tipo_cola as enum
from src.turno import Turno


class ColasDisponibles:
    """
    Clase que representa las colas disponibles en una tienda.
    """

    def __init__(self, colas_disp=None):
        """
            Constructor de la clase Turnos.

            Parameters
            ----------
            turnos_disp : dic{'Enum': list[]}
                Diccionario que almacena los turnos, la clave es el tipo de
                cola y el valor sera una lista con los turnos de dicho tipo.

            Raises
            ------
            ValueError
                Si el enum pasado por no es uno válido.
        """
        if colas_disp is not None:
            for cola in colas_disp:
                self._check_valid_cola(cola)
            self.colas_disponibles = colas_disp
        else:
            self.colas_disponibles = {}

    def aniadir_nuevo_turno_a_cola(self, n_turno: Turno):
        """
            Añadir un nuevo turno a la cola correspondiente

            Parameters
            ----------
            n_turno : Turno
                Turno nuevo que se añadirá a la cola
            Raises
            ------
            ValueError
                Si el enum pasado por no es uno válido.
        """
        self._check_valid_enum(n_turno.tipo_cola)
        for turno in self.colas_disponibles[n_turno.tipo_cola]:
            turno.append(n_turno)

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
