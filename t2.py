class Vertice:

    def __init__(self, numero):
        self.numero = numero
        self.adj = []

    numero = 0
    # numeros dos vertices aos quais se conecta





n, m = input().split(" ")

n = int(n)
m = int(m)
vertices = []
arestas = []
for i in range(0, m):
    vertices.append(Vertice(i))

for i in range(0, m):
    (u, v, c) = input().split(" ")

    u, v, c = int(u), int(v), int(c)

    vertices[u].adj.append((v, c))
    vertices[v].adj.append((u, c))
    arestas.append((u, v))

arestas_restantes = m - 1
caminho = [0, vertices[0].adj[0][0]]

indice_vertice_atual = vertices[0].adj[0][0]
indice_proximo_vertice = indice_vertice_atual
cor_aresta = vertices[0].adj[0][1]

vertices[indice_vertice_atual].adj.remove((0, cor_aresta))
vertices[0].adj.remove((indice_vertice_atual, cor_aresta))

while True:
    if indice_vertice_atual != 0 and arestas_restantes == 0:
        print("Não possui trilha Euleriana alternante")
        exit()

    if indice_vertice_atual == 0 and arestas_restantes == 0:
        break

    for i in range(0, len(vertices[indice_vertice_atual].adj)):

        if vertices[indice_vertice_atual].adj[i][1] != cor_aresta:

            if indice_vertice_atual == indice_proximo_vertice or indice_proximo_vertice == 0:

                indice_proximo_vertice = vertices[indice_vertice_atual].adj[i][0]

                cor_aresta = vertices[indice_vertice_atual].adj[i][1]


    if indice_vertice_atual == indice_proximo_vertice:
        print("Não possui trilha Euleriana alternante")
        exit()

    vertices[indice_vertice_atual].adj.remove((indice_proximo_vertice, cor_aresta))
    vertices[indice_proximo_vertice].adj.remove((indice_vertice_atual, cor_aresta))

    caminho.append(indice_proximo_vertice)
    indice_vertice_atual = indice_proximo_vertice
    arestas_restantes -= 1


for i in range(0, len(caminho)):
    print(caminho[i], end=" ")



