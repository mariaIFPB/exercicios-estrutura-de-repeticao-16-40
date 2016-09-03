"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""
qt = int(input("digite um valor: "))
cont = 0
sa = 0
for x in range(qt):
	#qa < 40
	qa = eval(input("digite um numero da sequencia menor que 40: "))
	if (qa <= 40):
		sa = sa + qa
		ma = sa/qt
	cont = cont +1
print("a soma é",sa)
print("a media de alunos é",ma)
