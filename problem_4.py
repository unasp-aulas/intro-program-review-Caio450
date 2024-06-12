
casa = float(input("Digite o valor da casa a comprar: R$ "))
salario = float(input("Digite o valor do salário: R$ "))
anos_pagar = float(input("Digite a quantidade de anos a pagar: "))

# Calcula o valor total a ser pago
total_pagar = casa * (1 + 0.05)

# Calcula o número total de meses a pagar
meses_pagar = anos_pagar * 12


prestacao_mensal = total_pagar / meses_pagar


limite_prestacao = salario * 0.3

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
else:
    print("Empréstimo negado. Valor da prestação excede 30% do salário.")
