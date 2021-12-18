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

    def posicion_y_tiempo_para_atender_a_cliente(self, cliente):
        """
            Añadir un nuevo turno a la cola correspondiente pasando
            solo el tipo de turno.

            Parameters
            ----------
            cliente : Cliente
                Cliente al cual se va a consultar tiempo restante aproximado
                para ser atendido
            Raises
            ------
            ValueError
                Si el cliente pasado por parametro no es uno válido.
        """
        if cliente not in self._clientes:
            raise TypeError('El cliente no se encuentra entre los \
                             clientes de la tienda')

        if cliente.turno in self._servicios.colas_disponibles[cliente.turno.tipo_turno]:
            posicion = self._servicios.colas_disponibles[cliente.turno.tipo_turno].index(cliente.turno)
            if posicion == 0:
                tiempo = 0
            elif posicion == 1:
                tiempo = self._servicios.tiempo_medio_colas[cliente.turno.tipo_turno]
            else:
                tiempo = posicion * self._servicios.tiempo_medio_colas[cliente.turno.tipo_turno]

            return posicion, tiempo
        else:
            raise TypeError('El turno del cliente no existe en esa cola')

    def generar_turno_y_asignar_a_cliente(self, cliente, tipo_cola):
        """
            Genera turno y se lo asigna a cliente
        """
        enum.TiposTurnos.check_valid_enum(tipo_cola)
        id_nuevo_turno = len(self._servicios.colas_disponibles[tipo_cola]) + 1
        nuevo_turno = Turno(id_nuevo_turno, tipo_cola)
        self._servicios.colas_disponibles[tipo_cola].append(nuevo_turno)
        cliente.turno = nuevo_turno

