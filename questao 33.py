"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""
qt = eval(input("digite um valor: "))
maior = qt
menor = qt
soma = 0
for x in range(qt):
    num = eval(input("digite um valor: "))
    soma = soma + num
    if (num > maior):
        maior = num
    elif(num < menor):
         menor = num
media = soma/qt
print("maior valor :",maior)
print("menor valor: ",menor)
print("a media =",media)
