8.Erro de lógica em média

Problema identificado: A fórmula da média está incorreta, provavelmente por erro na ordem das operações.

Algoritmo/estratégia: Somar as três notas primeiro e depois dividir o resultado por 3.
Python
media = (nota1 + nota2 + nota3) / 3

15. Função com retorno incorreto

Problema identificado: A função não está retornando corretamente a média das duas notas.

Algoritmo/estratégia: Criar a função, calcular a média e usar return para devolver o resultado.

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcular_media(8, 10)
print(resultado)
Resultado : 9. 0
