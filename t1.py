input()
degList = input().split(" ")

degList = [[int(degList[i]), i + 1] for i in range(0, len(degList))]

grafo = [[] for i in range(0, len(degList))]

for i in range(0, len(degList)):

    for j in range(1, degList[0][0] + 1):

        if degList[0][0] > len(grafo) - 1 or degList[len(degList) - 1][0] < 0:  # base da recursão
            print("Não é sequência gráfica!")
            exit()

        grafo[degList[0][1] - 1].append(degList[j][1])
        grafo[degList[j][1] - 1].append(degList[0][1])
        degList[0][0] -= 1
        degList[j][0] -= 1

    degList = degList[1:]  # a lista original será válida somente se essa nova for válida
    degList.sort(reverse=True, key=lambda x: x[0])

for i in range(0, len(grafo)):
    grafo[i].sort()
    for j in range(0, len(grafo[i])):
        print(str(grafo[i][j]), end=" ")

    print()
