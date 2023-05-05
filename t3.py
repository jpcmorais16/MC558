def cor(cores, saida, chegada):

    for i in range(0, len(cores)):
        if cores[i][0] == saida and cores[i][1] == chegada:
            return cores[i][2]


def visitar(lista_adj, marcacao, ordem, posicao):
    if marcacao[posicao][1] == 1:
        return (marcacao, ordem)

    for vertice in lista_adj[posicao]:
        (marcacao, ordem) = visitar(lista_adj, marcacao, ordem, vertice[0])

    marcacao[posicao] = (marcacao[posicao][0], 1)
    ordem.append(posicao)

    return (marcacao, ordem)


def ordenacao_topologica(lista_adj):
    marcacao = [(i, 0) for i in range(0, len(lista_adj))]
    ordem = []

    for i in range(0, len(lista_adj)):
        (marcacao, ordem) = visitar(lista_adj, marcacao, ordem, i)

    ordem.reverse()

    return ordem


def n_caminhos(ordem_topologica, lista_adj, fim):

    caminhos = [[0, 0, 0] for i in range(0, len(lista_adj))]

    for vertice in ordem_topologica:

        for vertice_adj in lista_adj[vertice]:

            if vertice_adj[0] == fim:
                caminhos[vertice][vertice_adj[1]] += 1

    ordem_topologica.reverse()

    for vertice in ordem_topologica[2:]:

        for vertice_adj in lista_adj[vertice]:

            if vertice_adj[1] == 0:
                caminhos[vertice][0] += caminhos[vertice_adj[0]][0] + caminhos[vertice_adj[0]][1] + caminhos[vertice_adj[0]][2]

            if vertice_adj[1] == 1:
                caminhos[vertice][1] += caminhos[vertice_adj[0]][0] + caminhos[vertice_adj[0]][1]

            if vertice_adj[1] == 2:
                caminhos[vertice][2] += caminhos[vertice_adj[0]][0]

    return caminhos


n, m, s, t = input().split(" ")
n = int(n)
m = int(m)
s = int(s)
t = int(t)

if s == t:
    print(1)
    exit()

lista_adj = [[] for i in range(0, n)]

cores = []

for i in range(0, m):
    saida, chegada, cor = input().strip().split(" ")

    lista_adj[int(saida)].append((int(chegada), int(cor)))


ordem = ordenacao_topologica(lista_adj)

caminhos = n_caminhos(ordem, lista_adj, t)

print(sum(caminhos[int(s)]))
