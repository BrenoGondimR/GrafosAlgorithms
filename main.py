import sys

# Função para encontrar o vértice com a distância mínima entre os vértices ainda não visitados
def encontrar_vertice_minimo(distancias, visitados):
    minimo = sys.maxsize
    minimo_indice = -1
    for i in range(len(distancias)):
        if distancias[i] < minimo and not visitados[i]:
            minimo = distancias[i]
            minimo_indice = i
    return minimo_indice

# Função para imprimir o caminho mínimo a partir do vértice inicial até o vértice de destino
def imprimir_caminho(caminho, destino):
    if caminho[destino] == -1:
        print(destino, end=' ')
        return
    imprimir_caminho(caminho, caminho[destino])
    print(destino, end=' ')

# Função que implementa o algoritmo de Dijkstra
def dijkstra(grafo, vertice_inicial):
    num_vertices = len(grafo)
    distancias = [sys.maxsize] * num_vertices  # Inicializa todas as distâncias como infinito
    distancias[vertice_inicial] = 0  # A distância para o vértice inicial é 0
    visitados = [False] * num_vertices
    caminho = [-1] * num_vertices

    for _ in range(num_vertices):
        u = encontrar_vertice_minimo(distancias, visitados)
        visitados[u] = True

        for v in range(num_vertices):
            if (
                grafo[u][v] > 0
                and not visitados[v]
                and distancias[v] > distancias[u] + grafo[u][v]
            ):
                distancias[v] = distancias[u] + grafo[u][v]
                caminho[v] = u

    # Imprimir as distâncias e os caminhos para todos os vértices
    print("Distâncias a partir do vértice inicial:")
    for i in range(num_vertices):
        if distancias[i] == sys.maxsize:
            print(f"Vértice {i}: inacessível")
        else:
            print(f"Vértice {i}: {distancias[i]}")

    print("\nCaminhos a partir do vértice inicial:")
    for i in range(num_vertices):
        if i != vertice_inicial:
            print(f"Caminho até o vértice {i}: ", end='')
            imprimir_caminho(caminho, i)
            print()

# Matriz de adjacência do grafo fornecido na imagem
grafo = [
            [0, 5, 7, 1, 0, 0, 0],
            [5, 0, 2, 3, 0, 0, 0],
            [7, 2, 0, 6, 5, 1, 0],
            [1, 3, 6, 0, 0, 5, 3],
            [0, 0, 5, 0, 0, 4, 1],
            [0, 0, 1, 5, 4, 0, 0],
            [0, 0, 0, 3, 1, 0, 0]
        ]

vertice_inicial = 0  # Escolha o vértice inicial aqui

dijkstra(grafo, vertice_inicial)
