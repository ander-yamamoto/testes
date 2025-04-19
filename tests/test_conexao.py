# tests/test_conexao.py
import pytest
from beings.conexao import ConexaoSimulada

# Fixture com setup e teardown
@pytest.fixture
def conexao():
    conexao = ConexaoSimulada()
    conexao.conectar()          # 🔧 Setup
    yield conexao               # fornece a instância pro teste
    conexao.desconectar()       # 🧹 Teardown

# Teste usando a fixture
def test_conexao_ativa(conexao):
    assert conexao.ativa == True