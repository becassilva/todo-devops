import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import adicionar_tarefa, listar_tarefas, concluir_tarefa


def setup_function():
    tarefas = listar_tarefas()
    tarefas.clear()


def test_adicionar_tarefa():
    adicionar_tarefa("Estudar DevOps")

    assert len(listar_tarefas()) == 1
    assert listar_tarefas()[0]["descricao"] == "Estudar DevOps"
    assert listar_tarefas()[0]["concluida"] is False


def test_concluir_tarefa():
    adicionar_tarefa("Estudar Docker")

    resultado = concluir_tarefa(0)

    assert resultado is True
    assert listar_tarefas()[0]["concluida"] is True


def test_concluir_tarefa_inexistente():
    resultado = concluir_tarefa(0)

    assert resultado is False
    