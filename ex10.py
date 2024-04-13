# Lista fornecida
lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

contagem = {}

for numero in lista:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

# Encontrando o número que mais se repete
numero_mais_repetido = None
quantidade_mais_repetida = 0

for numero, quantidade in contagem.items():
    if quantidade > quantidade_mais_repetida:
        numero_mais_repetido = numero
        quantidade_mais_repetida = quantidade

print(f"O número que mais se repete é: {numero_mais_repetido}")
