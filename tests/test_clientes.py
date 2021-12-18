import pytest
import sys
from assertpy import assert_that

sys.path.append('./')
sys.path.append('./src/')
from src.cliente import Cliente
from src.turno import Turno
from src.enum_tipo_cola import TiposTurnos


@pytest.fixture
def mi_cliente():
    return Cliente('Angel', 'angel@gmail.com', '02/09/1995')

@pytest.fixture
def mi_turno():
    return Turno('1', 'Pescaderia')

def test_constructor_cliente(mi_cliente):
    assert_that(mi_cliente)

def test_get_id_turno_cliente(mi_cliente, mi_turno):
    mi_cliente.turno = mi_turno
    assert_that(mi_cliente.turno.id).is_equal_to('1')
