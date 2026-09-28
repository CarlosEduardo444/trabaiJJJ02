
temperaturas = [25.5, 30.0, -2.0, 30.0, 18.3]

maior = temperaturas[0]
menor = temperaturas[0]
for t in temperaturas:
    if t > maior:
        maior = t
    if t < menor:
        menor = t

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
