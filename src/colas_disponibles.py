import enum_tipo_cola as enum


class Turnos:
    """
    Clase que representa las colas disponibles en una tienda.
    """

    def __init__(self, colas_disponibles=None):
        """
            Constructor de la clase Turnos.

            Parameters
            ----------
            turnos_disponibles : dic{'Enum': list[]}
                Diccionario que almacena los turnos, la clave es el tipo de
                cola y el valor sera una lista con los turnos de dicho tipo.

            Raises
            ------
            ValueError
                Si el enum pasado por no es uno válido.
        """
        if turnos_disponibles != None:
            for cola in turnos_disponibles:
                self._check_valid_cola(cola)
        else:
            self.turnos_disponibles

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
