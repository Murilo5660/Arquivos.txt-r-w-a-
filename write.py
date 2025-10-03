#Exercício 1:
with open("Meu_Diário.txt","w") as bloco:
    bloco.write("Hoje, 3 de outubre de 2025, elaborei uma atividade em código sobre arquivo.txt.\n")

print("Arquivo 'Meu_Diário.txt' criado com sucesso!")

#Exercício 2:
try:
    with open("Meu_Diário.txt","r") as bloco:
        conteudo = bloco.read()
        print (" --- Conteudo do Diario ---")
        print ( conteudo )
except FileNotFoundError:
    print("O arquivo Meu_Diário.txt  ainda não existe. Rode o exercicio 1 primeiro ")

#Exercício 3:
with open("Meu_Diário.txt","a") as bloco:
    bloco.write("Estou aprendendo a manipular arquivos e e muito util.\n")

print("Nova anotação no Meu Diário!")

#Exercício 4:
with open("tarefas.txt","w") as arquivo_tarefas:
    print("Por favor, digite 3 tarefas a serem feitas:")
    for i in range(3):
        tarefa = input(f"Tarefa {i+1}:")
        arquivo_tarefas . write ( tarefa + "\n")

print ("\ nLista de tarefas foi salva em ’tarefas .txt ’!")

#Exercício 5:
print (" --- Minha Lista de Tarefas ---")
try:
    with open (" tarefas .txt ", "r") as arquivo_tarefas :
        numero_tarefa = 1
        for tarefa in arquivo_tarefas :
            print ( f"{ numero_tarefa }. { tarefa . strip ()}")
            numero_tarefa += 1 
            numero_tarefa + 1
except FileNotFoundError :
    print (" Arquivo ’tarefas .txt ’ nao encontrado . Rode o exercicio 4 primeiro .")