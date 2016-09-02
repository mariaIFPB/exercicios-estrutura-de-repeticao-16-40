n = eval(input("digite um valor: "))
soma = 0
cont = 0
for x in range(n):
	s = eval(input("digite um numero da sequencia: "))
	if s > 0 :
		soma = soma + s 
	cont = cont + 1

print ("resultado é: ", soma)

me = soma / n
print(me)
