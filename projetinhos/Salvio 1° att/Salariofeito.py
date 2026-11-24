FUNCIONARIA = input("Digite o nome da funcionária: ")
SALARIO = float(input("Digite o salário da funcionária: "))
P_INSS = SALARIO * 0.11
P_SAUDE = SALARIO * 0.075
TODOS_DESCONTOS = int(P_INSS + P_SAUDE) 
SALARIO_LIQUIDO = int(SALARIO - P_INSS - P_SAUDE)

print ("Nome do Funcionario: ",FUNCIONARIA)
print ("Salario Bruto: $",SALARIO)
print ("Todos os Descontos: $", TODOS_DESCONTOS)
print ("Salario Liquido: $", SALARIO_LIQUIDO)