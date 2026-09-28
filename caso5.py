try: 
    nota = float(input("Digite a nota meu nobre: "))

    if nota < 0:
      print("Digite apenas números positivos cara!")
    elif nota > 10:
      print("Só se for o tanto que tu precisa para passar, digite apenas números de 0 a 10!")
    else:
       if nota >= 7:
        print("Aprovado!!!!")
       elif nota >= 5:
        print("Vai pra recuperação.")
       else:
        print("Reprovado KKKKKKKKKKKKKKKKKKKKK")


except ValueError:
  print("Digite apenas números inteligente.")
