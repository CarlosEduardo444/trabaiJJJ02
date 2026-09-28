produto = input("Digite o nome do produto: ")
preco = input("Digite o preço: ")

if preco.strip() == "":
    print("Erro: o preço não foi informado.")
else:
    try:
        preco = float(preco)
        quantidade = int(input("Digite a quantidade: "))

        total = preco * quantidade

        print(f"Valor total: R$ {total:.2f}")

    except ValueError:
        print("Erro: digite um preço e uma quantidade válidos.")
