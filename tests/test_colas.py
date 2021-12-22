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

    with open('tests/clientes.txt', 'r') as f:
        lineas = f.readlines()
    clientes = []

    for cliente in lineas:
        x = cliente.split(", ")
        x[2] = x[2].strip('\n')
        x[2] = x[2].strip(' ')
        clientes.append(Cliente(x[0], x[1], x[2]))

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


def test_tiempo_colas(mi_tienda):
    """
        En un caso real el rendimiento se valora de la siguiente forma:
            Bueno -> Si el tiempo de espera medio es inferior a 2 minutos.
            Medio -> Si el tiempo de espera medio es superior a 2 minutos
                     e inferior a 5 minutos.
            Malo -> Si el tiempo de espera medio es superior a 5 minutos.
    """
    for i in range(2):
        mi_tienda._servicios.comienzo_atender_turno(mi_tienda._servicios.colas_disponibles['Pescaderia'], 290)
        mi_tienda._servicios.termino_atender_turno(mi_tienda._servicios.colas_disponibles['Pescaderia'], 300)


        mi_tienda._servicios.comienzo_atender_turno(mi_tienda._servicios.colas_disponibles['Carniceria'], 150)
        mi_tienda._servicios.termino_atender_turno(mi_tienda._servicios.colas_disponibles['Carniceria'], 300)

        mi_tienda._servicios.comienzo_atender_turno(mi_tienda._servicios.colas_disponibles['Fruteria'], 0)
        mi_tienda._servicios.termino_atender_turno(mi_tienda._servicios.colas_disponibles['Fruteria'], 400)

    mi_tienda.calcular_rendimiento_colas()

    assert_that(mi_tienda._servicios.rendimiento_colas['Pescaderia']).is_equal_to("Alto")
    assert_that(mi_tienda._servicios.rendimiento_colas['Carniceria']).is_equal_to("Medio")
    assert_that(mi_tienda._servicios.rendimiento_colas['Fruteria']).is_equal_to("Bajo")

def test_posicion_y_tiempo_espera_cliente(mi_tienda):

    mi_tienda._servicios.tiempo_medio_colas['Carniceria'] = 40
    # Aquí comprobamos la posición y tiempo de espera del cliente Nº6 que es el
    # siguiente en ser atendido en la cola de la carniceria. Por tanto el
    # tiempo de espera del cliente Nº6 es el tiempo medio de la cola
    # multiplicado por el número de clientes que tiene por delante, en
    # este caso al ser el siguiente en ser atendido es 0.
    posicion, tiempo = mi_tienda.posicion_y_tiempo_para_atender_a_cliente(mi_tienda._clientes[6]._turno)
    assert_that((posicion, tiempo)).is_equal_to((0, 0))
    
    # Aquí comprobamos la posición y tiempo de espera del cliente Nº7 que es el
    # segundo en la cola de la carniceria. Por tanto el
    # tiempo de espera del cliente Nº7 es el tiempo medio de la cola
    # multiplicado por el número de clientes que tiene por delante, en
    # este caso al ser el siguiente en ser atendido es 1.
    posicion, tiempo = mi_tienda.posicion_y_tiempo_para_atender_a_cliente(mi_tienda._clientes[7]._turno)
    assert_that((posicion, tiempo)).is_equal_to((1, 40))

    # Aquí comprobamos la posición y tiempo de espera del cliente Nº8 que es el
    # siguiente en ser atendido en la cola de la carniceria. Por tanto el
    # tiempo de espera del cliente Nº8 es el tiempo medio de la cola
    # multiplicado por el número de clientes que tiene por delante, en
    # este caso al ser el siguiente en ser atendido es 2.
    posicion, tiempo = mi_tienda.posicion_y_tiempo_para_atender_a_cliente(mi_tienda._clientes[8]._turno)
    assert_that((posicion, tiempo)).is_equal_to((2, 80))
