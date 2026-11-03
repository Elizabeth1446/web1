num = int(input("Digite um numero: "))
if num % 5 == 0 and num % 3 == 0:
    print(f"O numero {num} é Divisivel por ambos")
elif num % 3 == 0:
    print(f"O numero {num} é Divisivel por 3")
elif num % 5 == 0:
    print(f"O numero {num} é Divisivel por 5")
else:
    print(f"O numero {num} não é Divisivel")