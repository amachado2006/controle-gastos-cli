"""
Testes automatizados para o Controle de Gastos Pessoais.
"""

import os
import json
import pytest
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import gastos as app


# ---- Configuração dos testes (usa arquivo temporário) ----

@pytest.fixture(autouse=True)
def arquivo_temporario(tmp_path, monkeypatch):
    """Redireciona o arquivo de dados para uma pasta temporária em cada teste."""
    arquivo = tmp_path / "dados" / "gastos.json"
    monkeypatch.setattr(app, "ARQUIVO_DADOS", str(arquivo))


# ---- Testes de adição ----

def test_adicionar_gasto_valido():
    """Caminho feliz: adiciona um gasto com dados corretos."""
    gasto = app.adicionar_gasto("Mercado", 150.0, "Alimentação")
    assert gasto["descricao"] == "Mercado"
    assert gasto["valor"] == 150.0
    assert gasto["categoria"] == "Alimentação"


def test_adicionar_gasto_sem_descricao():
    """Entrada inválida: descrição vazia deve gerar erro."""
    with pytest.raises(ValueError, match="descrição não pode ser vazia"):
        app.adicionar_gasto("", 50.0, "Transporte")


def test_adicionar_gasto_valor_negativo():
    """Entrada inválida: valor negativo deve gerar erro."""
    with pytest.raises(ValueError, match="valor deve ser maior que zero"):
        app.adicionar_gasto("Ônibus", -10.0, "Transporte")


def test_adicionar_gasto_valor_zero():
    """Caso limite: valor zero também é inválido."""
    with pytest.raises(ValueError):
        app.adicionar_gasto("Algo", 0, "Outros")


# ---- Testes de listagem ----

def test_listar_gastos_vazio():
    """Lista vazia quando não há gastos."""
    resultado = app.listar_gastos()
    assert resultado == []


def test_listar_gastos_com_dados():
    """Lista retorna os gastos adicionados."""
    app.adicionar_gasto("Aluguel", 800.0, "Moradia")
    app.adicionar_gasto("Internet", 100.0, "Serviços")
    resultado = app.listar_gastos()
    assert len(resultado) == 2


# ---- Testes de total ----

def test_calcular_total_vazio():
    """Total é zero quando não há gastos."""
    assert app.calcular_total() == 0.0


def test_calcular_total_com_gastos():
    """Total soma corretamente os valores."""
    app.adicionar_gasto("Café", 10.0, "Alimentação")
    app.adicionar_gasto("Uber", 25.50, "Transporte")
    assert app.calcular_total() == 35.50


# ---- Testes de remoção ----

def test_remover_gasto_existente():
    """Remove um gasto que existe."""
    gasto = app.adicionar_gasto("Cinema", 30.0, "Lazer")
    resultado = app.remover_gasto(gasto["id"])
    assert resultado is True
    assert app.listar_gastos() == []


def test_remover_gasto_inexistente():
    """Tenta remover ID que não existe — deve retornar False."""
    resultado = app.remover_gasto(999)
    assert resultado is False
