tarefas = []


def adicionar_tarefa(tarefa):
    tarefas.append({"descricao": tarefa, "concluida": False})


def listar_tarefas():
    return tarefas


def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        return True
    return False


if __name__ == "__main__":
    adicionar_tarefa("Estudar DevOps")
    adicionar_tarefa("Configurar Docker")

    concluir_tarefa(0)

    print("Tarefas:")
    for indice, tarefa in enumerate(listar_tarefas(), start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{indice}. {tarefa['descricao']} - {status}")