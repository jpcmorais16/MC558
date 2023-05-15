class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.father = self
        self.number_of_elements = 1

    def increase_number_of_elements(self, amount):
        self.number_of_elements += amount

    def set_father(self, new_father):
        self.father = new_father

    def union(self, outer_set):

        self.set_father(outer_set)

    def find_representative(self):
        if self.father == self:
            return self

        representative = self.father.find_representative()
        self.set_father(representative)

        return representative


n, m, k = input().split(" ")
n = int(n)
m = int(m)
k = int(k)

edges = []

disjoint_sets = [Node(i) for i in range(0, n)]

for i in range(0, m):
    v1, v2, weight = input().split(" ")

    new_edge = Edge(int(v1), int(v2), int(weight))

    edges.append(new_edge)

edges.sort(key=lambda edge: edge.weight)

total_components = n
total_weight = 0

for current_edge in edges:

    set1 = disjoint_sets[current_edge.v1]
    set2 = disjoint_sets[current_edge.v2]

    representative1 = set1.find_representative()
    representative2 = set2.find_representative()

    if representative1 != representative2:

        if representative1.number_of_elements >= representative2.number_of_elements:
            representative2.union(representative1)
            representative1.increase_number_of_elements(representative2.number_of_elements)

        else:
            representative1.union(representative2)
            representative2.increase_number_of_elements(representative1.number_of_elements)

        total_components -= 1
        total_weight += current_edge.weight

    if total_components == k:
        break

print(total_weight)
