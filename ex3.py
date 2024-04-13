while True:
    try:
        valor = int(input("Digite um valor inteiro entre 1 e 10: "))
        if valor < 1 or valor > 10:
            print("Por favor, digite um valor entre 1 e 10.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"Tabuada do {valor}:")
for multiplicador in range(1, 11):
    resultado = valor * multiplicador
    print(f"{valor} x {multiplicador} = {resultado}")
