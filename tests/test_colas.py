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
    for i in range(5):
        colas.comienzo_atender_turno(colas.colas_disponibles['Pescaderia'])
        sleep(random.uniform(4, 5))
        colas.termino_atender_turno(colas.colas_disponibles['Pescaderia'])

