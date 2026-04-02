import pytest
from main import MedSync

def test_adicionar_com_sucesso():
    app = MedSync()
    # Caso 1: Adicionando um remédio corretamente
    resultado = app.adicionar_medicamento("Aspirina", "08:00")
    assert "Sucesso" in resultado
    assert len(app.medicamentos) == 1

def test_erro_entrada_vazia():
    app = MedSync()
    # Caso 2: Tentando adicionar vazio (deve gerar erro)
    with pytest.raises(ValueError):
        app.adicionar_medicamento("", "")

def test_lista_vazia_inicial():
    app = MedSync()
    # Caso 3: Verificar se a lista começa vazia corretamente
    assert app.listar_medicamentos() == "Nenhum medicamento agendado."