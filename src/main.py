tarefas = []


def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)


def listar_tarefas():
    return tarefas


if __name__ == "__main__":
    adicionar_tarefa("Estudar DevOps")
    adicionar_tarefa("Configurar Docker")

    print("Tarefas:")
    for tarefa in listar_tarefas():
        print(f"- {tarefa}")