try:
    idade = int(input("Qual sua idade? "))
    if idade >= 18:
       print("Liberado!")
    elif idade <= 0:
       print("Erro! Digite sua real idade.")
    else:
       print("Maioridade não atingida")

except ValueError:
    print("Digite apenas números")
