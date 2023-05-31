class Vertex:
    def __init__(self, id, weight):
        self.id = id
        self.list = []
        self.weight = weight

    def add_out_edge(self, edge_id):
        self.list.append(edge_id)


class Graph:
    def __init__(self, vertex_list, start_vertex_id, end_vertex_id):
        self.vertex_list = vertex_list
        self.start_vertex_id = start_vertex_id
        self.end_vertex_id = end_vertex_id

        self.distance_list = [-101*len(vertex_list) for i in range(0, len(vertex_list))]
        self.distance_list[start_vertex_id] = 100

    def relax(self, vertex_id1, vertex_id2):

        edge_weight = self.vertex_list[vertex_id2].weight
        distance1 = self.distance_list[vertex_id1]
        distance2 = self.distance_list[vertex_id2]

        if distance2 < distance1 + edge_weight\
               and distance1 + edge_weight > 0:

            self.distance_list[vertex_id2] = self.distance_list[vertex_id1] + edge_weight


n = int(input())

salas = input().split(" ")

weights = [int(salas[i]) for i in range(0, len(salas))]

m = int(input())

vertex_list = [Vertex(i, weights[i]) for i in range(0, len(weights))]
edges = []

for i in range(0, m):
    j, k = input().split(" ")
    edges.append((int(j), int(k)))
    vertex_list[int(j)].add_out_edge(int(k))

graph = Graph(vertex_list, 0, n-1)


for i in range(0, len(vertex_list) - 1):

    for j in range(0, len(edges)):

        first_vertex = edges[j][0]
        second_vertex = edges[j][1]

        graph.relax(first_vertex, second_vertex)

#print(graph.distance_list)
print("possible" if 100 + graph.distance_list[n-1] > 0 else "impossible")