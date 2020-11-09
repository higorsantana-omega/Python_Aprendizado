import numpy as np

class VetorNaoOrdenado():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaposiçao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultimaposiçao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultimaposiçao + 1):
                print(i, ' - ', self.valores[i])
    
    def insere(self, valor):
        if self.ultimaposiçao == self.capacidade - 1:
            print('Capacidade Máxima')
        else:
            self.ultimaposiçao += 1
            self.valores[self.ultimaposiçao] = valor
    
    def pesquisar(self, valor):
        for i in range(self.ultimaposiçao + 1):
            if valor == self.valores[i]:
                return i
        return -i

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaposiçao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaposiçao -= 1

vetor = VetorNaoOrdenado(5)
vetor.insere(2)
vetor.insere(21)
vetor.insere(6)
vetor.insere(3)
vetor.insere(1)
vetor.imprime()
print('--------------Excluir------------')
vetor.excluir(3)
vetor.imprime()
print(vetor.pesquisar(21))
