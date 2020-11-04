import timeit
# # A ideia de notação Big O é de descrever o comportamento geral.
# # Em termos do crescimento do numero de operações conforme cresce o numero
# # de elementos processados. (n)

# # n descreve o crescimento do algoritmo.
# # Quanto mais crescer o número de operações para processar, pior é o desempenho do algoritmo.
# # Pois ele executa mais instruções, e é mais "complexo"

# Como comparar dois algoritmos?
# Comparação objetiva entre algoritmos
# Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação
# O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas


# O(n)
# 11 passos
# menos desempenho
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

print(soma1(10))

# 3 passos
# mais desempenho
def soma2(n):
    return(n * (n + 1)) / 2

print(soma2(10))