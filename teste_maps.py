import networkx as nx
import matplotlib.pyplot as plt
import googlemaps

gmaps = googlemaps.Client(key='')

#lista de endereço dos alunos da escola
estudantes_endereco = ['rua vereador zino rodriges - PE','rua frei ricardo de pilar - PE','rua doutora francisca alves catao - PE','rua vereador zino rodrigues - PE']
escola_endereco = ''

#função para obter as coordenadas geográficas de um endereço (latitude e longitude) de um endereço
def coletar_coordenadas(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        localizacao = geocode_result[0]['geometria']['localizacao']
        return(localizacao['lat'],localizacao['long'])
    return None

#exemplo de como usar a função para obter as coordenadas dos alunos e da escola
coordenadas_estudantes =[coletar_coordenadas(address) for address in estudantes_endereco]
coordenadas_escola = coletar_coordenadas(escola_endereco)

print('Coordenadas dos alunos: ')
print(coordenadas_estudantes)
print('Coordenada da escola: ')
print(coordenadas_escola)



#daqui para baixo o cód só teve mudanças nas linhas 35 a 39, fora isso segue o mesmo
def create_graph(): 
    G = nx.Graph()

    # Adicione os nós dos pontos de coleta dos alunos e a escola
    G.add_nodes_from([('Aluno1', {'address': 'Endereço do Aluno'}),
                     ('Aluno2', {'address': 'Endereço do Aluno'}),
                     ('Aluno3', {'address': 'Endereço do Aluno'}),
                     ('Aluno4', {'address': 'Endereço do Aluno'}),
                     ('Escola', {'address': 'Endereço do Aluno'})])

    # Adicione as arestas (tempos de transporte em minutos) entre os pontos
    G.add_edge('Aluno1', 'Aluno2', weight=5)
    G.add_edge('Aluno1', 'Aluno3', weight=8)
    G.add_edge('Aluno1', 'Aluno4', weight=10)
    G.add_edge('Aluno1', 'Escola', weight=15)
    G.add_edge('Aluno2', 'Aluno3', weight=7)
    G.add_edge('Aluno2', 'Aluno4', weight=6)
    G.add_edge('Aluno2', 'Escola', weight=9)
    G.add_edge('Aluno3', 'Aluno4', weight=5)
    G.add_edge('Aluno3', 'Escola', weight=12)
    G.add_edge('Aluno4', 'Escola', weight=8)

    return G

def find_best_path(graph, source, students_to_collect, path=[]):
    path = path + [source]

    if len(path) == len(students_to_collect) + 1:
        return path

    best_path = None
    for neighbor in graph.neighbors(source):
        if neighbor not in path and neighbor in students_to_collect:
            new_path = find_best_path(graph, neighbor, students_to_collect, path)
            if new_path:
                if not best_path or calculate_total_weight(graph, new_path) < calculate_total_weight(graph, best_path):
                    best_path = new_path

    return best_path

def calculate_total_weight(graph, path):
    total_weight = 0
    for i in range(len(path) - 1):
        total_weight += graph[path[i]][path[i + 1]]['weight']
    return total_weight

import networkx as nx
import matplotlib.pyplot as plt

# Restante do código...

def main():
    graph = create_graph()

    students_to_collect = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4']
    start_node = 'Escola'

    best_path = find_best_path(graph, start_node, students_to_collect)

    # Imprima o trajeto ótimo
    print("Trajeto ótimo para coletar os alunos e levar para a escola:")
    print(best_path)

    # Desenhe o grafo com o trajeto ótimo destacado
    pos = nx.get_node_attributes(graph, 'pos')
    plt.figure(figsize=(10, 8))
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color='lightblue')
    nx.draw_networkx_nodes(graph, pos, nodelist=best_path, node_color='red', node_size=3000)

    # Converta o objeto zip em uma lista explícita
    edgelist = list(zip(best_path, best_path[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=edgelist, edge_color='red', width=3)

    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    main()
