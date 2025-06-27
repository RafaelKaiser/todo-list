def adicionar_tarefa(tarefas, descricao):
    """
    Adiciona uma nova tarefa à lista.
    Uma tarefa é um dicionário com 'descricao', 'concluida' e 'prioridade'.
    """
    if descricao:  # Garantiremos para que a descrição não fique vazia
        # --- Adicionamos para que seja prioridade ---
        prioridade_input = input("Defina a prioridade (Alta, Média, Baixa - padrão: Baixa): ").strip().capitalize()
        if prioridade_input not in ["Alta", "Média", "Baixa"]:
            prioridade = "Baixa" 
            print("Prioridade inválida. Definindo como 'Baixa'.")
        else:
            prioridade = prioridade_input
        # --- Fim da Adição para Prioridade ---

        nova_tarefa = {
            "descricao": descricao,
            "concluida": False,
            "prioridade": prioridade # Adicionando o campo de prioridade
        }
        tarefas.append(nova_tarefa)
        print(f"\nTarefa '{descricao}' adicionada com sucesso (Prioridade: {prioridade})!")
    else:
        print("\nA descrição da tarefa não pode ser vazia.")

def listar_tarefas(tarefas):
    """Lista todas as tarefas, mostrando o status (concluída ou pendente) e prioridade."""
    print("\n--- Sua Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa na lista. Adicione uma!")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluida!" if tarefa["concluida"] else "Pendente!"
            print(f"{i + 1}. {status} {tarefa['descricao']} (Prioridade: {tarefa['prioridade']})")
    print("--------------------------")

def marcar_como_concluida(tarefas, indice):
    """Marca uma tarefa como concluída com base no seu índice na lista."""
    # O índice do usuário começa em 1, mas o da lista em 0
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        if tarefas[indice_real]["concluida"]:
            print(f"\n ⚠️ A tarefa '{tarefas[indice_real]['descricao']}' já estava marcada como concluída.")
        else:
            tarefas[indice_real]["concluida"] = True
            print(f"\n ✅ Tarefa '{tarefas[indice_real]['descricao']}' marcada como concluída!")
    else: 
        print("\n ❌ Índice inválido. Por favor, escolha um número da lista.")

def remover_tarefa(tarefas, indice):
    """Remove uma tarefa da lista com base no seu índice."""
    indice_real = indice - 1
    if 0 <= indice_real < len(tarefas):
        tarefa_removida = tarefas.pop(indice_real)
        print(f"\n🗑️ Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    else:
        print("\n ❌ Índice inválido. Por favor, escolha um número da lista.")

# Função adicionada
def editar_tarefa(tarefas, indice, nova_descricao):
    """Edita a descrição de uma tarefa existente com base no seu índice."""
    indice_real = indice - 1 
    if 0 <= indice_real < len(tarefas):
        tarefa_antiga_descricao = tarefas[indice_real]["descricao"]
        tarefas[indice_real]["descricao"] = nova_descricao
        print(f"\n Descrição da tarefa '{tarefa_antiga_descricao}' atualizada para '{nova_descricao}'!")
    else:
        print("\n Índice inválido. Por favor, escolha um número válido da lista.")

# Adicionei a linha "5"
def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Editar Descrição da Tarefa") 
    print("0. Sair")

def main():
    # ... (código existente antes do while True) ...
    lista_de_tarefas = [] # Exemplo, mantenha a sua lista_de_tarefas existente

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(lista_de_tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(lista_de_tarefas)
        elif escolha == '3':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para marcar como concluída: "))
                marcar_como_concluida(lista_de_tarefas, indice)
            except ValueError:
                print("\n Entrada inválida. Por favor, digite um número.")
        elif escolha == '4':
            listar_tarefas(lista_de_tarefas)
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                remover_tarefa(lista_de_tarefas, indice)
            except ValueError:
                print("\n Entrada inválida. Por favor, digite um número.")
        # --- Adição MAIS SIMPLIFICADA para Editar Descrição ---
        elif escolha == '5':
            listar_tarefas(lista_de_tarefas) # Mostra as tarefas
            if not lista_de_tarefas:
                print("Nenhuma tarefa para editar.")
                continue # Volta para o início do loop

            try:
                indice = int(input("Digite o NÚMERO da tarefa que deseja editar: "))
                nova_descricao = input("Digite a NOVA descrição para a tarefa: ").strip() # .strip() remove espaços extras
                
                if nova_descricao:
                    editar_tarefa(lista_de_tarefas, indice, nova_descricao) # A função editar_tarefa já valida o índice
                else:
                    print("\n A nova descrição não pode ser vazia.")
            except ValueError:
                print("\n Entrada inválida. Por favor, digite um número.")
        # --- Fim da Adição MAIS SIMPLIFICADA ---
        elif escolha == '0':
            print("\nObrigado por usar o Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("\n Opção inválida. Por favor, tente novamente.")

# Garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()