"""Este modulo se encarga de gestionar la tienda"""

import time
from colas_disponibles import ColasDisponibles
import enum_tipo_cola as enum
from src.turno import Turno
from src.cliente import Cliente


class Tienda:
    """
    Clase que representa una tienda.
    """

    def __init__(self):
        """
            Constructor de la clase Tienda.
        """
        self._clientes = []
        self._servicios = ColasDisponibles()

    def aniadir_cliente(self, cliente: Cliente):
        """
            Añadir un nuevo turno a la cola correspondiente

            Parameters
            ----------
            cliente : Cliente
                Cliente nuevo que se añadirá a la cola de clientes esperando
        """
        self._clientes.append(cliente)

    def posicion_y_tiempo_para_atender_a_cliente(self, turno):
        """
            Añadir un nuevo turno a la cola correspondiente pasando
            solo el tipo de turno.

            Parameters
            ----------
            turno : Turno
                Turno al cual se va a consultar tiempo restante aproximado
                para ser atendido
            Raises
            ------
            ValueError
                Si el turno pasado por parametro no es uno válido.
        """

        if turno in self._servicios.colas_disponibles[turno.tipo_turno]:
            posicion = self._servicios.colas_disponibles[turno.tipo_turno].index(turno)
            if posicion == 0:
                tiempo = 0
            elif posicion == 1:
                tiempo = self._servicios.tiempo_medio_colas[turno.tipo_turno]
            else:
                tiempo = posicion * self._servicios.tiempo_medio_colas[turno.tipo_turno]

            return posicion, tiempo
        else:
            raise TypeError('El turno no es válido')

    def generar_turno_y_asignar_a_cliente(self, cliente, tipo_cola):
        """
            Genera turno y se lo asigna a cliente
        """
        enum.TiposTurnos.check_valid_enum(tipo_cola)
        id_nuevo_turno = len(self._servicios.colas_disponibles[tipo_cola]) + 1
        nuevo_turno = Turno(id_nuevo_turno, tipo_cola)
        self._servicios.colas_disponibles[tipo_cola].append(nuevo_turno)
        cliente.turno = nuevo_turno

    def calcular_rendimiento_colas(self):
        """
            Se calcula el rendimiento de cada cola y se almacena
            en rendimiento_colas.
        """
        for tipo in self._servicios.tiempo_medio_colas.keys():
            if self._servicios.tiempo_medio_colas[tipo] > 300.0:
                self._servicios.rendimiento_colas[tipo] = "Bajo"
            elif self._servicios.tiempo_medio_colas[tipo] < 120.0:
                self._servicios.rendimiento_colas[tipo] = "Alto"
            else:
                self._servicios.rendimiento_colas[tipo] = "Medio"

