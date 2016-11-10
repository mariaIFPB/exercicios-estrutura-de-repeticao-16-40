"""
questao 20
Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
"""
n = eval(input("digite n: "))
prod = n
cont = n-1
while (n <16 and n >0):
	n = eval(input("digite n: "))
	if (n <16 and n >0):
		while (cont > 1):
			prod = prod*cont
			cont = cont - 1
		print(n,"! = ",prod)
else:
	print("numero invalido")
