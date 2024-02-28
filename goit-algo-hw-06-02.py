import networkx as nx
import matplotlib.pyplot as plt
import random

# Створення графа
G = nx.Graph()

# Додавання користувачів до графа
num_users = 50
for user_id in range(1, num_users + 1):
    G.add_node(f"User{user_id}")

# Максимальна кількість зв'язків
max_connections = 150

# Додавання ребер (зв'язків) між випадковими парами користувачів
connections_added = 0
while connections_added < max_connections:
    user1 = random.randint(1, num_users)
    user2 = random.randint(1, num_users)
    if user1 != user2 and not G.has_edge(f"User{user1}", f"User{user2}"):  # Виключимо петлі та дублікати
        G.add_edge(f"User{user1}", f"User{user2}")
        connections_added += 1

# Візуалізація графа
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray')
plt.title("Мережа Instagram")
plt.show()

# Функція для пошуку шляхів з використанням алгоритму DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Функція для пошуку шляхів з використанням алгоритму BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Виберіть випадковий початковий та кінцевий вузол
start_node = random.choice(list(G.nodes()))
end_node = random.choice(list(G.nodes()))

# Знаходження всіх шляхів між вибраними вузлами за допомогою DFS
print("Шляхи між", start_node, "та", end_node, "за допомогою DFS:")
for path in dfs_paths(G, start_node, end_node):
    print(path)

# Знаходження всіх шляхів між вибраними вузлами за допомогою BFS
print("\nШляхи між", start_node, "та", end_node, "за допомогою BFS:")
for path in bfs_paths(G, start_node, end_node):
    print(path)
