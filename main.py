import sys
import networkx as nx
import matplotlib.pyplot as plt

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

    # Criar o grafo utilizando a biblioteca networkx
    G = nx.Graph()
    for i in range(num_vertices):
        for j in range(num_vertices):
            if grafo[i][j] > 0:
                G.add_edge(i, j, weight=grafo[i][j])

    # Definir a posição dos vértices no gráfico
    pos = nx.spring_layout(G)

    # Definir as cores dos vértices e arestas
    node_colors = ['blue' if i == vertice_inicial else 'red' for i in range(num_vertices)]
    edge_colors = ['black' for _ in G.edges()]

    # Plotar o gráfico
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=800)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

# Matrizes de adjacência do grafo fornecidos nas imagens
grafo = [
            [0, 5, 7, 1, 0, 0, 0],
            [5, 0, 2, 3, 0, 0, 0],
            [7, 2, 0, 6, 5, 1, 0],
            [1, 3, 6, 0, 0, 5, 3],
            [0, 0, 5, 0, 0, 4, 1],
            [0, 0, 1, 5, 4, 0, 0],
            [0, 0, 0, 3, 1, 0, 0]
]

grafo2 = [
                [0, 0, 0, 0, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 11, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0],
                [0, 11, 0, 3, 0, 3, 5, 0, 0, 6, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5],
                [5, 1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0],
                [1, 0, 3, 0, 6, 0, 1, 0, 5, 7, 1, 0, 4, 0],
                [0, 0, 5, 4, 0, 1, 0, 0, 5, 7, 1, 0, 0, 0],
                [0, 0, 0, 0, 8, 0, 10, 0, 5, 7, 1, 0, 7, 0],
                [0, 0, 0, 0, 0, 6, 0, 10, 0, 0, 0, 0, 0, 0],
                [0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 13, 8, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 9, 6],
                [2, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 4, 0, 7, 0, 0, 9, 0, 0, 0],
                [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0],
        ]

vertice_inicial = 0  # Escolha o vértice inicial aqui

dijkstra(grafo, vertice_inicial)
