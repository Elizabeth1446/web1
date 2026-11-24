num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num2 == 0:
  print("Erro: Não é possível dividir por zero!")
else:
  if num1 % num2 == 0:
    print(f"O número {num1} é múltiplo de {num2}.")
  else:
    print(f"O número {num1} NÃO é múltiplo de {num2}.")