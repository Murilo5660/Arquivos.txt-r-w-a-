# Exercício 1: Criar arquivo e escrever
with open("Meu_Diário.txt", "w") as bloco:
    bloco.write("Hoje, 3 de outubro de 2025, elaborei uma atividade em código sobre arquivo.txt.\n")

print("Arquivo 'Meu_Diário.txt' criado com sucesso!")


# Exercício 2: Ler o conteúdo do arquivo
try:
    with open("Meu_Diário.txt", "r") as bloco:
        conteudo = bloco.read()
        print(" --- Conteúdo do Diário ---")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo 'Meu_Diário.txt' ainda não existe. Rode o exercício 1 primeiro.")


# Exercício 3: Acrescentar informação ao arquivo
with open("Meu_Diário.txt", "a") as bloco:
    bloco.write("Estou aprendendo a manipular arquivos e é muito útil.\n")

print("Nova anotação no Meu Diário!")


# Exercício 4: Criar lista de tarefas
with open("tarefas.txt", "w") as arquivo_tarefas:
    print("Por favor, digite 3 tarefas a serem feitas:")
    for i in range(3):
        tarefa = input(f"Tarefa {i+1}: ")
        arquivo_tarefas.write(tarefa + "\n")

print("\nLista de tarefas foi salva em 'tarefas.txt'!")


# Exercício 5: Ler lista de tarefas
print(" --- Minha Lista de Tarefas ---")
try:
    with open("tarefas.txt", "r") as arquivo_tarefas:
        numero_tarefa = 1
        for tarefa in arquivo_tarefas:
            print(f"{numero_tarefa}. {tarefa.strip()}")
            numero_tarefa += 1
except FileNotFoundError:
    print("Arquivo 'tarefas.txt' não encontrado. Rode o exercício 4 primeiro.")
