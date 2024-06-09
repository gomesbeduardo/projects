def adicionar_tarefa(tarefas, nome_tarefa):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Parâmetros:
    tarefas (list): Lista de tarefas existentes.
    nome_tarefa (str): Nome da tarefa a ser adicionada.

    Retorna:
    None
    """
    try:
        tarefa = {'nome': nome_tarefa, 'completada': False}
        tarefas.append(tarefa)
        print(f'Tarefa ({nome_tarefa}) adicionada com sucesso!')
    except Exception as e:
        print(f'Erro ao adicionar tarefa: {str(e)}')
    return

def listar_tarefas(tarefas):
    """
    Lista todas as tarefas existentes na lista de tarefas.

    Parâmetros:
    tarefas (list): Lista de tarefas existentes.

    Retorna:
    None
    """
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa ["completada"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome):
    """
    Atualiza o nome de uma tarefa na lista de tarefas.

    Parâmetros:
    tarefas (list): Lista de tarefas existentes.
    indice_tarefa (int): Índice da tarefa a ser atualizada (começa em 1).
    novo_nome (str): Novo nome da tarefa.

    Retorna:
    None
    """
    try:
        indice_tarefa_ajuste = indice_tarefa - 1
        if 0 <= indice_tarefa_ajuste < len(tarefas):
            tarefas[indice_tarefa_ajuste]['nome'] = novo_nome
            print(f'Tarefa {indice_tarefa} atualizada para ({novo_nome})')
        else:
            print(f'Tarefa {indice_tarefa} não existe!')
    except Exception as e:
        print(f'Erro ao atualizar tarefa: {str(e)}')
    return

def completar_tarefa(tarefas, indice_tarefa):
    """
    Marca uma tarefa como completada na lista de tarefas.

    Parâmetros:
    tarefas (list): Lista de tarefas existentes.
    indice_tarefa (int): Índice da tarefa a ser marcada como completada (começa em 1).

    Retorna:
    None
    """
    try:
        indice_tarefa_ajuste = indice_tarefa - 1
        if 0 <= indice_tarefa_ajuste < len(tarefas):
            tarefas[indice_tarefa_ajuste]['completada'] = True
            print(f'Tarefa {indice_tarefa} completada com sucesso!')
        else:
            print(f'Tarefa {indice_tarefa} não existe!')
    except Exception as e:
        print(f'Erro ao completar tarefa: {str(e)}')
    return

def deletar_tarefa(tarefas):
    """
    Remove todas as tarefas completadas da lista de tarefas.

    Parâmetros:
    tarefas (list): Lista de tarefas existentes.

    Retorna:
    None
    """
    try:
        indices_para_remover = [i for i, tarefa in enumerate(tarefas) if tarefa['completada']]
        for indice in reversed(indices_para_remover):
            del tarefas[indice]
        print(f'\n{len(indices_para_remover)} tarefas completadas foram deletadas.')
    except Exception as e:
        print(f'Erro ao deletar tarefas: {str(e)}')
    return

def get_valid_string_input(prompt, min_length=None, max_length=None):
    """
    Solicita ao usuário uma entrada de string válida, respeitando os limites de comprimento.

    Parâmetros:
    prompt (str): Mensagem a ser exibida ao usuário.
    min_length (int, optional): Comprimento mínimo da entrada.
    max_length (int, optional): Comprimento máximo da entrada.

    Retorna:
    str: Entrada de string válida.
    """
    while True:
        value = input(prompt)
        if min_length is not None and len(value) < min_length:
            print(f'Valor deve ter pelo menos {min_length} caracteres. Por favor, tente novamente.')
            continue
        if max_length is not None and len(value) > max_length:
            print(f'Valor deve ter no máximo {max_length} caracteres. Por favor, tente novamente.')
            continue
        return value
    return

def get_valid_integer_input(prompt, min_value=None, max_value=None):
    """
    Solicita ao usuário uma entrada de número inteiro válida, respeitando os limites de valor.

    Parâmetros:
    prompt (str): Mensagem a ser exibida ao usuário.
    min_value (int, optional): Valor mínimo da entrada.
    max_value (int, optional): Valor máximo da entrada.

    Retorna:
    int: Entrada de número inteiro válida.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f'Valor deve ser maior ou igual a {min_value}. Por favor, tente novamente.')
                continue
            if max_value is not None and value > max_value:
                print(f'Valor deve ser menor ou igual a {max_value}. Por favor, tente novamente.')
                continue
            return value
        except ValueError:
            print('Valor inválido. Por favor, tente novamente.')
    return

menu_options = {
    1: adicionar_tarefa,
    2: listar_tarefas,
    3: atualizar_tarefa,
    4: completar_tarefa,
    5: deletar_tarefa,
    6: lambda: print('Encerrando...')
}

tarefas = []

while True:
    print('\nMenu do Gerenciador de Lista de Tarefas:')
    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefa')
    print('3 - Atualizar Tarefa')
    print('4 - Completar Tarefa')
    print('5 - Deletar Tarefas Completadas')
    print('6 - Sair')

    opc = get_valid_integer_input('Digite sua escolha: ', min_value=1, max_value=6)

    if opc in menu_options:
        if opc == 1:
            nome_tarefa = get_valid_string_input('Digite o nome da tarefa: ', min_length=1, max_length=50)
            menu_options[opc](tarefas, nome_tarefa)
        elif opc == 2:
            if len(tarefas) > 0:
                listar_tarefas(tarefas)
            else:
                print("Não há tarefas disponíveis para serem listadas.")
        elif opc == 3:
            if len(tarefas) > 0:
                listar_tarefas(tarefas)
                indice_tarefa = get_valid_integer_input('Digite o número da tarefa: ', min_value=1, max_value=len(tarefas))
                nome_tarefa = get_valid_string_input('Digite o novo nome da tarefa: ', min_length=1, max_length=50)
                menu_options[opc](tarefas, indice_tarefa, nome_tarefa)
            else:
                print("Não há tarefas disponíveis para atualizar.")
        elif opc == 4:
            if len(tarefas) > 0:
                listar_tarefas(tarefas)
                indice_tarefa = get_valid_integer_input('Digite o número da tarefa: ', min_value=1, max_value=len(tarefas))
                completar_tarefa(tarefas, indice_tarefa)
            else:
                print("Não há tarefas disponíveis para completar.")
        elif opc == 5:
            deletar_tarefa(tarefas)
            listar_tarefas(tarefas)
        elif opc == 6:
            print("Encerrando...")
            break
        else:
            menu_options[opc]()
    else:
        print('Opção inválida. Por favor, tente novamente.')
