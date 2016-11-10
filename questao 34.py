# 34
x = 2
y = "v"
num = int(input("digite um valor: "))
while ((y == "v") and (x < num)):
    if((num % x) == 0):
        y = "f"
    else:
        x = x + 1
if(y == "v"):
    print("o numero é primo")
else:
    print("o numero não é primo")
