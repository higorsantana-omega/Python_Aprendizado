# https://wiki.python.org/moin/TimeComplexity


# Função manual
# Criamos uma lista vazia e vamos adicionando um por um (manualmente)
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

print(lista1())

# Função automatica
# 1 passo
def lista2():
    return range(1000)

l = lista2()

for i in l:
    print(i)