"""
questao 36
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário.
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""
num = eval(input("digite um valor: "))
valor_inicial = eval(input("digite um valor inicial: "))
valor_final = eval(input("digite um valor final: ")) 
for x in range(valor_inicial,valor_final):
	if (valor_final > valor_inicial):
		valor_inicial += 1
		print(num," x ",valor_inicial, "=" ,num*valor_inicial)
if (valor_final < valor_inicial):
	print("inválido")
