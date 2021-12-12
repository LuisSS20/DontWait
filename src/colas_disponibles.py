"""Este modulo se encarga de gestionar las colas de la tienda"""

import time
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
        self.colas_disponibles = {}
        self.tiempo_medio_colas = {}
        self.dict_turnos_atendidos = {}

        if colas_disp is not None:
            for cola in colas_disp:
                self._check_valid_enum(cola)
                if colas_disp[cola]:
                    self.tiempo_medio_colas[cola] = colas_disp[cola]
                else:
                    self.tiempo_medio_colas[cola] = []
            self.colas_disponibles = colas_disp

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
        if not hasattr(enum.TiposTurnos, enum_cola):
            raise TypeError('El tipo de cola no es válido')

    def comienzo_atender_turno(self, cola):
        """
            Se almacena la hora en la que se ha atendido el turno.

            Parameters
            ----------
            cola : list[Turno]
                Lista de turnos de la cual se coge el primer turno para
                atenderlo.
        """
        cola[0].tiempo_turno = time.time()

    def termino_atender_turno(self, cola):
        """
            Se elimina de la cola el turno que ha sido atendido.
            Se calcula de nuevo el tiempo medio.

            Parameters
            ----------
            cola : list[Turno]
                Lista de turnos de la cual se coge el primer turno para
                eliminarlo de la cola.
        """
        tiempo_final = time.time()
        cola[0].tiempo_turno = tiempo_final - cola[0].tiempo_turno
        # Almaceno el turno que ha sido atentido
        self.lista_turnos_atendidos.append(cola[0].copy())
        # Vuelvo a calcular el tiempo medio de espera
        self.calcular_tiempo_medio_por_turno(
                    self.dict_turnos_atendidos[cola[0].tipo_cola])
        # Saco el turno de la cola correspodiente
        cola.pop()

    def calcular_tiempo_medio_por_turno(self,
                                        lista_turnos_atendidos):
        """
            Se almacena la hora en la que se ha atendido el turno.

            Parameters
            ----------
            cola : list[Turno]
                Lista de turnos ya atendidos de la cual se extraen los tiempos
                que han tardado en atenderse cada turno.
        """
        sum_tiempo = 0
        for turno in lista_turnos_atendidos:
            sum_tiempo += turno.tiempo_turno

        # Agrego el tiempo medio en tiempo_medio_colas[tipo_cola]
        self.tiempo_medio_colas[lista_turnos_atendidos[0].tipo_cola] = sum_tiempo / len(lista_turnos_atendidos)
