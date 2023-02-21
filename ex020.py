# primeiro fiz assim:
'''import random
alunos = ["Pedro", "Luzia", "Ricardo", "Hannah"]
ordem_apresentação = random.shuffle(alunos)
print(f'Essa será a ordem de apresentação: )'''

# depois assim:
'''import random
alunos = []

while True:
    aluno = input("Digite os nomes dos alunos para sortear a ordem de apresentação (ao terminar de digitar os nomes "
                  "dos alunos que você quer sortear, pressione enter): ")
    if aluno == '':
        break
    alunos.append(aluno)

sorteio = random.shuffle(alunos)
print(f'Essa será a ordem de apresentação dos trabalhos: {alunos}')'''

# prof fez assim:

from random import shuffle
primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno =  input("Terceiro aluno: ")
quarto_aluno =  input("Quarto aluno: ")
alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(alunos)
print(f"Essa é a ordem de apresentação: {alunos}.")