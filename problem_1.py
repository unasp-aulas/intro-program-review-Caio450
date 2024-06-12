def main():
    try:

       
        cargo = input("Digite o nível do cargo (junior, pleno, senior): ").strip().lower()
        salario = float(input("Digite o salário atual: "))
      
        if cargo == 'junior':
            aumento = 0.15
        elif cargo == 'pleno':
            aumento = 0.26
        elif cargo == 'senior':
            aumento = 0.34
        else:
            
            return -1

        
        novo_salario = salario * (1 + aumento)

  
        return novo_salario

    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido para o salário.")
        return -1


resultado = main()
if resultado != -1:
    print(f"O novo salário é: R$ {resultado:.2f}")
else:
    print("Cargo inválido.")

