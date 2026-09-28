
nota = float(input("Digite a nota: "))

if nota >= 0 and nota < 6.0:
    print("Desempenho: Baixo")

elif nota >= 6.0 and nota < 8.0:
    print("Desempenho: Mediano")
elif nota >= 8.0 and nota <= 10.0:
    print("Desempenho: ótimo")

else:
    print("Nota inválida")
