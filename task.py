import networkx as nx
import matplotlib.pyplot as plt

# Парсінг файлу
with open("cities.csv") as f:
    cities = [
        (lambda tokens: tokens[:-1] + [int(tokens[-1])])(line.split(';'))
        for line in f
    ]

# Створення та візуалізація графів
build_graph = nx.Graph()
build_graph.add_weighted_edges_from(cities)
nx.draw_networkx(build_graph)
plt.show()


# Функція знаходження найкоротшого маршруту
def short_route(graph, cities_1, cities_2):
    short_cut = nx.dijkstra_path(graph, cities_1, cities_2)
    distance = nx.dijkstra_path_length(graph, cities_1, cities_2)
    return f"Маршрут: {short_cut} найкоротший.  Відстань складає {distance} кілометрів"


print(short_route(build_graph, 'Kyiv', 'Sumy'))


