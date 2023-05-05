def soma(lista):
    resultado = 0

    for i in range(0, len(lista)):
        resultado += lista[i]

    return resultado


def eh_sequencia_grafica(lista):
    # base

    if len(lista) == 1 and lista[0][0] == 0:
        return [[]]

    elif len(lista) == 1:
        print("ronaldo")
        return [-1]

    # recursao

    nova_lista = []

    for i in range(1, len(lista)):

        if i <= lista[0][0]:
            nova_lista.append((lista[i][0] - 1, lista[i][1]))

        else:
            nova_lista.append((lista[i][0], lista[i][1]))

    nova_lista_copia = nova_lista

    nova_lista.sort(reverse=True, key=lambda x: x[0])

    lista_adj = eh_sequencia_grafica(nova_lista)

    lista_adj.insert(0, [])

    for i in range(1, len(lista_adj)):
        for j in range(0, len(lista_adj[i])):
            lista_adj[i][j] += 1

    for i in range(1, 1 + lista[0][0]):
        lista_adj[nova_lista_copia[i-1][1] - 1].append(1)
        lista_adj[0].append(nova_lista_copia[i-1][1])

    # lista_adj[len(lista) - 1].reverse()

    return lista_adj


degList = input().split(" ")

degList = [(int(degList[i]), i + 1) for i in range(0, len(degList))]

if soma(degList[0]) % 2 != 0:
    print("falso")

resultado = eh_sequencia_grafica(degList)

for i in resultado:
    i.sort()

print(resultado)
