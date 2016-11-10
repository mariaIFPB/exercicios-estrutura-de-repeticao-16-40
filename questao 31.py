#questao 31
n = 1
total = 0
while (n > 0) :
    n = eval(input("sao quantos valores?"))
    for x in range(n):
        n = eval(input("digite o valor do produto: "))
        if (n==0):
            break
        total = total + n
    print("total : ",total)
    dinheiro = eval(input("qual o valor pago pelo cliente?"))
    troco = dinheiro - total
    print("troco : ",troco)
    n = eval(input("sao quantos valores?"))
