
#questao 19

num = eval(input("digite um valor: "))
maior = num
menor = num
cont = 0
soma = 0
if (num >=0 and num <= 1000):
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
else:
    print("numero invalido")
