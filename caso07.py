
cpf = input("informe seu CPF: ")

if len(cpf) != 11:
    print("CPF inválido, digite novamente.")
elif not cpf.isdigit():
    print("somente números são permitidos.")
else:
    print("tudo okkk")
