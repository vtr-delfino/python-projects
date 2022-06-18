x, y, z = 10, 20, 30

metodo = str(input("Digite o que deseja fazer: "))

def tabuada(x):
    i = 0
    while i < 10:
        i += 1
        print(f"{x:2} x {i:2} = {x * i}")

def calculadora():
    n1, n2 = float(input("Digite dois números (separados por espaço):"))
    operação = str(input("Digite a operação (sum, sub, div e mult):"))
    if operação == "sum":
        return n1 + n2
    elif operação == "sub":
        return n1 - n2
    elif operação == "div":
        return n1 / n2
    elif operação == "mult":
        return n1 * n2

if metodo == "Tabuada":
    tabuada(x)
elif metodo == "Calculadora":
    calculadora()
