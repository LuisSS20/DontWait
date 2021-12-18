from time import sleep
import pytest
import sys
import random
from assertpy import assert_that

sys.path.append('./')
sys.path.append('./src/')
from src.colas_disponibles import ColasDisponibles
from src.turno import Turno
from src.tienda import Tienda
from src.cliente import Cliente
from src.enum_tipo_cola import TiposTurnos


@pytest.fixture
def mis_clientes():
    clientes = []
    clientes.append(Cliente('Angel', 'angel@gmail.com', '02/09/1995'))
    clientes.append(Cliente('Daniel', 'daniel@gmail.com', '05/11/1995'))
    clientes.append(Cliente('Maria', 'maria@gmail.com', '20/10/1995'))
    clientes.append(Cliente('Ana', 'ana@gmail.com', '10/02/1995'))
    clientes.append(Cliente('Alonso', 'alonso@gmail.com', '31/05/1995'))
    clientes.append(Cliente('Natala', 'angel@gmail.com', '02/09/1995'))
    clientes.append(Cliente('Rosa', 'daniel@gmail.com', '05/11/1995'))
    clientes.append(Cliente('Adrian', 'maria@gmail.com', '20/10/1995'))
    clientes.append(Cliente('Javier', 'ana@gmail.com', '10/02/1995'))
    clientes.append(Cliente('Pedro', 'alonso@gmail.com', '31/05/1995'))
    clientes.append(Cliente('Juan', 'angel@gmail.com', '02/09/1995'))
    clientes.append(Cliente('Alberto', 'daniel@gmail.com', '05/11/1995'))
    clientes.append(Cliente('Lucia', 'maria@gmail.com', '20/10/1995'))
    clientes.append(Cliente('Estrella', 'ana@gmail.com', '10/02/1995'))
    clientes.append(Cliente('Carlos', 'alonso@gmail.com', '31/05/1995'))

    return clientes

@pytest.fixture
def mis_colas():
    cola = ColasDisponibles()
    for i in range(10):
        cola.aniadir_turno('Pescaderia')
        cola.aniadir_turno('Carniceria')
        cola.aniadir_turno('Fruteria')

    return cola

@pytest.fixture
def mi_tienda(mis_clientes):
    tienda = Tienda()
    tienda._clientes = mis_clientes
    for i in range(int(len(tienda._clientes)/2)):
        if i % 2 == 0:
            tienda.generar_turno_y_asignar_a_cliente(tienda._clientes[i], 'Pescaderia')
        else:
            tienda.generar_turno_y_asignar_a_cliente(tienda._clientes[i], 'Fruteria')
    
    for i in range(int(len(tienda._clientes)/2)-1, len(tienda._clientes)):
        tienda.generar_turno_y_asignar_a_cliente(tienda._clientes[i], 'Carniceria')

    return tienda


def test_constructor_ColasDisponibles():
    assert_that(ColasDisponibles())


def test_existen_colas(mis_colas):
    """
        Testeo que exista al menos un tipo de cola en una tienda
    """
    assert_that(mis_colas.colas_disponibles).is_not_empty()


def test_colas_no_vacias(mis_colas):
    """
        Testeo que exista al menos un tipo de cola en una tienda
    """
    for cola in mis_colas.colas_disponibles.keys():
        assert_that(cola).is_not_empty()


def test_tiempo_colas(mis_colas):
    """
        En un caso real el rendimiento se valora de la siguiente forma:
            Bueno -> Si el tiempo de espera medio es inferior a 2 minutos.
            Medio -> Si el tiempo de espera medio es superior a 2 minutos
                     e inferior a 5 minutos.
            Malo -> Si el tiempo de espera medio es superior a 5 minutos.

        Como no puedo hacer que el test dure tanto, multiplicaré los
        resultados por 10000
    """
    for i in range(5):
        mis_colas.comienzo_atender_turno(mis_colas.colas_disponibles['Pescaderia'])
        sleep(random.uniform(0, 0.004))
        mis_colas.termino_atender_turno(mis_colas.colas_disponibles['Pescaderia'])

        mis_colas.comienzo_atender_turno(mis_colas.colas_disponibles['Carniceria'])
        sleep(random.uniform(0.025, 0.03))
        mis_colas.termino_atender_turno(mis_colas.colas_disponibles['Carniceria'])

        mis_colas.comienzo_atender_turno(mis_colas.colas_disponibles['Fruteria'])
        sleep(random.uniform(0.03, 0.04))
        mis_colas.termino_atender_turno(mis_colas.colas_disponibles['Fruteria'])

    for tipo in mis_colas.tiempo_medio_colas.keys():
        mis_colas.tiempo_medio_colas[tipo] *= 10000

    mis_colas.calcular_rendimiento_colas()

    assert_that(mis_colas.rendimiento_colas['Pescaderia']).is_equal_to("Alto")
    assert_that(mis_colas.rendimiento_colas['Carniceria']).is_equal_to("Medio")
    assert_that(mis_colas.rendimiento_colas['Fruteria']).is_equal_to("Bajo")

def test_posicion_y_tiempo_espera_cliente(mi_tienda):
    """
        Como no puedo hacer que el test dure tanto, multiplicaré los
        tiempos por 100
    """
    mi_tienda._servicios.comienzo_atender_turno(mi_tienda._servicios.colas_disponibles['Pescaderia'])
    sleep(0.04)
    mi_tienda._servicios.termino_atender_turno(mi_tienda._servicios.colas_disponibles['Pescaderia'])

    for i in range(2):
        mi_tienda._servicios.comienzo_atender_turno(mi_tienda._servicios.colas_disponibles['Fruteria'])
        sleep(0.04)
        mi_tienda._servicios.termino_atender_turno(mi_tienda._servicios.colas_disponibles['Fruteria'])

    for i in range(2):
        mi_tienda._servicios.comienzo_atender_turno(mi_tienda._servicios.colas_disponibles['Carniceria'])
        sleep(0.4)
        mi_tienda._servicios.termino_atender_turno(mi_tienda._servicios.colas_disponibles['Carniceria'])

    for tipo in mi_tienda._servicios.tiempo_medio_colas.keys():
        mi_tienda._servicios.tiempo_medio_colas[tipo] *= 100

    # Aquí comprobamos la posición y tiempo de espera del cliente Nº2 que tambien debería de ser
    # el Nº2 de la cola de la pescaderia ya que de los 3 turnos iniciales se ha atendido ya
    # a un cliente. Por tanto el tiempo de espera del cliente Nº2 es el tiempo medio de
    # la cola de pescadería multiplicado por el número de clientes que tiene por delante (1)
    posicion, tiempo = mi_tienda.posicion_y_tiempo_para_atender_a_cliente(mi_tienda._clientes[2])
    # Redondeo el tiempo para pasar test, ya que al variar milisegundos sería imposible pasar el test
    assert_that((posicion, round(tiempo))).is_equal_to((1, 4))

    # Aquí comprobamos la posición y tiempo de espera del cliente Nº1 que tambien debería de ser
    # el Nº1 de la cola de la fruteria ya que de los 3 turnos iniciales se han atendido ya
    # a dos clientes. Por tanto el tiempo de espera del cliente Nº3 es el tiempo medio de
    # la cola de fruteria multiplicado por el número de clientes que tiene por delante (0)
    posicion, tiempo = mi_tienda.posicion_y_tiempo_para_atender_a_cliente(mi_tienda._clientes[1])
    # Redondeo el tiempo para pasar test, ya que al variar milisegundos sería imposible pasar el test
    assert_that((posicion, round(tiempo))).is_equal_to((0, 0))

    # Aquí comprobamos la posición y tiempo de espera del cliente Nº12 que debería de ser
    # el Nº7 de la cola de la carniceria ya que de los 9 turnos iniciales se han atendido ya
    # a dos clientes. Por tanto el tiempo de espera del cliente Nº12 es el tiempo medio de
    # la cola de fruteria multiplicado por el número de clientes que tiene por delante (6)
    posicion, tiempo = mi_tienda.posicion_y_tiempo_para_atender_a_cliente(mi_tienda._clientes[12])
    # Redondeo el tiempo para pasar test, ya que al variar milisegundos sería imposible pasar el test
    assert_that((posicion, round(tiempo))).is_equal_to((6, 240))
