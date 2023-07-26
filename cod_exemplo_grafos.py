import networkx as nx
import matplotlib.pyplot as plt
import random

numero_1 = random.randint(1, 20)
numero_2 = random.randint(1, 20)
numero_3 = random.randint(1, 20)
numero_4 = random.randint(1, 20)
numero_5 = random.randint(1, 20)
numero_6 = random.randint(1, 20)
numero_7 = random.randint(1, 20)
numero_8 = random.randint(1, 20)
numero_9 = random.randint(1, 20)
numero_10 = random.randint(1, 20)
numero_11 = random.randint(1, 20)
numero_12 = random.randint(1, 20)
numero_13 = random.randint(1, 20)
numero_14 = random.randint(1, 20)
numero_15 = random.randint(20, 20)


# Função para gerar um número aleatório entre 1 e 20
def numero_aleatorio():
  return random.randint(1, 20)


var1 = [numero_aleatorio(), numero_aleatorio()]
var2 = [numero_aleatorio(), numero_aleatorio()]
var3 = [numero_aleatorio(), numero_aleatorio()]
var4 = [numero_aleatorio(), numero_aleatorio()]
var5 = [numero_aleatorio(), numero_aleatorio()]
var6 = [numero_aleatorio(), numero_aleatorio()]


def criar_grafo():
  G = nx.Graph()

  # Adicione os nós dos pontos de coleta dos alunos e a escola
  G.add_nodes_from([('Aluno1', {
    'pos': (var1)
  }), ('Aluno2', {
    'pos': (var2)
  }), ('Aluno3', {
    'pos': (var3)
  }), ('Aluno4', {
    'pos': (var4)
  }), ('Casa', {
    'pos': (var5)
  }), ('Escola', {
    'pos': (var6)
  })])

  G.add_edge('Casa', 'Escola', weight=14)

  G.add_edge('Aluno1', 'Aluno2', weight=numero_1)
  G.add_edge('Aluno1', 'Aluno3', weight=numero_2)
  G.add_edge('Aluno1', 'Aluno4', weight=numero_3)
  G.add_edge('Aluno1', 'Escola', weight=numero_4)
  G.add_edge('Casa', 'Aluno1', weight=numero_5)

  G.add_edge('Aluno2', 'Aluno3', weight=numero_6)
  G.add_edge('Aluno2', 'Aluno4', weight=numero_7)
  G.add_edge('Aluno2', 'Escola', weight=numero_8)
  G.add_edge('Casa', 'Aluno2', weight=numero_9)

  G.add_edge('Aluno3', 'Aluno4', weight=numero_11)
  G.add_edge('Aluno3', 'Escola', weight=numero_12)
  G.add_edge('Casa', 'Aluno3', weight=numero_13)

  G.add_edge('Aluno4', 'Escola', weight=numero_14)
  G.add_edge('Casa', 'Aluno4', weight=numero_15)

  return G


def encontrar_melhor_trajeto(grafo,
                             ponto_inicial,
                             alunos_a_coletar,
                             caminho=[]):
  caminho = caminho + [ponto_inicial]

  if len(caminho) == len(alunos_a_coletar) + 1:
    return caminho

  melhor_trajeto = None
  for vizinho in grafo.neighbors(ponto_inicial):
    if vizinho not in caminho and vizinho in alunos_a_coletar:
      novo_trajeto = encontrar_melhor_trajeto(grafo, vizinho, alunos_a_coletar,
                                              caminho)
      if novo_trajeto:
        if not melhor_trajeto or calcular_peso_total(
            grafo, novo_trajeto) < calcular_peso_total(grafo, melhor_trajeto):
          melhor_trajeto = novo_trajeto

  return melhor_trajeto


def calcular_peso_total(grafo, caminho):
  peso_total = 0
  for i in range(len(caminho) - 1):
    peso_total += grafo[caminho[i]][caminho[i + 1]]['weight']
  return peso_total


def main():
  grafo = criar_grafo()

  alunos_a_coletar = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4']
  ponto_inicial = 'Casa'

  melhor_trajeto = encontrar_melhor_trajeto(grafo, ponto_inicial,
                                            alunos_a_coletar)

  melhor_trajeto.append('Escola')

  # Imprima o trajeto ótimo
  print("Trajeto ótimo para coletar os alunos e levar para a escola:")
  print(melhor_trajeto)

  # Desenhe o grafo com o trajeto ótimo destacado
  pos = nx.get_node_attributes(grafo, 'pos')
  plt.figure(figsize=(10, 8))
  nx.draw(grafo, pos, with_labels=True, node_size=3000, node_color='lightblue')
  nx.draw_networkx_nodes(grafo,
                         pos,
                         nodelist=melhor_trajeto,
                         node_color='red',
                         node_size=3000)

  # Converta o objeto zip em uma lista explícita
  arestas = list(zip(melhor_trajeto, melhor_trajeto[1:]))
  nx.draw_networkx_edges(grafo,
                         pos,
                         edgelist=arestas,
                         edge_color='red',
                         width=3)

  labels = nx.get_edge_attributes(grafo, 'weight')
  nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
  plt.show()


if __name__ == "__main__":
  main()
