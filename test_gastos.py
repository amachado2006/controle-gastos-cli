"""Testes automatizados do Controle de Gastos Pessoais."""

import pytest
import requests as req
from unittest.mock import patch, MagicMock
from gastos import (
    adicionar_gasto,
    calcular_total,
    remover_gasto,
    buscar_cotacao,
)


def test_adicionar_gasto_valido(tmp_path, monkeypatch):
    monkeypatch.setattr("gastos.ARQUIVO_DADOS", str(tmp_path / "gastos.json"))
    gasto = adicionar_gasto("Almoco", 25.50, "Alimentacao")
    assert gasto["descricao"] == "Almoco"
    assert gasto["valor"] == 25.50
    assert gasto["categoria"] == "Alimentacao"


def test_adicionar_gasto_descricao_vazia():
    with pytest.raises(ValueError, match="descri"):
        adicionar_gasto("", 10.0, "Outros")


def test_adicionar_gasto_valor_negativo():
    with pytest.raises(ValueError, match="valor deve ser maior que zero"):
        adicionar_gasto("Teste", -5.0, "Outros")


def test_calcular_total(tmp_path, monkeypatch):
    monkeypatch.setattr("gastos.ARQUIVO_DADOS", str(tmp_path / "gastos.json"))
    adicionar_gasto("Item 1", 10.0, "Teste")
    adicionar_gasto("Item 2", 20.0, "Teste")
    assert calcular_total() == 30.0


def test_remover_gasto(tmp_path, monkeypatch):
    monkeypatch.setattr("gastos.ARQUIVO_DADOS", str(tmp_path / "gastos.json"))
    adicionar_gasto("Remover este", 5.0, "Teste")
    assert remover_gasto(1) is True
    assert remover_gasto(999) is False


def test_buscar_cotacao_sucesso():
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = {
        "USDBRL": {"bid": "5.25"},
        "EURBRL": {"bid": "5.80"},
    }

    with patch("gastos.requests.get", return_value=mock_response) as mock_get:
        cotacoes = buscar_cotacao()

        mock_get.assert_called_once_with(
            "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL",
            timeout=5,
        )

        assert "USD" in cotacoes
        assert "EUR" in cotacoes
        assert cotacoes["USD"] == 5.25
        assert cotacoes["EUR"] == 5.80
        assert isinstance(cotacoes["USD"], float)
        assert isinstance(cotacoes["EUR"], float)


def test_buscar_cotacao_erro_conexao():
    with patch("gastos.requests.get", side_effect=req.exceptions.ConnectionError):
        with pytest.raises(req.exceptions.ConnectionError):
            buscar_cotacao()