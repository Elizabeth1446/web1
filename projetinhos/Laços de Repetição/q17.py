fatorial=1
numero=int(input("Digite um numero positivo: "))
for L in range(1, numero+1):
    fatorial *= L
print(f"O fatorial de {numero} é {fatorial}")