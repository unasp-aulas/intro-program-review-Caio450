def main():
    while True:
        try:
           
            x = int(input("Digite um número (ou 0 para sair): "))

            if x == 0:
                print("Fim")
                break
      
            if x < 0:
                print("Por favor, insira um número positivo.")
                continue
          
            soma = 0

            for numero in range(1, x + 1):
                soma += numero
           
            print(f"A soma de todos os números da sequência até {x} é: {soma}")

        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro válido.")


main()
