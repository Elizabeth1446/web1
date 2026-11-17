caracter= input("Digite um Caracteres: ")[0]
vogais = "aeiouAEIOU"

if caracter.isdigit():
    print(f"O caractere '{caracter}' é um NÚMERO.")
elif caracter.isalpha():
    if caracter in vogais: 
        print(f"O caractere '{caracter}' é uma Vogal.")
    else:
        print(f"O caractere '{caracter}' é uma Consoante.")
else:
    print(f"O caractere '{caracter}'é um Simbolo")