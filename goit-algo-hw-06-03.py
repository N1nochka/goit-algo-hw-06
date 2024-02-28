import networkx as nx

# Створення графа
G = nx.Graph()

# Додавання міст і доріг з вагами
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

def dijkstra(graph, source):
    # Ініціалізація відстаней
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    
    # Створення множини відвіданих вершин
    visited = set()
    
    # Основний цикл алгоритму
    while len(visited) < len(graph.nodes()):
        # Вибір вершини з найменшою відстанню, яка ще не відвідана
        current_node = min((node for node in graph.nodes() if node not in visited), key=lambda x: distances[x])
        
        # Позначення поточної вершини як відвіданої
        visited.add(current_node)
        
        # Оновлення відстаней до сусідів поточної вершини
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                edge_weight = graph[current_node][neighbor]['weight']
                distances[neighbor] = min(distances[neighbor], distances[current_node] + edge_weight)
    
    return distances

# Застосування алгоритму Дейкстри для знаходження найкоротших шляхів від вершини 'A'
shortest_paths_from_A = dijkstra(G, source='A')

print("Найкоротші шляхи від вершини 'A' до всіх інших вершин:")
print(shortest_paths_from_A)
