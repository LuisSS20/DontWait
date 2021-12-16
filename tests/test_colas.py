from time import sleep
import pytest
import sys
import random
from assertpy import assert_that

sys.path.append('./')
sys.path.append('./src/')
from src.colas_disponibles import ColasDisponibles
from src.turno import Turno
from src.enum_tipo_cola import TiposTurnos


@pytest.fixture
def mis_colas():
    cola = ColasDisponibles()
    for i in range(10):
        cola.aniadir_turno('Pescaderia')
        cola.aniadir_turno('Carniceria')
        cola.aniadir_turno('Fruteria')

    return cola


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
        resultados por 1000
    """
    for i in range(5):
        mis_colas.comienzo_atender_turno(mis_colas.colas_disponibles['Pescaderia'])
        sleep(random.uniform(0, 0.004))
        mis_colas.termino_atender_turno(mis_colas.colas_disponibles['Pescaderia'])

        mis_colas.comienzo_atender_turno(mis_colas.colas_disponibles['Carniceria'])
        sleep(random.uniform(0.02, 0.03))
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
