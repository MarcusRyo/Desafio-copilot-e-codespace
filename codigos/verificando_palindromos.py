# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")

if verificar_palindromo(palavra):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
