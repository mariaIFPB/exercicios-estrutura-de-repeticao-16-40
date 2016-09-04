"""
questao 21
Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
a = 2
b= "v"
num = int(input(" digite um valor: "))
while ((b== "v") and (a <num)):
    if((num %a) == 0):
        b ="f"
    else:
        a += 1
if(b == "v"):
    print("o numero é primo.")
else:
    print("o numero não é primo.")
