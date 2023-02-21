# eu fiz assim:
import random
alunos = ["Pedro", "Luzia", "Ricardo", "Hannah"]
sorteio = random.choice(alunos)
print(f'Parabéns, {sorteio}! Você foi sorteade para apagar o quadro!')

# depois eu fiz assim:
import random
alunos = []
while True:
    aluno = input("Digite os nomes dos alunos que serão sorteados para apagar o quadro (pressione enter para "
                   "encerrar): ")
    if aluno == '':
        break
    alunos.append(aluno)
print(alunos)
sorteio = random.choice(alunos)
print(f'Parabéns, {sorteio}! Você foi sorteade para apagar o quadro!')

# o prof. fez assim:
import random
primeiro_aluno = input("Digite o nome do primeiro aluno: ")
segundo_aluno = input("Digite o nome do segundo aluno: ")
terceiro_aluno = input("Digite o nome do terceiro aluno: ")
quarto_aluno = input("Digite o nome do quarto aluno: ")
alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
sorteio = random.choice(alunos)
print(f'Alune sorteade: {sorteio}')