import networkx as nx
import matplotlib.pyplot as plt
import random

# Створення порожнього графа
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

# Аналіз основних характеристик графа
print("Кількість користувачів:", G.number_of_nodes())
print("Кількість зв'язків:", G.number_of_edges())
print("Середня ступінь користувачів:", sum(dict(G.degree()).values()) / G.number_of_nodes())