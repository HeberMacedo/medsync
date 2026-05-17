import json
from unittest.mock import MagicMock, patch

import pytest
from main import MedSync


def test_adicionar_com_sucesso():
    app = MedSync()
    resultado = app.adicionar_medicamento("Aspirina", "08:00")
    assert "Sucesso" in resultado
    assert len(app.medicamentos) == 1


def test_erro_entrada_vazia():
    app = MedSync()
    with pytest.raises(ValueError):
        app.adicionar_medicamento("", "")


def test_lista_vazia_inicial():
    app = MedSync()
    assert app.listar_medicamentos() == "Nenhum medicamento agendado."


def test_obter_dica_saude_mockada():
    app = MedSync()
    sample_data = {"slip": {"advice": "Beba mais água todos os dias."}}
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(sample_data).encode("utf-8")
    mock_response.__enter__.return_value = mock_response

    with patch("main.urlopen", return_value=mock_response):
        resultado = app.obter_dica_saude()

    assert resultado == "Beba mais água todos os dias."


def test_obter_dica_saude_integracao():
    app = MedSync()
    dica = app.obter_dica_saude()
    assert isinstance(dica, str)
    assert dica != ""
    assert "Não foi possível" not in dica
