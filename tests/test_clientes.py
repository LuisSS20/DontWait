import pytest
import sys
from assertpy import assert_that

sys.path.append('./')
sys.path.append('./src/')
from src.cliente import Cliente
from src.tienda import Tienda
from src.turno import Turno
from src.enum_tipo_cola import TiposTurnos


@pytest.fixture
def mi_cliente():
    return Cliente('Angel', 'angel@gmail.com', '02/09/1995')

def test_constructor_cliente(mi_cliente):
    assert_that(mi_cliente)

def test_turno_none_una_vez_atendido(mi_cliente):
    tienda = Tienda()
    mi_cliente.turno = Turno('1', 'Pescaderia')
    tienda._clientes = [mi_cliente]
    tienda._servicios.aniadir_nuevo_turno_a_cola(mi_cliente.turno)
    tienda._servicios.comienzo_atender_turno(tienda._servicios.colas_disponibles['Pescaderia'], 290)
    tienda._servicios.termino_atender_turno(tienda._servicios.colas_disponibles['Pescaderia'], 290)
    tienda.poner_turnos_ya_atendidos_none()
    assert_that(mi_cliente._turno).is_equal_to(None)
