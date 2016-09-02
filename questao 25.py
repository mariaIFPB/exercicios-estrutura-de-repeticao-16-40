"""
questao 25
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
#0 < jovem < 25 
#26 < adulta < 60
#idosa >= 61
n = int(input("digite o número de pessoas: "))
soma = 0
cont = 0
for x in range(n):
	s = eval(input("digite um numero da sequencia: "))
	if s > 0 :
		soma = soma + s 
	cont = cont + 1
print ("resultado é: ", soma)
me = soma/n 
print(me)
if(me <= 25 and me >= 0):
	print("jovem")
if(me <= 60 and me >= 26):
	print("adulta")
if(me > 60):
	print("idosa")
