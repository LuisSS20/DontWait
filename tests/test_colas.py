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


def test_constructor_ColasDisponibles():
    assert_that(ColasDisponibles())

colas = ColasDisponibles()

for i in range(10):
    colas.aniadir_turno('Pescaderia')
    colas.aniadir_turno('Carniceria')
    colas.aniadir_turno('Fruteria')


def test_existen_colas():
    """
        Testeo que exista al menos un tipo de cola en una tienda
    """
    assert_that(colas.colas_disponibles).is_not_empty()

def test_colas_no_vacias():
    """
        Testeo que exista al menos un tipo de cola en una tienda
    """
    for cola in colas.colas_disponibles.keys():
        assert_that(cola).is_not_empty()


def test_tiempo_colas():
    """
        En un caso real el rendimiento se valora de la siguiente forma:
            Bueno -> Si el tiempo de espera medio es inferior a 2 minutos.
            Medio -> Si el tiempo de espera medio es superior a 2 minutos
                     e inferior a 5 minutos.
            Malo -> Si el tiempo de espera medio es superior a 5 minutos.

        Como no puedo hacer que el test dure tanto, multiplicaré los
        resultados por 100
    """
    for i in range(5):
        colas.comienzo_atender_turno(colas.colas_disponibles['Pescaderia'])
        sleep(random.uniform(0, 1))
        colas.termino_atender_turno(colas.colas_disponibles['Pescaderia'])

        colas.comienzo_atender_turno(colas.colas_disponibles['Carniceria'])
        sleep(random.uniform(2, 3))
        colas.termino_atender_turno(colas.colas_disponibles['Carniceria'])

        colas.comienzo_atender_turno(colas.colas_disponibles['Fruteria'])
        sleep(random.uniform(3, 4))
        colas.termino_atender_turno(colas.colas_disponibles['Fruteria'])

        for tipo in colas.tiempo_medio_colas.keys():
            colas.tiempo_medio_colas[tipo] *= 100

        colas.calcular_rendimiento_colas()

        assert_that(colas.rendimiento_colas['Pescaderia']).is_equal_to("Alto")
        assert_that(colas.rendimiento_colas['Carniceria']).is_equal_to("Medio")
        assert_that(colas.rendimiento_colas['Fruteria']).is_equal_to("Bajo")

