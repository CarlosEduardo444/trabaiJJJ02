#caso 11
N = int(input("digite N"))
contador = 0
for numero in range(1, N + 1):
    if numero % 2 == 0:
        contador = contador + 1
        print(contador)
