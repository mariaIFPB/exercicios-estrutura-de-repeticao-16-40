"""
questao 18
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""
num = eval(input("digite um valor: "))
maior = num
menor = num
cont = 0
soma = 0
for x in range(num):
    num = eval(input("digite um valor: "))
    soma = soma + num
    if (num > maior):
        maior = num
    elif(num < menor):
         menor = num
print("soma =",soma)
print("maior valor :",maior)
print("menor valor: ",menor)
