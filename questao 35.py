"""
questao 35
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
"""
n = int(input("digite o valor de n: "))
cont = 0
i = 2
j = 1
while (i <= n) :
    while (j <= i):
        if ((i % j ) == 0):
            cont = cont +1
        j = j +1
    if(cont == 2):
        print(i)
    i = i + 1
    j = 1
    cont = 0
