soma=0
while True:
    try:
        x = int(input("digite um numero(ou 0 para sair)"))
        if x == 0:
            print("fim")
            break
        soma += x
        print(f"a soma de todos os numeros e:{soma}")
    except ValueError:
        print("valor invalido")