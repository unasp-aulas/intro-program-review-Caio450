def main():
    try:
      km = int(input("quantos km deseja percorrer?"))
      if km <= 200:
        preco = km * 0.5
      elif km <= 400:
        preco=km*0.45
      else:
        km>=400
        preco=km*0.30
      if km <= 200:
        preco=km*0.5
      print(f"o valor em km é:{preco:.2f}")
    except ValueError:
        print("Entrada inválida! Por favor, insira um valor numérico para a distância.")
main()