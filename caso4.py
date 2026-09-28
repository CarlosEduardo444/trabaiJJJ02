#caso 4
preco = input("digite um preco:")
quantidade = input("vai levar quantos?")
try:
    preco = float(preco)
    quantidade = int(quantidade)
    total = preco * quantidade
    print(total)
except:
    print("isso não é um número bro")
