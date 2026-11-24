numero=int(input("Digite o primeiro numero: "))

for L in range(1,10):
   numero=int(input("Digite os numeros: "))
   
   if numero > Maior:
      Maior=max
  
   if numero < Menor:
      Menor=min

print(f"/n O maior número digitado foi: {Maior}")
print(f"/n O menor número digitado foi: {Menor}")