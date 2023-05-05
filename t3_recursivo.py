class Aresta:
    def __init__(self, saida, chegada, cor):
        self.cor = cor
        self.saida = saida
        self.chegada = chegada

def Caminhos(arestas, inicio, fim):

    vetor_retorno = [0, 0, 0]

    for aresta in arestas:

        if aresta.saida == inicio:

            if (aresta.chegada == fim):
                vetor_retorno[aresta.cor] += 1
                continue

            vetor_caminhos = Caminhos(arestas, aresta.chegada, fim)

            if(aresta.cor == 2):
                vetor_retorno[2] += vetor_caminhos[0]

            if(aresta.cor == 1):
                vetor_retorno[1] += vetor_caminhos[0] + vetor_caminhos[1]

            if(aresta.cor == 0):
                vetor_retorno[0] += vetor_caminhos[0] + vetor_caminhos[1] + vetor_caminhos[2]

    return vetor_retorno

n, m, s, t = input().split(" ")
n = int(n)
m = int(m)
s = int(s)
t = int(t)


lista_adj = [[] for i in range(0, n)]

cores = []

arestas = []

for i in range(0, m):
    saida, chegada, cor = input().split(" ")

    aresta = Aresta(int(saida), int(chegada), int(cor))

    arestas.append(aresta)

caminhos = Caminhos(arestas, s, t)

print(sum(caminhos))