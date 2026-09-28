idade = int(input("Informe a idade do aluno: "))
curso = input("Informe o curso: ")
ano = int(input("Informe o ano: "))

# Verifica se os dados são válidos
if idade <= 0:
    print("Erro: idade inválida!")

elif curso.strip() == "":
    print("Erro: o curso não pode ficar vazio!")

elif ano < 2020 or ano > 2026:
    print("Erro: ano inválido!")

else:
    print("Cadastro realizado com sucesso!")
