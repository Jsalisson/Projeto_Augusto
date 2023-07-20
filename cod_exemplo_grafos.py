import networkx as nx

def encontrar_caminho_mais_curto(grafo, origem, destino):
    try:
        caminho_mais_curto = nx.shortest_path(grafo, source=origem, target=destino, weight='weight')
        distancia = nx.shortest_path_length(grafo, source=origem, target=destino, weight='weight')
        return caminho_mais_curto, distancia
    except nx.NetworkXNoPath:
        return None, None

if __name__ == "__main__":
    # Criar um grafo ponderado direcionado
    G = nx.DiGraph()

    # Adicionar arestas ao grafo com seus respectivos pesos (distâncias)
    G.add_edge('A', 'B', weight=4)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('B', 'C', weight=5)
    G.add_edge('B', 'D', weight=10)
    G.add_edge('C', 'D', weight=3)
    G.add_edge('D', 'A', weight=7)

    origem = 'A'
    destino = 'D'

    caminho, distancia = encontrar_caminho_mais_curto(G, origem, destino)

    if caminho:
        print(f"Caminho mais curto de {origem} para {destino}: {caminho}")
        print(f"Distância: {distancia}")
    else:
        print(f"Não há caminho entre {origem} e {destino}.")
