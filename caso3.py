aluno = []

while True:
    print("\n1. Armazenar aluno \n2. Consultar aluno \n")
    
    try:
        escolha = int(input("Você deseja armazenar ou consultar um anjinho? "))
        
        if escolha == 1:
            nome = str(input("Digite nome do aluno que você deseja armazenar: "))
            aluno.append(nome)
            
            id_aut = len(aluno)
            print(f"Armazenado com sucesso meu jovem! Id é {id_aut}")
            
        elif escolha == 2:
            id = int(input("Informe o id do aluno que você quer: "))
            
            if id <= 0:
                print("Id inexistente rapazzz")
            elif (id - 1) >= len(aluno):
                print("Sem alunos registrados nesse id amore!")
            else:
                print(f"O anjinho na posição {id} é {aluno[id - 1]}")
            
        else:
            print("Opção inválida!")
            break
            
    except ValueError:
        print("Error! Digite só número abençoado")
