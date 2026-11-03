a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))
if (a < b + c) and (b < a + c) and (c < a + b):
    print("Podem tornar um triangulo!")

    if  a == b == c:
        print("Equilátero")
    elif  (a != b) and (b != c) and (a != c):
            print("É Escaleno")
    else:
        print("É Isósceles")
else:
    print("Não pode tornar um triangulo")
