*Situação 12* — Lista com dados duplicados
Problema identificado:
A lista de estudantes pode conter nomes repetidos, sendo necessário identificar quais nomes aparecem mais de uma vez.

Algoritmo/estratégia:
Percorrer a lista de nomes e verificar quantas vezes cada nome aparece. Se um nome aparecer mais de uma vez, ele será armazenado em uma lista de duplicados. No final, os nomes repetidos serão exibidos.

Código Python:

nomes = ["Ana", "João", "Maria", "Ana", "Pedro", "João"]

duplicados = []

for nome in nomes:
    if nomes.count(nome) > 1 and nome not in duplicados:
        duplicados.append(nome)

if len(duplicados) > 0:
    print("Nomes repetidos:")
    for nome in duplicados:
        print(nome)
else:
    print("Não existem nomes repetidos.")

Casos de teste
Teste 1: Entrada: Ana, João e Maria. Resultado esperado: não existem nomes repetidos. Resultado obtido: não existem nomes repetidos. O teste passou.
Teste 2: Entrada: Ana, João e Ana. Resultado esperado: o nome Ana deve ser identificado como repetido. Resultado obtido: Ana foi identificada como repetida. O teste passou.
Teste 3: Entrada: Ana, João, Ana e João. Resultado esperado: os nomes Ana e João devem ser identificados como repetidos. Resultado obtido: Ana e João foram identificados como repetidos. O teste passou.

Conclusão:
O programa consegue percorrer a lista e identificar os nomes que aparecem mais de uma vez.


*Situação 19*
Problema identificado:
É necessário testar diferentes caminhos de execução de uma função que utiliza idade, renda e situação cadastral.

Algoritmo/estratégia:
A função verifica primeiro a idade. Caso o usuário seja maior de idade, verifica a renda. Depois verifica a situação do cadastro. Cada condição leva a um resultado diferente.

Código python

def verificar_usuario(idade, renda, cadastro):

    if idade < 18:
        return "Usuário menor de idade."

    elif renda < 1500:
        return "Usuário maior de idade, mas possui renda baixa."

    elif cadastro == "inativo":
        return "Usuário maior de idade, renda suficiente, mas cadastro inativo."

    else:
        return "Usuário aprovado."


# Teste 1
print("Teste 1:")
print(verificar_usuario(16, 2000, "ativo"))

# Teste 2
print("\nTeste 2:")
print(verificar_usuario(20, 1000, "ativo"))

# Teste 3
print("\nTeste 3:")
print(verificar_usuario(20, 2000, "inativo"))

# Teste 4
print("\nTeste 4:")
print(verificar_usuario(20, 2000, "ativo"))

Casos de teste:
Teste 1: Entrada: idade 16, renda 2000 e cadastro ativo. Resultado esperado: usuário menor de idade. Resultado obtido: usuário menor de idade. O teste passou.
Teste 2: Entrada: idade 20, renda 1000 e cadastro ativo. Resultado esperado: usuário maior de idade, mas possui renda baixa. Resultado obtido: usuário maior de idade, mas possui renda baixa. O teste passou.
Teste 3: Entrada: idade 20, renda 2000 e cadastro inativo. Resultado esperado: usuário maior de idade, renda suficiente, mas cadastro inativo. Resultado obtido: usuário maior de idade, renda suficiente, mas cadastro inativo. O teste passou.
Teste 4: Entrada: idade 20, renda 2000 e cadastro ativo. Resultado esperado: usuário aprovado. Resultado obtido: usuário aprovado. O teste passou.

Caminhos cobertos:
Usuário menor de 18 anos.
Usuário maior de idade com renda baixa.
Usuário maior de idade, renda suficiente e cadastro inativo.
Usuário aprovado.

Conclusão:
Os testes foram realizados para executar os diferentes caminhos condicionais existentes no programa. Dessa forma, foi possível verificar o comportamento da função em cada situação.
