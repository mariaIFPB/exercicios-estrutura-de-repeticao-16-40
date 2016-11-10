"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
qt = int(input("digite um valor: "))
cont = 0
vt = 0
for x in range(qt):
	n = eval(input("digite um numero da sequencia : "))
	vt = vt + n
	vm = vt/qt
	cont = cont +1
print("a soma é",vt)
print("o valor médio gasto é",vm)
