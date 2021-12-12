import pytest
import sys
from assertpy import assert_that

sys.path.append('./')
sys.path.append('./src/')
from src.colas_disponibles import ColasDisponibles
from src.turno import Turno
from src.enum_tipo_cola import TiposTurnos


colas_vacias = ColasDisponibles()
colas_disp = {'Pescaderia': [1, 2, 3, 4, 5, 6],
              'Carniceria': [],
              'Fruteria': [1, 2, 3, 4, 5, 6]}


def test_constructor_ColasDisponibles():
    assert_that(ColasDisponibles(colas_disp))


colas = ColasDisponibles(colas_disp)


def test_colas_vacias():
    assert_that(colas_vacias.colas_disponibles).is_empty()


# def test_enum_valido():
#     for tipo in colas_disp:
#         assert_that(ColasDisponibles._check_valid_enum(tipo))