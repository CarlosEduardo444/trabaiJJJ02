
SENHA_CORRETA = "Escola@2026"
MAX_TENTATIVAS = 3

for tentativa in range(1, MAX_TENTATIVAS + 1):
    senha = input(f"Senha (tentativa {tentativa}/{MAX_TENTATIVAS}): ")
    if senha == SENHA_CORRETA:
        print("Acesso liberado!")
        break
    print("Senha incorreta.")
else:
    print("Número máximo de tentativas excedido. Acesso bloqueado.")
